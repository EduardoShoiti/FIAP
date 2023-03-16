# ESTRUTURAS CONDICIONAIS - simples (if) - "se"

# if 1>0:
#     #dentro do if
#     print("1>0")
#     print("blablabla")
#     print("outra linha")
#     contador = 1
#     if 2==0:
#         print(contador)
#         contador+=1
#         print(contador)
#     contador+=1
#     #numero1=input("qualquer coisa")
#     print(contador)
# #estou fora do if

# minha_idade=30
# idade_colega=40
#if aceita composições
# if minha_idade>idade_colega:
#     print("você é mais velho ")
#
# # else = Todo o resto
# else:  #você não escreve condições
#     print("você não é mais velho")

#utilizando apenas if e else, faça um programa que diga
# a diferença de idade entre você e um colega, e seus nomes,
# sem que a resposta seja um número negativo

# seu_nome = input("Diga seu nome: ")
# sua_idade = float(input("Olá,{}\nDiga a sua idade ".format(seu_nome)))
#
#
# nome_do_colega = input("Diga o nome do seu colega: ")
# idade_colega = float(input("Olá {}, amigo de {}\nDiga a idade de um colega ".\
#                      format(nome_do_colega,seu_nome)))
# ## primeira forma de fazer
# diferenca_de_idade=sua_idade-idade_colega
#
# if diferenca_de_idade<0:
#     diferenca_de_idade *= (-1)
#     print(diferenca_de_idade)
# else:
#     print(diferenca_de_idade)
#
# ## segunda forma de fazer
# if sua_idade>idade_colega:
#     print(sua_idade-idade_colega)
# else:
#     print(idade_colega-sua_idade)
#
# ## terceira forma
# if sua_idade-idade_colega>0:
#     print(sua_idade-idade_colega)
# else:
#     print(idade_colega - sua_idade)
#     #ou
#     print((sua_idade-idade_colega)*(-1))
#

#cada else "fecha" um if

# variavel = 2
#
# if variavel==2:
#     variavel+=1
#     print(variavel)
#
# print(variavel)
#
# if variavel==2:
#     variavel+=2
#
# print(variavel)


# Exercício:
#utilizando apenas if e else, faça um programa que peça a idade sua e de um colega e seus respectivos nomes, e diga:
## a diferença de idade entre vocês, chamando pelo nome, sem que a resposta seja um número negativo
## quantas vezes a pessoa mais velha é mais velha que a mais nova, limitando a resposta a 2 casas decimais
## para cada pessoa, diga:
### se ela for maior de idade, há quanto tempo ela fez 18 anos E quanto tempo falta para se aposentar (assumindo que a idade de aposentadoria é 75 anos);
### se ela for menor de idade, quantos anos faltam para ela fazer 18 anos E se ela ainda é criança (menor de 12 anos) ou já é adolescente (maior ou igual a 12 anos)

meu_nome = input("Digite seu nome: ")
minha_idade = int(input("Digite sua idade: "))
colega_nome = input("Digite o nome do colega: ")
colega_idade = int(input("Digite a idade do colega: "))

diferenca_idade = 0
vezes_mais_velha = 0

if minha_idade > colega_idade:
    diferenca_idade = minha_idade - colega_idade
    vezes_mais_velha = minha_idade / colega_idade
if colega_idade > minha_idade:
    diferenca_idade = colega_idade - minha_idade
    vezes_mais_velha = colega_idade / minha_idade

print(f"A diferença de idade entre {meu_nome} e {colega_nome} é de: {diferenca_idade} ano(s)")
print(f"A pessoa mais velha é {vezes_mais_velha:.2f} vezes mais velha")

if minha_idade >= 18:
    print(f"{meu_nome} fez 18 anos à {minha_idade - 18} ano(s). E falta {75 - minha_idade} ano(s) para aposentar")
if colega_idade >= 18:
    print(f"{colega_nome} fez 18 anos à {colega_idade - 18} ano(s). E falta {75 - colega_idade} ano(s) para aposentar")

if minha_idade < 18:
    print(f"Faltam {18 - minha_idade} ano(s) para {meu_nome} fazer 18 anos")
    if minha_idade >= 12:
        print(f"{meu_nome} é adolescente")
    else:
        print(f"{meu_nome} é cirnaça")

if colega_idade < 18:
    print(f"Faltam {18 - colega_idade} ano(s) para {colega_nome} fazer 18 anos")
    if colega_idade >= 12:
        print(f"{colega_nome} é adolescente")
    else:
        print(f"{colega_nome} é cirnaça")