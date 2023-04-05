# Code by: Júlio de Oliveira
# Just a simple login system using Python
#
# Created in: 03/08/2023

import Tools

# Aqui é guardado o nome de usuários, mas apenas por tempo limitado, usada para verificação.
listNames = []
fileName = "login-basico/Users.txt"

# Função para procurar por um nome que seja idêntico ao nome de usuário e senha cadastrado
def lookforName():
   
   if alltogether in listNames:
      return True


def readFile(name, ret=False):

   for line in open(fileName, "r"):
      listNames.append(line)

      if ret == True:
         return line


if Tools.FileExists(fileName) == False:
   
   Tools.CreateFile(fileName)


def create_account():

   n_user = str(input("Nome de usuário que deseja cadastrar: "))
   n_psswrd = str(input("Senha para o usuário: "))

   # Precisa ser escrito dessa forma, pois desse jeito será jogado todos os dados do arquivo para a lista, para comparar e verificar se estão corretos.
   Tools.WriteFile(fileName, f"{n_user}{n_psswrd}\n")
   print("pronto!")


def login():

   readFile(fileName, "r")

   username = str(input("Nome de usuário: "))
   psswrd = str(input("Senha: "))

   # essa variável precisa ser global para economizar espaço, não precisando declarar "username" e "psswrd" como globais também. A variável "alltogether" junta usuário e senha para que na função "lookforName()" consiga funcionar de maneira mais eficaz. (OBS.: o "\n" foi adicionado pois quando os dados vão para a lista, anteriormente adicionados para a organização e separação dos dados na lista, sendo assim vão também com o "\n", pois estavam atrapalhando a verificação).
   global alltogether
   alltogether = username + psswrd + "\n"

   if lookforName() == True: 
      print("Logado com sucesso!")
      exit()
   else: 
      print("Usuário e/ou senha não cadastrados")

# Loop principal:
while True:

   print("[1] Cadastrar usuário.")
   print("[2] Entrar em uma conta existente.")
   print("[0] Sair")
   npt = int(input("Digite o número da sua escolha: "))

   if npt == 0:
      break

   if npt == 1:
      create_account()

   elif npt == 2:
      login()