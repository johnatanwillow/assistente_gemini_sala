// script.js

// 1. Variáveis Globais e Seletores de Elementos
// ===============================================
const readIntroButton = document.getElementById('read-intro-button');
const introTextElement = document.querySelector('.intro-text');    

const chatSection = document.getElementById('chat-section');
const chatWindow = document.getElementById('chat-window');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const sendButton = chatForm.querySelector('.btn-send');

let chatHistory = []; // Manterá o histórico da conversa para enviar ao backend
let isSendingMessage = false; // Flag para evitar múltiplas submissões

const PROMPT_INITIAL = ""; // Vazio ou remova completamente, ele será enviado do backend.


// 2. Funções Auxiliares (mantidas, pois são genéricas para a UI)
// =====================

/**
 * Usa a Web Speech API para falar um determinado texto.
 * @param {string} text - O texto a ser falado.
 * @param {string} [lang='auto'] - O idioma do texto (ex: 'en-US', 'pt-BR'). 'auto' para detecção.
 */
function speakText(text, lang = 'auto') {
    if ('speechSynthesis' in window) {
        const utterance = new SpeechSynthesisUtterance(text);

        // Se o idioma for 'auto', tenta adivinhar o idioma do texto.
        // Uma forma simples é verificar padrões de palavras ou usar uma biblioteca (mais complexo).
        // Por enquanto, vamos priorizar o que for explícito.
        let detectedLang = lang;
        if (lang === 'auto') {
            // Tentativa de detecção básica baseada em palavras-chave ou padrões
            if (text.toLowerCase().includes('bem-vindo') || text.toLowerCase().includes('olá') || text.toLowerCase().includes('português')) {
                detectedLang = 'pt-BR';
            } else {
                detectedLang = 'en-US'; // Padrão para inglês se não for detectado português
            }
        }

        const voices = speechSynthesis.getVoices();
        let selectedVoice = null;

        if (detectedLang.startsWith('pt-')) {
            // Tenta encontrar uma voz em português do Brasil
            selectedVoice = voices.find(voice => 
                voice.lang.startsWith('pt-') && 
                (voice.name.includes('Google português do Brasil') || voice.name.includes('Portuguese (Brazil)'))
            );
        } else if (detectedLang.startsWith('en-')) {
            // Tenta encontrar uma voz em inglês que soe mais "natural"
            selectedVoice = voices.find(voice => 
                voice.lang.startsWith('en-') && 
                (voice.name.includes('Google US English') || voice.name.includes('Google UK English') || 
                 voice.name.includes('English (United States)') || voice.name.includes('English (United Kingdom)'))
            );
        }

        if (selectedVoice) {
            utterance.voice = selectedVoice;
            utterance.lang = selectedVoice.lang; // Define a linguagem da fala com base na voz encontrada
        } else {
            // Fallback: se nenhuma voz específica for encontrada, usa a linguagem detectada
            utterance.lang = detectedLang;
            console.warn(`Nenhuma voz específica encontrada para ${detectedLang}. Usando voz padrão do navegador.`);
        }

        utterance.rate = 1.0; // Velocidade da fala (1.0 é normal)
        utterance.pitch = 1.0; // Tonalidade (1.0 é normal)

        speechSynthesis.speak(utterance);
    } else {
        console.warn('Seu navegador não suporta a API de Síntese de Fala.');
        alert('Seu navegador não suporta a API de Síntese de Fala.');
    }
}


/**
 * Adiciona uma mensagem ao chat.
 * @param {string} message - O texto da mensagem.
 * @param {'user'|'bot'} type - O tipo de mensagem ('user' ou 'bot').
 */
