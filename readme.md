# Assistente de Aulas - Prof. Johnatan Willow 🚀
--- 
Este projeto é um sistema de gamificação para auxiliar Recrutas da Frota de Colonização Espacial a aprender inglês, a "Língua Prime" 🚀🚀🚀. Ele utiliza um assistente de IA baseado na API do Google Gemini, atuando como um "Terminal de Missões" para fornecer suporte pedagógico, calibração gramatical, sugestões de vocabulário, cenários de role-play e gerenciamento de XP.

## Sumário 📜

* [Visão Geral](#visão-geral)
* [Funcionalidades](#funcionalidades)
* [Estrutura do Projeto](#estrutura-do-projeto)
* [Segurança e Informações Sensíveis](#segurança-e-informações-sensíveis)
* [Configuração e Instalação](#configuração-e-instalação)
    * [Pré-requisitos](#pré-requisitos)
    * [Instalação](#instalação)
* [Como Executar](#como-executar)
* [Uso](#uso)
* [Créditos](#créditos)

---

## Visão Geral 🌌

O "Assistente de Aulas" é uma aplicação web que simula um ambiente de exploração espacial e colonização, onde os alunos (Recrutas) interagem com um "Terminal de Missões" (assistente de IA) para melhorar suas habilidades em inglês. O sistema inclui um backend em FastAPI que serve como proxy para a API do Google Gemini, garantindo a segurança da chave de API, e um frontend interativo com HTML, CSS e JavaScript.

## Funcionalidades ✨

* **Assistência de IA:** Suporte dinâmico para dúvidas de inglês (gramática, vocabulário, etc.) através do modelo Gemini 1.5 Flash.
* **Temática Gamificada:** Experiência imersiva com linguagem e cenários de exploração espacial.
* **Módulos de Treinamento:** Diversas atividades como "Calibração de Módulos de Tradução", "Simulações de Combate Lexical" e "RPG: Diário Financeiro Pessoal".
* **Sistema de XP:** Pontuação por atividades concluídas, incentivando o aprendizado.
* **Modo Comandante:** Um modo especial para o Professor Johnatan Willow gerenciar e moldar atividades da turma.
* **Proxy Seguro:** O backend protege a chave de API do Gemini, não a expondo no frontend.

## Estrutura do Projeto
assistente_gemini_sala/
├── .gitignore
├── gemini_proxy.py
├── index.html
├── readme.md
├── requirements.txt
├── script.js
└── styles.css
└── imagens/ (diretório para imagens do frontend)
 `gemini_proxy.py`: Backend FastAPI que atua como proxy para a API do Google Gemini. 🐍
* `index.html`: Estrutura principal do frontend da aplicação. 🌐
* `styles.css`: Estilos CSS para a interface da aplicação. 🎨
* `script.js`: Lógica JavaScript para interatividade do frontend, comunicação com o proxy e síntese de fala. 💻
* `requirements.txt`: Lista as dependências Python necessárias para o backend. 📦
* `.gitignore`: Define os arquivos e diretórios que devem ser ignorados pelo controle de versão Git, incluindo o arquivo de variáveis de ambiente (`.env`). 🚫
* `readme.md`: Este arquivo, contendo informações sobre o projeto. 📄
* `imagens/`: Contém os ativos de imagem utilizados no frontend (e.g., `Foto G.png`, `send-icon.svg`, `speaker.svg`, ícones de funcionalidades). 🖼️

## Segurança e Informações Sensíveis 🛡️

A chave de API do Gemini é uma informação sensível e é tratada com segurança nesta aplicação.

* **Não Exposição no Frontend:** A chave de API **não** é exposta no código do frontend (`script.js` ou `index.html`). Todas as chamadas para a API do Gemini são feitas através do backend (`gemini_proxy.py`). ⛔
* **Uso de Variáveis de Ambiente:** A chave de API é carregada do ambiente através de `os.getenv("GEMINI_API_KEY")`. Isso significa que a chave não é hardcoded no código-fonte. 🔑
* **Exclusão no Git:** O arquivo `.gitignore` inclui explicitamente `.env`, garantindo que arquivos contendo variáveis de ambiente locais (como sua chave de API) não sejam acidentalmente enviados para o repositório Git público. 🕵️‍♀️

**Recomendação:** Sempre utilize variáveis de ambiente para armazenar sua chave de API do Gemini e **nunca** a inclua diretamente no código ou em arquivos versionados. ⚠️

## Configuração e Instalação 🛠️

### Pré-requisitos ✅

* Python 3.8+
* `pip` (gerenciador de pacotes do Python)
* Uma chave de API do Google Gemini. Você pode obtê-la em [Google AI Studio](https://ai.google.dev/).

### Instalação ⬇️

1.  **Clone o Repositório:**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO>
    cd assistente_gemini_sala
    ```

2.  **Crie um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv venv
    ```

3.  **Ative o Ambiente Virtual:**
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Instale as Dependências do Python:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure a Chave de API do Gemini:**
    Crie um arquivo `.env` na raiz do projeto (o mesmo nível de `gemini_proxy.py`) e adicione sua chave de API. **Este arquivo já está no `.gitignore` para sua segurança.**
    ```dotenv
    GEMINI_API_KEY="SUA_CHAVE_DE_API_DO_GEMINI_AQUI"
    ```
    Substitua `"SUA_CHAVE_DE_API_DO_GEMINI_AQUI"` pela sua chave de API real do Gemini.

## Como Executar ▶️

1.  **Certifique-se de que o ambiente virtual está ativado** e que você configurou a variável de ambiente `GEMINI_API_KEY`.

2.  **Inicie o servidor FastAPI (Backend):**
    ```bash
    uvicorn gemini_proxy:app --reload --port 8000
    ```
    Isso iniciará o servidor na porta `8000`. O `--reload` é útil para desenvolvimento, pois reinicia o servidor automaticamente a cada alteração no código.

3.  **Abra o Frontend:**
    Navegue até o arquivo `index.html` no seu navegador web. Você pode simplesmente abrir o arquivo HTML diretamente ou usar uma extensão de servidor local (como "Live Server" no VS Code) para serví-lo, o que é recomendado para evitar problemas de CORS.

## Uso 💬

* Ao acessar `index.html`, o assistente de IA estará pronto para interagir. 👋
* Digite suas perguntas ou comandos na caixa de texto e clique no botão de enviar (ícone de foguete). ➡️
* Você pode interagir com os diferentes "Protocolos de Treinamento" listados na seção de funcionalidades. 🗺️
* Se o usuário for o Professor Johnatan Willow, digitar a palavra-passe "Rocinante" ativará o "Modo Assistente do Comandante Johnatan Willow". 👨‍✈️
* O botão "Ouvir Transmissão de Boas-Vindas" lerá a introdução do site em português. 🔊

## Créditos 🙏

* Desenvolvido por Prof. Johnatan Willow. 🧑‍💻
* Baseado em estratégias, implementações e mecânicas autorais de gamificação na sala de aula de inglês. 🎓
* Impulsionado pela API do Google Gemini. ♊