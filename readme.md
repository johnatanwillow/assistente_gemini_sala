# Assistente de Aulas - Prof. Johnatan Willow 🚀
--- 
Este projeto é um sistema de gamificação para auxiliar Recrutas da Frota de Colonização Espacial a aprender inglês, a "Língua Prime" 🚀🚀🚀. Ele utiliza um assistente de IA baseado na API do Google Gemini, atuando como um "Terminal de Missões" para fornecer suporte pedagógico, calibração gramatical, sugestões de vocabulário, cenários de role-play e gerenciamento de XP.

## Sumário 📜

* [Visão Geral](#visão-geral)
* [Agente de IA: Um Parceiro de Estudos Inteligente](#agente-de-ia-um-parceiro-de-estudos-inteligente)
    * [Funcionalidades Principais](#funcionalidades-principais)
    * [Capacidades Detalhadas do Agente de IA](#capacidades-detalhadas-do-agente-de-ia)
        * [1. Conversação Personalizada: Praticando o Diálogo em Inglês](#1-conversação-personalizada-praticando-o-diálogo-em-inglês)
        * [2. Suporte 24 Horas por Dia, 7 Dias por Semana: Tire Suas Dúvidas a Qualquer Hora](#2-suporte-24-horas-por-dia-7-dias-por-semana-tire-suas-dúvidas-a-qualquer-hora)
        * [3. Atividades e Jogos Interativos: Aprendendo se Divertindo](#3-atividades-e-jogos-interativos-aprendendo-se-divertindo)
        * [4. Análise de Progresso e Melhora no Ensino: Entendendo o seu Desempenho](#4-análise-de-progresso-e-melhora-no-ensino-entendendo-o-seu-desempenho)
        * [5. Ajuda para Escrever e Corrigir Textos](#5-ajuda-para-escrever-e-corrigir-textos)
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

## Agente de IA: Um Parceiro de Estudos Inteligente ✨

Este projeto, o "Assistente de Aulas - Prof. Johnatan Willow", é como um **parceiro de estudo inteligente** que usa a tecnologia de Inteligência Artificial para te ajudar a aprender inglês. Ele funciona como um "Terminal de Missões" da nossa Frota de Colonização Espacial, tornando o aprendizado divertido e eficaz.

### Funcionalidades Principais

Aqui estão as principais características do nosso assistente de IA:

* **Assistência de IA:** Oferece um suporte dinâmico para suas dúvidas de inglês (como gramática, vocabulário e mais) usando o poderoso modelo Gemini 1.5 Flash.
* **Temática Gamificada:** Proporciona uma experiência de aprendizado envolvente e divertida com uma linguagem e cenários inspirados na exploração espacial.
* **Módulos de Treinamento:** Contém diversas atividades específicas, como "Calibração de Módulos de Tradução", "Simulações de Combate Lexical" e um "RPG: Diário Financeiro Pessoal", para você praticar diferentes habilidades.
* **Sistema de XP:** Você ganha pontos de experiência (XP) ao concluir atividades, o que te motiva a aprender cada vez mais.
* **Modo Comandante:** Existe um modo especial para o Professor Johnatan Willow, onde ele pode gerenciar e adaptar as atividades para a turma.
* **Proxy Seguro:** O sistema de bastidores (backend) protege a chave de acesso da IA (API Key do Gemini), garantindo que ela não fique exposta na parte visível do site (frontend).

### Capacidades Detalhadas do Agente de IA

Vamos ver em detalhes o que ele já consegue fazer e onde podemos torná-lo ainda melhor:

#### 1. Conversação Personalizada: Praticando o Diálogo em Inglês

* **Simulação de Diálogos:** **Já Faz!** Nosso agente de IA pode criar conversas simuladas, como se você estivesse em uma situação real (por exemplo, viajando, fazendo uma entrevista, ou pedindo comida em um restaurante). Você pode praticar seu inglês falando com ele, sem medo de errar, em um ambiente seguro e temático de exploração espacial.
* **Feedback Instantâneo (O que acertar e melhorar):** **Já Faz!** Quando você fala ou escreve, o agente consegue te dizer na hora o que precisa ser ajustado na sua gramática (as regras da língua), na forma como você pronuncia as palavras, na sua fluidez (o quão "natural" você soa) e no seu vocabulário. Ele te mostra a correção e explica o porquê, como um "protocolo correto".
* **Adaptação ao Seu Nível (Mais fácil ou mais difícil):** **Já Faz!** Como o nosso assistente usa uma inteligência artificial avançada (a API Google Gemini), ele consegue perceber o seu nível de inglês. Assim, ele adapta as conversas e as palavras usadas para que você sempre tenha um desafio que te motive, sem ser muito fácil nem muito difícil.

#### 2. Suporte 24 Horas por Dia, 7 Dias por Semana: Tire Suas Dúvidas a Qualquer Hora

* **Respostas para Suas Perguntas:** **Já Faz!** Se você tiver dúvidas sobre gramática, o significado de uma palavra, ou alguma expressão em inglês, pode perguntar ao agente a qualquer momento. Ele dará explicações claras e exemplos. Ele também pode responder perguntas sobre as atividades da aula, como os "Módulos de Tradução" ou "Simulações de Combate Lexical".
* **Material de Apoio (Áudio e Vocabulário):** **Parcialmente Implementado / Sugestão de Melhoria.** O agente pode te dar sugestões de vocabulário e sinônimos relacionados ao espaço. Além disso, as respostas do Terminal de Missões podem ser ouvidas em voz alta (como uma "transmissão de boas-vindas"), o que ajuda na pronúncia. Para o futuro, poderíamos pensar em como o agente poderia também te indicar ou gerar links para vídeos ou outros materiais de apoio de forma mais direta.

#### 3. Atividades e Jogos Interativos: Aprendendo se Divertindo

* **Exercícios Adaptativos (Desafios Sob Medida):** **Já Faz!** O agente pode criar pequenos desafios e atividades interativas (como os "Protocolos de Treinamento" listados no site, por exemplo, "Rastreamento de Sondas Perdidas" ou "Simulações de Combate Lexical"). Ele pode até mesmo gerar exercícios específicos com base nas áreas que você mais precisa melhorar.
* **Gamificação (Aulas Viram Missões!):** **Já Faz!** Todo o sistema foi pensado como um jogo! Você é um "Recruta da Frota de Colonização Espacial", e suas tarefas são "Missões". Você ganha Pontos de Experiência (XP) a cada acerto, e temos até um "RPG: Diário Financeiro Pessoal" para você aprender sobre finanças em inglês de forma divertida.

#### 4. Análise de Progresso e Melhora no Ensino: Entendendo o seu Desempenho

* **Identificação de Erros Comuns:** **Parcialmente Implementado / Sugestão de Melhoria.** O agente de IA consegue perceber os erros que você comete durante a conversa e te ajudar a corrigi-los na hora. No entanto, ele não "guarda" um histórico dos seus erros ao longo do tempo (entre diferentes sessões) para criar relatórios detalhados para o professor. Para o futuro, poderíamos desenvolver essa capacidade de "lembrar" seus padrões de erro persistentes.
* **Planos de Estudo Personalizados:** **Parcialmente Implementado / Sugestão de Melhoria.** A IA já adapta a conversa em tempo real ao seu nível e necessidades. Mas ela não gera um "plano de estudos" completo e estruturado para você seguir por vários dias ou semanas. Isso seria uma funcionalidade mais avançada para o futuro, onde o agente poderia criar trilhas de aprendizado mais longas e personalizadas.

#### 5. Ajuda para Escrever e Corrigir Textos

* **Assistência na Escrita:** **Já Faz!** O módulo de "Calibração de Módulos de Tradução" e a capacidade de dar feedback sobre gramática e vocabulário significam que o agente pode te ajudar a escrever textos, sugerindo como melhorar suas frases, a ortografia e o estilo.
* **Correção de Atividades Escritas:** **Já Faz!** Assim como ele corrige suas frases durante a conversa, o agente pode te ajudar a corrigir exercícios de escrita, mostrando onde você errou e explicando a forma correta. Isso torna o processo mais rápido para o professor e dá um retorno detalhado para você, Recruta.

## Estrutura do Projeto
```json
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
