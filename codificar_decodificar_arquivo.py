import base64

def main () : 

    opcao = input(str("digite C para codificar ou D para decodificar um arquivo: "))

    if opcao == "C":
        arquivo_a_ser_codificado = input("Digite a frase/palavra que desejas codificar: ")
        nome = input("Digite o nome do arquivo: ")
        codificar_arquivo(arquivo_a_ser_codificado, nome)

    elif opcao == "D": 
        nome_arquivo = input("digite o nome do arquivo para decodificar: ")
        arquivo_a_ser_decodificado = open(nome_arquivo,'r')
        decodificar_arquivo(arquivo_a_ser_decodificado)

def codificar_arquivo(arquivo_a_ser_codificado, nome):
    
    texto_bytes = arquivo_a_ser_codificado.encode('ascii')
    base64_bytes = base64.b64encode(texto_bytes)
    base64_message = base64_bytes.decode('ascii')
    arq = open(nome, "w")
    arq.write(base64_message)
    arq.close()
    return arq

def decodificar_arquivo(arquivo_a_ser_decodificado):

    linha = arquivo_a_ser_decodificado.readline()
    decodificarBytes = base64.b64decode(linha)
    decodificarStr = str(decodificarBytes, "utf-8")
    print(decodificarStr)
    return decodificarStr

if __name__ =='__main__':
    main ()