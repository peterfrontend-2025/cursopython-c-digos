print("Olá humano, responda as seguintes perguntas:\n")
nome = input('Qual é seu nome? ')
idade = int(input('qual a sua idade? '))
peso = float(input('qual é seu peso? '))
# print('Olá', nome, 'sua idade é',idade, 'e seu peso é',peso,'correto?', sep=" ")
#print(f"\nTipo nome: {type(nome)}\nTipo idade: {type(idade)}\nTipo peso: {type(peso)}\n")

print(f"Olá {nome}, sua idade é {idade} e seu peso é {peso}.")

#esta variável estará guadando o valor sim ou não
resposta = input('Correto? ')

#aqui estou dando uma condição para a variável resposta, caso seja verdadeiro, vai "printar" a mensagem correspondente
if resposta == 'sim':
    print('Ótimo, que bom que eu acertei!')

#aqui tabém estou dando uma condição para a variável resposta, porém, com outro resultado caso seja verdadeiro
if resposta == 'não':
    print('Oh não, vamos começar de novo')

#aqui estou falando para a pessoa se decidir e parar de ser pateta :)
if resposta == 'mais ou menos':
    print('ou é sim ou é não, decida :)')