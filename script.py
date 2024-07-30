# script.py
def main():
    mensagem = "Olá, GitHub Actions!"
    
    # Escrever mensagem em um arquivo
    with open("mensagem.txt", "w") as f:
        f.write(mensagem)
    
    # Imprimir mensagem no console
    print(mensagem)

if __name__ == "__main__":
    main()
