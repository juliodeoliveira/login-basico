def CreateFile(name):
    '''
        CreateFile é uma função que cria arquivos independentemente do seu formato.
        ~ name : recebe o nome do arquivo que deseja criar (com extensão).
    '''
    try:
        n = open(name, "wt+")
        n.close()
    except:
        print("Something just failed")


def FileExists(name):
    '''
        FileExists é uma função que verifica se um determinado arquivo existe.
        ~name : recebe o nome do arquivo a ser verificado (com extensão).
        Retorna: True - para arquivo encontrado; False - para arquivo não encontrado
    '''

    try:
        n = open(name, "rt")
        
    except FileNotFoundError:
        return False

    else:
        return True

def WriteFile(file_name, write):
    '''
        WriteFile é uma função que escreve qualquer texto que desejar em um determinado aquivo.
        ~file_name : recebe o nome do arquivo que deseja escrever/adicionar um texto.
        ~write : recebe o texto que deseja escrever no arquivo.
    '''

    try:
        n = open(file_name, "a")
    except:
        print("An error occoured.")
    else:
        try:
            n.write(write)
        except:
            print("Error when I try to write in archive")
        

def ReadFile(name):
    '''
        ReadFile é uma função que lê e te mostra o texto dentro de determinado arquivo
        ~name : recebe o nome do arquivo que deseja ler.
        Retorna : Cada linha de texto inserida dentro do arquivo.
    '''

    try:
        n = open(name, "r")
    except:
        print("A error occoured when I try to open the file.")

    else:
        for line in n:
            return line

