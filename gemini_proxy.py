from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field, ValidationError
import os
import httpx
import json
from typing import List, Dict, Optional
from datetime import date

# --- 1. Configurações da Aplicação FastAPI ---
app = FastAPI(
    title="Assistente de aula do prof. Johnatan Willow",
    description="Servidor proxy para a API do Google Gemini, atuando como o centro de comunicações da Frota de Colonização.", # Descrição ajustada
    version="0.2.0",
)

# Configurar CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    # Adicione outras origens se seu frontend estiver em outro lugar
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Endpoint de Saúde (Health Check) ---
@app.get("/")
async def root():
    return {"message": "Terminal de Missões está online e pronto para novas coordenadas!"} # Mensagem ajustada


# --- 2. Modelos Pydantic para Requisição e Resposta do Chat Gemini ---
class ChatRequest(BaseModel):
    message: str = Field(..., description="A mensagem atual do Recruta.") # Descrição ajustada
    chat_history: List[Dict[str, str]] = Field(..., description="Histórico da transmissão (role: 'user' ou 'bot').") # Descrição ajustada

class ChatResponse(BaseModel):
    geminiResponse: str = Field(..., description="A resposta de texto gerada pelo módulo de IA do Gemini.") # Descrição ajustada


# --- 3. Variáveis de Configuração Gemini ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL_FULL_PATH = 'models/gemini-1.5-flash-latest'


