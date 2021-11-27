import replit
#- - - 
#   MENU DE OPÇÔES
#- - - 
def menu():
 print(30* "=")
 print("AVALIAÇÂO")
 print(30* "=")

 print("1. PERCORRER PALAVRA")
 print("2. JOGO DA QUINA")
 print("9. FINALIZAR PROGRAMA")

 escolha = int(input("\nSelecione a opção: "))

 return(escolha)
def jogoquina():
 import random
 quina1 = []
 while len(quina1) < 5:
    x = random.randint (1, 60)
    if x not in quina1: #não repete os n. sorteados
        quina1.append(x)
 quina1.sort() #sort coloca em ordem crescente
 print ('Aposta:')
 print (quina1)
 print()
 quina2 = []
 while len(quina2) < 5:
    x = random.randint (1, 60)
    if x not in quina2: 
        quina2.append(x)
 quina2.sort() 
 print ('Resultado:')
 print (quina2)
 print()
opcao = 0
enter =""
while opcao != 9:
  

  opcao = menu()

  if(opcao == 1):
   print("Opção 1 -PERCORRER A PALAVRA")
   palavra()

  elif(opcao == 2):
   print("JOGO DA QUINA")
   jogoquina()
   
  else:
   print("OPÇÃO INVÁLIDA")
   enter = input("\nPressione ENTER para prosseguir!")