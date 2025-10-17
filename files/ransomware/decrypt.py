from cryptography.fernet import Fernet
import os


def carregar_chave():
    """Carrega a chave de criptografia do arquivo 'chave.key'."""
    return open("chave.key", "rb").read()


def descriptografar_arquivo(arquivo, chave):
    """Descriptografa um arquivo usando a chave fornecida."""
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_descriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)


def encontrar_arquivos(diretorio):
    """Encontra e lista todos os arquivos em um diretório."""
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho = os.path.join(raiz, arquivo)
            if arquivo != "ransomware.py" and not arquivo.endswith(".key"):
                lista.append(caminho)
    return lista


def mensagem_decriptacao():
    with open("DECRYPTION_INFO.txt", "w") as f:
        f.write("Seus arquivos foram descriptografados com sucesso! \n")
        f.write("Obrigado por cooperar. \n")


def main():
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")

    for arquivo in arquivos:
        descriptografar_arquivo(arquivo, chave)
    mensagem_decriptacao()
    print("Descriptografia concluída. Todos os arquivos foram restaurados.")


if __name__ == "__main__":
    main()
