parar_programa = False

while parar_programa == False:
    tipo_entrada_dos_dados = int(input("Escolha o número que representa o tipo de entrada de dados:"
                                       "\n1- App Porto"
                                       "\n2- WhatsApp"
                                       "\n3- Telefone"))

    # Variáveis sobre problema e características do veiculo
    tipo_problema = input("Qual o problema ocorrido? (ex: problema na bateria, veiculo está cheirando queimado...)")

    veiculo_classificacao = input("Digite a classificação do veículo (caminhao, onibus...): ")
    veiculo_marca = input("Digite a marca do veículo: ")
    veiculo_modelo = input("Digite o modelo do veículo: ")
    veiculo_peso = float(input("Digite o peso do veículo em Kg: "))
    veiculo_altura = float(input("Digite a altura do veículo em metros: "))
    veiculo_comprimento = float(input("Digite o comprimento do veículo em metros: "))
    veiculo_carga_adicional = float(input("Digite em kg a carga adicional que o veículo está levando (se não houver: 0): "))



    parar_programa = True