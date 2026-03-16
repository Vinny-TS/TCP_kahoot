import socket

def iniciar_cliente():
    HOST = '127.0.0.1'
    PORTA = 50000

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        cliente.connect((HOST, PORTA))
        print("=== BEM-VINDO AO MINI KAHOOT ===")
        
        nome = input("Digite seu nome de usuário: ")
        cliente.sendall(nome.encode('utf-8'))

        for _ in range(3):
            # 1. Recebe e imprime a questão
            questao = cliente.recv(1024).decode('utf-8')
            print(f"\n{questao}")

            # 2. Coleta e envia a resposta
            resposta = ""
            while resposta not in ['A', 'B', 'C', 'D']:
                resposta = input("Sua resposta (A/B/C/D): ").strip().upper()
                if resposta not in ['A', 'B', 'C', 'D']:
                    print("Por favor, digite apenas A, B, C ou D.")

            cliente.sendall(resposta.encode('utf-8'))

            # 3. NOVO: Recebe e exibe o feedback imediato
            feedback_imediato = cliente.recv(1024).decode('utf-8')
            print(f"\n> {feedback_imediato}")

            # 4. NOVO: Envia um aviso (ACK) para o servidor mandar a próxima pergunta
            cliente.sendall(b"OK")

        # Recebe o relatório final
        resultado_final = cliente.recv(2048).decode('utf-8')
        print(resultado_final)

    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar ao servidor. Verifique se ele está rodando.")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        cliente.close()

if __name__ == "__main__":
    iniciar_cliente()