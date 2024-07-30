# script.py
def main():
    mensagem = "esse é o trabalho da gabi e do gabriel!"
    
    # Escrever mensagem em um arquivo
    with open("mensagem.txt", "w") as f:
        f.write(mensagem)
    
    # Imprimir mensagem no console
    print(mensagem)

if __name__ == "__main__":
    main()