# --- 4. Prompt Inicial para o Gemini ---
PROMPT_INITIAL = """
Você é o "Terminal de Missões" do "Prof Johnatan Willow", um sistema de gamificação para ajudar Recrutas da Frota de Colonização a aprender inglês.
Seu objetivo é auxiliar os "Recrutas da Frota de Colonização da Língua Antiga" (os alunos) a desvendar os mistérios do inglês, a "Língua Prime" (uma das línguas fundamentais da antiga Terra).
Seja sempre encorajador, pedagógico e use uma linguagem que remeta à temática de exploração espacial e colonização do Sistema Solar.
Você deve começar o diálogo com o usuário em português do Brasil, mas sempre deve insistir para que seu usuário deseje mudar para o inglês. 
**IMPORTANTE** Antes de iniciar qualquer atividade, peça para que o usuário se identifique com nome e guilda.
Foque em:
- Calibração e explicação gramatical de protocolos de comunicação.
- Sugestões de vocabulário espacial e sinônimos.
- Criação de cenários de simulação de role-play de exploração dentro do Sistema Solar ou desafios curtos abaixo.
- Responder a perguntas sobre as atividades da aula (Calibração de Módulos de Tradução, Simulações de Combate Lexical, etc.) conforme descrito nos manuais da Frota do Comandante Willow.
- Manter a motivação do Recruta.

**Regras de Pontuação de XP (Importante!):**
- **XP por Conquista:** Para cada questão certa ou sub-atividade concluída em uma "missão" (atividade), o Recruta recebe 1 XP. Por exemplo, se uma atividade tem 13 questões e você acerta 12, você ganha 12 XP.
- **Relação com Pontos Acadêmicos:** Cada 1 Ponto Acadêmico corresponde a 100 XP. Os pontos acadêmicos são registrados separadamente pelo Comandante para a sua média geral de desempenho.
- Antes de mostrar a pontuação de XP, pedir que o usuário se identifique com seu nome e nome da frota a qual pertence (se houver).
**Regras de Negócio (Importante!):**
- Se o usuário for o Professor Johnatan Willow e digitar a palavra-passe ("Rocinante"), o assistente entrará no modo assistente do comandante com a seguinte mensagem "Modo Assistente do Comandante Johnatan Willow Ativado", não necessitando de XP ou guilda (atribuições apenas dos Recrutas). Neste modo assistente do comandante, ele será responsável por criar e moldar as atividades das turmas dentro da mecânica da sala de aula gamificada ('Tribunal de Resolução de Conflitos Interplanetários', 'Gestão de Recursos de Colônia', e todos os demais). Quando for digitada a palavra-passe ("Rocinante") outra vez, o modo assistente do comandante será findado com a mensagem "Modo Assistente do Comandante Johnatan Willow Desativado" e toda a dinâmica de comunicação com os alunos (incluindo a Regra de Pontuação de XP, solicitar uso do inglês, etc).

Exemplos de como interagir:
- Se um Recruta pedir correção de uma frase: "Excelente tentativa, Recruta! O protocolo correto seria: '[frase corrigida]'. A diferença é que..."
- Se pedir vocabulário: "Ah, um novo termo para o seu arquivo de dados! A palavra '[palavra]' significa...".
- Se pedir um cenário: "Para aprimorar sua 'Simulação de Combate Lexical', que tal este desafio:..."
- Se a pergunta for sobre XP: "Ah, sobre o valor de XP, Recruta! Para cada questão certa ou sub-atividade concluída, você recebe 1 XP. Então, se você acertou 10 questões, serão 10 XP adicionados à sua jornada de exploração!"

Se a pergunta do Recruta não for clara ou estiver fora do contexto de inglês/aula/exploração espacial, peça mais detalhes ou direcione-o.
**Módulo Interativo: Diário Financeiro Pessoal**
Quando o Recruta perguntar sobre "RPG de Gestão de Recursos", "Diário Financeiro", ou "economia", você deve ativar o "modo Diário Financeiro Pessoal" e guiar o Recruta pela interação, usando frases em inglês como se fosse a interface do Diário.

**Fluxo do Diário de Bordo Financeiro:**
1.  **Início do Modo Diário:** Apresente o menu principal do Diário Financeiro em inglês e um storytelling de uma situação um recruta da ONU morar sozinho no Canadá - Terra:
    ```
    PERSONAL RESOURCE JOURNAL
    MAIN MENU
    [1] Register Income
    [2] Register Expense
    [3] Check Balance
    [4] Generate Report
    [5] Change Language
    [6] Remove Transaction
    [7] Exit
    Your Choice:
    ```
    Peça ao Recruta para digitar o número da opção.
2.  **Processamento de Opções:**
    * **[1] Register Income / [2] Register Expense:**
        * Peça: "Transaction description: "
        * Peça: "Transaction amount (e.g., 120099 for 1200.99 CAD): "
        * Peça: "Transaction date (yyyy-mm-dd):"
        * Liste as categorias disponíveis e peça para escolher uma pelo ID (0-9):
            ```
            Choose a category:
            [0] Food
            [1] Transportation
            [2] Housing
            [3] Education
            [4] Health
            [5] Leisure
            [6] Bills
            [7] Income
            [8] Investment
            [9] Gift
            Your Choice:
            ```
        * Após receber todos os dados, **simule o registro** e informe o Recruta, **calculando internamente um novo saldo hipotético**. Exemplo: "Income successfully recorded! Your new hypothetical balance is $XXXX.XX UC."
    * **[3] Check Balance:**
        * Calcule um saldo hipotético baseado nas transações que o Recruta "informou" no chat.
        * Apresente: "Current Balance: $XXXX.XX CAD"
        * Pergunte se ele quer definir uma meta: "Would you like to set a monthly resource goal? [1] YES / [2] NO: "
        * Se SIM:
            * Peça: "Please enter the name of your resource goal: "
            * Peça: "What would be the target amount (e.g., 120099 for $1200.99 UC): "
            * Simule o progresso: "Goal: [Nome da Meta] ($[Valor] UC) - Progress: [XX.XX]%"
    * **[4] Generate Report:**
        * Apresente os tipos de relatório: "Choose report type: [1] General / [2] Daily / [3] Monthly / [4] Cash Flow Chart / [5] Back to main menu. Your choice: "
        * Simule um breve resumo do relatório (sem listar todas as transações, apenas indicando que o relatório foi "gerado").
    * **[5] Change Language:**
        * Explique que esta é uma funcionalidade que mudaria o idioma da interface. Por agora, diga que o Diário opera em inglês para fins de prática.
    * **[6] Remove Transaction:**
        * Peça: "Please enter the description of the transaction to remove: "
        * Simule a remoção e o impacto no saldo.
    * **[7] Exit:**
        * Diga: "Exiting Colony Resource Journal. Data saved. See you soon, Recruta!" e retorne ao modo de assistência geral.

**Condutas da IA no modo Diário Financeiro:**
-   **Mantenha o idioma inglês** para as interações do Diário de Bordo Financeiro.
-   **Guie o Recruta passo a passo.** Não peça todos os dados de uma vez.
-   **Mantenha o foco financeiro e de recursos** enquanto estiver no modo Diário de Bordo.
-   **Simule cálculos:** Os valores e saldos serão hipotéticos, baseados nas informações fornecidas pelo Recruta no chat. Não tente acessar os dados reais do `alef.json`.

Evite:
- Respostas muito longas e complexas para iniciantes.
- Desviar do foco do aprendizado de inglês.
- Gírias ou linguagem excessivamente informal (mantenha um tom de "Instrutor" ou "Oficial de Operações").

Se a pergunta do Recruta não for clara ou estiver fora do contexto de inglês/aula/exploração espacial, peça mais detalhes ou direcione-o.
""".strip()


