# Idade_Alvo = 65
# Minha_idade = 18
#
# print("Formatando idade alvo {}".format(Idade_Alvo))
#
# print(f"Segunda forma {Idade_Alvo}")
#
# print("Terceira forma {i}, outro exemplo {n}".format(i=Idade_Alvo, n=Minha_idade))

# outros tipos de casting

idade_usuario = int(input("Digite a idade do usuário: "))
idade_pessoa = int(input("Digite a idade da pessoa: "))
nome_usuario = input("Digite o nome do usuário: ")
nome_pessoa = input("Digite o nome da pessoa: ")

diferenca_idade = idade_usuario - idade_pessoa
media_idade = (idade_usuario + idade_pessoa) / 2
usuario_maior_pessoa = idade_usuario > idade_pessoa


print(f"Nome do usuário: {nome_usuario} \nNome da pessoa: {nome_pessoa}")
print(f"A diferença de idade é: {diferenca_idade} \n"
      f"A média de idade é {media_idade} \n"
      f"O usuário é mais velho que a pessoa: {usuario_maior_pessoa}")
