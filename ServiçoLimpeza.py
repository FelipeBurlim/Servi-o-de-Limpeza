def submenu_faxineiros():
    print("Submenu de faxineiros:")
    print("1. Listar todos faxineiros")
    print("2. Listar um faxineiro")
    print("3. Incluir faxineiro")
    print("4. Alterar faxineiros")
    print("5. Excluir faxineiro")
    opção=input()
    faxineiros(opção)

def faxineiros(op):
    #igualmain

def submenu_clientes():
    print("Submenu de clientes:")
    print("1. Listar todos clientes")
    print("2. Listar um cliente")
    print("3. Incluir cliente")
    print("4. Alterar clientes")
    print("5. Excluir cliente")
    opção=input()
    clientes(opção)

def clientes(op):
    #igualmain

def submenu_serviços():
    print("Submenu de serviços:")
    print("1. Listar todos serviços")
    print("2. Listar um serviço")
    print("3. Incluir serviço")
    print("4. Alterar serviços")
    print("5. Excluir serviço")
    opção=input()
    serviços(opção)

def serviços(op):
    #igualmain


def menu():
    print("Menu Principal:")
    print("1. Submenu de Faxineiros")
    print("2. Submenu de Clientes")
    print("3. Submenu de Serviços")
    print("4. Submenu Relatórios")
    print("5. Sair")
    opção=int(input())
    return opção


def main():
    op=1
    while op!=5:
        op=menu()
        if op==1:
            submenu_faxineiros()
        elif op==2:
            submenu_clientes()
        elif op==3:
            submenu_serviços()        
        elif op==4:
            #relatorios
        else:
            print("Digite uma opção válida!")

main()