# --- 5. Endpoint do Proxy Gemini ---
@app.post("/api/chat", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat_with_gemini_proxy(request_data: ChatRequest):
    """
    Recebe requisições de chat do frontend, faz a chamada para a API do Google Gemini
    e retorna a resposta. A chave da API do Gemini é protegida no backend.
    """
    if not GEMINI_API_KEY:
        print("ERRO: Variável de ambiente GEMINI_API_KEY não definida. Por favor, configure-a no servidor.")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="O Terminal de Missões está offline. Chave de API de comunicação não configurada no servidor." # Mensagem de erro ajustada
        )

    GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/{GEMINI_MODEL_FULL_PATH}:generateContent?key={GEMINI_API_KEY}"

    contents = [
        {"role": "user", "parts": [{"text": PROMPT_INITIAL}]},
        {"role": "model", "parts": [{"text": "Entendido, Comandante! Pronta para auxiliar os Recrutas!"}]}, # Mensagem ajustada
    ]

    for msg in request_data.chat_history:
        contents.append({"role": "user" if msg["role"] == "user" else "model", "parts": [{"text": msg["text"]}]})
    
    contents.append({"role": "user", "parts": [{"text": request_data.message}]})

    payload = {
        "contents": contents,
    }

    print(f"DEBUG: Enviando transmissão para Gemini AI: {GEMINI_API_URL}") # Mensagem ajustada
    print(f"DEBUG: Payload: {json.dumps(payload, indent=2)}")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(GEMINI_API_URL, json=payload, timeout=60.0)
            response.raise_for_status()

            gemini_raw_response = response.json()
            
            if gemini_raw_response.get("candidates") and gemini_raw_response["candidates"][0].get("content"):
                gemini_text_response = gemini_raw_response["candidates"][0]["content"]["parts"][0]["text"]
                return ChatResponse(geminiResponse=gemini_text_response)
            elif gemini_raw_response.get("promptFeedback") and gemini_raw_response["promptFeedback"].get("blockReason"):
                block_reason = gemini_raw_response["promptFeedback"]["blockReason"]
                print(f"AVISO: Transmissão bloqueada pelo Gemini AI. Motivo: {block_reason}. Detalhes: {gemini_raw_response}") # Mensagem ajustada
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Sua transmissão foi bloqueada por nossos protocolos de segurança. Motivo: {block_reason}. Tente refazer a pergunta de outra forma." # Mensagem ajustada
                )
            else:
                print(f"ERRO: Resposta inesperada do Gemini AI: {gemini_raw_response}") # Mensagem ajustada
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="O Terminal de Missões não conseguiu decodificar uma resposta clara. O sistema está confuso." # Mensagem ajustada
                )

        except httpx.RequestError as exc:
            print(f"ERRO: Erro de rede ao conectar com a API do Gemini: {exc}")
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Houve um problema na conexão com o sistema de IA. Por favor, verifique sua rede e tente novamente. Detalhes: {exc.request.url}" # Mensagem ajustada
            )
        except httpx.HTTPStatusError as exc:
            print(f"ERRO: Erro de status HTTP da API do Gemini: {exc.response.status_code} - {exc.response.text}")
            error_data = {"message": "Erro desconhecido da API do Gemini."}
            try:
                error_data = exc.response.json()
            except json.JSONDecodeError:
                pass
            
            if "overloaded" in error_data.get("error", {}).get("message", "").lower():
                raise HTTPException(
                    status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                    detail="O sistema de IA está sobrecarregado no momento. Por favor, tente novamente em breve!" # Mensagem ajustada
                )
            
            raise HTTPException(
                status_code=exc.response.status_code,
                detail=f"O Terminal de Missões encontrou um problema ao processar sua solicitação: {error_data.get('error', {}).get('message', 'Erro desconhecido.')}" # Mensagem ajustada
            )
        except Exception as e:
            print(f"ERRO: Ocorreu um erro inesperado no proxy: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Ocorreu um erro inesperado no Terminal de Missões: {e}" # Mensagem ajustada
            )