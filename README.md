# Mini Kahoot via Terminal 🕹️

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Sockets](https://img.shields.io/badge/Sockets-TCP-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

Um jogo de perguntas e respostas estilo "Kahoot" executado inteiramente via terminal. Este projeto foi desenvolvido para demonstrar os conceitos de comunicação em rede utilizando a arquitetura Cliente-Servidor com Sockets TCP em Python.

## 📌 Sobre o Projeto

O sistema é composto por dois scripts (`servidor.py` e `cliente.py`). O servidor hospeda um quiz de múltipla escolha e aguarda a conexão de um cliente. O cliente se conecta, identifica-se e responde às questões em tempo real. Ao final, o servidor processa as respostas e devolve um boletim completo com os acertos e erros.

### Funcionalidades
- **Comunicação Confiável:** Utiliza o protocolo TCP (Transmission Control Protocol) para garantir a entrega das mensagens sem perdas.
- **Fluxo Interativo:** O servidor envia as perguntas sequencialmente, aguardando a resposta do usuário antes de prosseguir.
- **Validação de Entrada:** O cliente garante que o usuário digite apenas opções válidas (A, B, C ou D).
- **Feedback Detalhado:** Geração de um relatório final contendo o total de acertos e o gabarito comparativo (resposta do usuário vs. resposta correta).

---

## ⚙️ Arquitetura e Comunicação

A comunicação segue o seguinte fluxo:
1. `Servidor` abre o socket e escuta na porta `50000`.
2. `Cliente` conecta e envia o **Nome de Usuário**.
3. `Servidor` entra em um loop, enviando o enunciado da **Questão N**.
4. `Cliente` recebe, exibe, coleta a resposta (A/B/C/D) e envia de volta ao `Servidor`.
5. Após 3 iterações, o `Servidor` calcula a nota e envia a **String de Relatório Final**.
6. Conexão é encerrada.

---

## 🚀 Como Executar

### Pré-requisitos
O projeto utiliza apenas a biblioteca nativa `socket` do Python. **Nenhuma dependência externa é necessária.** Certifique-se apenas de ter o Python 3.x instalado em sua máquina.

### Passos para execução

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/mini-kahoot-terminal.git
   cd mini-kahoot-terminal
   ```

2. Abra um terminal e inicie o **Servidor**:
   ```bash
   python servidor.py
   ```
   *O servidor ficará aguardando conexões na porta 50000.*

3. Abra um **segundo terminal** (deixando o primeiro rodando) e inicie o **Cliente**:
   ```bash
   python cliente.py
   ```
   *Siga as instruções na tela para jogar!*
