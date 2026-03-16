import socket

QUESTOES = [
    {
        "enunciado": "Q1. Em redes, qual protocolo é orientado à conexão?\nA) UDP\nB) TCP\nC) ICMP\nD) ARP",
        "correta": "B"
    },
    {
        "enunciado": "Q2. Qual dessas estruturas de dados usa o princípio LIFO (Last In, First Out)?\nA) Fila\nB) Árvore\nC) Pilha\nD) Grafo",
        "correta": "C"
    },
    {
        "enunciado": "Q3. Qual camada do modelo OSI é responsável pelo roteamento de pacotes?\nA) Enlace\nB) Rede\nC) Transporte\nD) Aplicação",
        "correta": "B"
    }
]

def iniciar_servidor():
    HOST = '127.0.0.1'
    PORTA = 50000

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((HOST, PORTA))
    servidor.listen(1)

    print(f"[*] Servidor do Quiz rodando em {HOST}:{PORTA}")
    print("[*] Aguardando competidores...")

    while True:
        conexao, endereco = servidor.accept()
        print(f"\n[+] Nova conexão de {endereco}")

        try:
            nome_usuario = conexao.recv(1024).decode('utf-8').strip()
            if not nome_usuario:
                break
            
            print(f"[*] Usuário conectado: {nome_usuario}")

            acertos = 0
            feedback = []

            for i, q in enumerate(QUESTOES):
                # 1. Envia a questão
                conexao.sendall(q["enunciado"].encode('utf-8'))

                # 2. Recebe a resposta do cliente
                resposta_cliente = conexao.recv(1024).decode('utf-8').strip().upper()

                # 3. Corrige e envia o feedback imediato
                resposta_correta = q["correta"]
                if resposta_cliente == resposta_correta:
                    acertos += 1
                    msg_imediata = "✅ Resposta Correta!"
                else:
                    msg_imediata = f"❌ Resposta Incorreta! A alternativa certa era a {resposta_correta}."
                
                conexao.sendall(msg_imediata.encode('utf-8'))

                # 4. Aguarda a confirmação do cliente para não encavalar as mensagens (TCP Stream)
                conexao.recv(1024)

                # Salva para o relatório final
                feedback.append(f"Q{i+1} (resposta: {resposta_cliente} | correta: {resposta_correta})")

            # 5. Prepara e envia o relatório final
            relatorio = f"\n--- Resultado Final ---\n"
            relatorio += f"Usuário: {nome_usuario}\n"
            relatorio += f"Total de acertos: {acertos}/3\n"
            relatorio += "\n".join(feedback)
            
            conexao.sendall(relatorio.encode('utf-8'))
            print(f"[*] Quiz finalizado para {nome_usuario}. Relatório enviado.")

        except Exception as e:
            print(f"[-] Erro na conexão: {e}")
        finally:
            # Encerra a conexão com este cliente específico
            conexao.close()
            print("[*] Conexão com o cliente encerrada.")
        
        # O BREAK faz o servidor sair do loop "while True" após atender 1 cliente
        print("[*] Desligando o servidor principal...")
        break

    # Fecha o socket principal do servidor, liberando a porta
    servidor.close()

if __name__ == "__main__":
    iniciar_servidor()