function addMessageToChat(message, type) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message', `${type}-message`);
    messageElement.innerHTML = message; // Usar innerHTML para permitir quebras de linha e formatação básica

    // Se for uma mensagem do bot, adiciona um botão de áudio
    if (type === 'bot') {
        const audioButton = document.createElement('button');
        audioButton.classList.add('audio-button');
        audioButton.innerHTML = '<img src="./imagens/speaker.svg" alt="Ouvir" class="speaker-icon">';
        
        audioButton.onclick = () => {
            speakText(message);
        };
        messageElement.appendChild(audioButton);
    }

    chatWindow.appendChild(messageElement);

    // Rola para o final da janela de chat
    chatWindow.scrollTop = chatWindow.scrollHeight;
}


/**
 * Exibe uma mensagem de status na interface.
 * Esta função não será mais usada para o status da API Key, mas pode ser útil para outros status.
 * @param {string} message - O texto da mensagem de status.
 * @param {'success'|'error'|'info'} type - O tipo de status.
 */
function displayStatus(message, type) {
    const generalStatusDiv = document.getElementById('general-status'); // Você precisaria adicionar este div no HTML
    if (generalStatusDiv) {
        generalStatusDiv.textContent = message;
        generalStatusDiv.className = `general-status ${type}`; // Adicione classes para estilização
    } else {
        console.log(`Status (${type}): ${message}`); // Apenas loga no console se o div não existir
    }
}

/**
 * Habilita/Desabilita os elementos da interface de chat.
 * @param {boolean} enable - True para habilitar, false para desabilitar.
 */
function toggleChatInterface(enable) {
    userInput.disabled = !enable;
    sendButton.disabled = !enable;
    // Se estiver habilitando, remove a classe hidden da seção de chat
    if (enable) {
        chatSection.classList.remove('hidden');
    }
}


// 3. Integração com o Backend (Seu novo servidor Python)
// ===================================

/**
 * Envia uma mensagem para o endpoint do seu backend e obtém a resposta do Gemini.
 * @param {string} message - A mensagem do usuário.
 */
async function sendMessageToBackend(message) {
    if (isSendingMessage) return; // Evita envio duplicado
    isSendingMessage = true;
    userInput.disabled = true; // Desabilita input e botão enquanto envia
    sendButton.disabled = true;
    sendButton.innerHTML = '<span class="loading-spinner"></span>'; // Adiciona spinner

    addMessageToChat(message, 'user');
    chatHistory.push({ role: 'user', text: message }); // Adiciona ao histórico do frontend

    try {
        const backendUrl = 'http://127.0.0.1:8000/api/chat'; // Ajuste a porta se você rodar seu backend em outra porta

        const response = await fetch(backendUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                chat_history: chatHistory.slice(0, -1)
            }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            console.error('Erro do backend proxy:', errorData);
            throw new Error(`Sim! Temos um COMMUNICATION ERROR com o Assistente Espacial: ${errorData.detail || response.statusText}`);
        }

        const data = await response.json();
        const botResponse = data.geminiResponse;

        addMessageToChat(botResponse, 'bot');
        chatHistory.push({ role: 'bot', text: botResponse });

    } catch (error) {
        console.error('Erro ao comunicar com o backend:', error);
        addMessageToChat(`Alô! Houston! Temos um problema na comunicação com o Assistente Espacial: ${error.message}. Não fique fora de órbita!`, 'bot');
    } finally {
        isSendingMessage = false;
        userInput.value = '';
        userInput.disabled = false;
        sendButton.innerHTML = '<img src="./imagens/send-icon.svg" alt="Enviar" class="send-icon">';
        sendButton.disabled = false;
        userInput.focus();
    }
}


// 4. Listeners de Eventos
// =======================

// Listener para o botão "Ouvir Introdução"
if (readIntroButton && introTextElement) {
    readIntroButton.addEventListener('click', () => {
        // Passa 'pt-BR' explicitamente para a introdução em português
        speakText(introTextElement.textContent, 'pt-BR'); 
    });
}

// Listener para o formulário de chat
chatForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const message = userInput.value.trim();

    if (message && !isSendingMessage) {
        sendMessageToBackend(message);
    }
});

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    toggleChatInterface(true);
    userInput.focus();
});