#duvida: setup dos dados no listar boa ou não (listars) /// incluir apenas 1 (incluir) /// mais de um telefone em faxineiro ///conferir cada dado incluindo (incluir) /// perguntar o dado pa alterar e encher de if ou ter que reinserir todos os dados (alterar)

#faxineiros -eu
def submenu_faxineiros():
    print("Submenu de faxineiros:")
    print("1. Listar todos faxineiros")
    print("2. Listar um faxineiro")
    print("3. Incluir faxineiro")
    print("4. Alterar faxineiros")
    print("5. Excluir faxineiro")
    print("Escolha uma ação:")
    opção=int(input())
    faxineiros(opção)

def faxineiros(op):
    if op==1:
        listartd_f()
    elif op==2:
        print("Cpf do faxineiro:")
        cpf=input()
        listar_f(cpf)
    elif op==3:
        incluir_f()
    elif op==4:
        print("Cpf do faxineiro: ")
        cpf=input()
        alterar_f(cpf)
    elif op==5:
        print("Cpf do faxineiro: ")
        cpf=input()
        excluir_f(cpf)
    else:
        print("Digite uma opção válida")

def listartd_f():
    FaxineirosDic={'42565796901':['Victor Hugo Zivas','Homem',3393984,'16/09/2006',1499093210],'67765732652':['Leonardo Almeida Quente','Homem', 1243753,'10/02/2007',14996627901],'34155646432':['Pedro Boschetti Chongas','Mulher',2136778, '14/12/2006',14996001179],'65266576523':['Teo Brazola Tolis','Homem',7643423,'23/09/2006',14995632020],'36786543701':['Pedro Peres Penis','Mulher',3231000,'21/04/2007',19059237312]}    
    print("Faxineiros:")
    for i in FaxineirosDic:
        print(f"\t {FaxineirosDic[i][0]}:")
        for j in range(1,len(FaxineirosDic[i])):
            print(f"\t\t {FaxineirosDic[i][j]}")
        print()
        
def listar_f(cpf):
    FaxineirosDic={'42565796901':['Victor Hugo Zivas','Homem',3393984,'16/09/2006',1499093210],'67765732652':['Leonardo Almeida Quente','Homem', 1243753,'10/02/2007',14996627901],'34155646432':['Pedro Boschetti Chongas','Mulher',2136778, '14/12/2006',14996001179],'65266576523':['Teo Brazola Tolis','Homem',7643423,'23/09/2006',14995632020],'36786543701':['Pedro Peres Penis','Mulher',3231000,'21/04/2007',19059237312]}    
    if cpf in FaxineirosDic:
        print(FaxineirosDic[cpf][0],":")
        for i in range(1,len(FaxineirosDic[cpf])):
            print(f"\t {FaxineirosDic[cpf][i]}")
    else:
        print("Cpf inválido: faxineiro inexistente ou cpf incorreto.")
    
def incluir_f():
    FaxineirosDic={'42565796901':['Victor Hugo Zivas','Homem',3393984,'16/09/2006',1499093210],'67765732652':['Leonardo Almeida Quente','Homem', 1243753,'10/02/2007',14996627901],'34155646432':['Pedro Boschetti Chongas','Mulher',2136778, '14/12/2006',14996001179],'65266576523':['Teo Brazola Tolis','Homem',7643423,'23/09/2006',14995632020],'36786543701':['Pedro Peres Penis','Mulher',3231000,'21/04/2007',19059237312]}    
    print("Entre com os dados do faxineiro: ")
    cpf=input("Cpf: ")
    if cpf in FaxineirosDic:
        print("Cpf ja cadastrado.")
    else:
        nome=input("Nome: ")
        sexo=input("Sexo: ")
        rg=int(input("RG: "))
        data=input("Data de nascimento: ")
        num=int(input("Numero de contato: "))
        FaxineirosDic[cpf]=[nome,sexo,rg,data,num]
        if cpf in FaxineirosDic:
            print("Faxineiro incluído com sucesso.")
        else:
            print("Erro no cadastro do faxineiro.")

def alterar_f(cpf):
    FaxineirosDic={'42565796901':['Victor Hugo Zivas','Homem',3393984,'16/09/2006',1499093210],'67765732652':['Leonardo Almeida Quente','Homem', 1243753,'10/02/2007',14996627901],'34155646432':['Pedro Boschetti Chongas','Mulher',2136778, '14/12/2006',14996001179],'65266576523':['Teo Brazola Tolis','Homem',7643423,'23/09/2006',14995632020],'36786543701':['Pedro Peres Penis','Mulher',3231000,'21/04/2007',19059237312]}    
    if cpf in FaxineirosDic:
        print("Insira os dados novos: ")
        nome=input("Nome: ")
        sexo=input("Sexo: ")
        rg=int(input("RG: "))
        data=input("Data de nascimento: ")
        num=int(input("Numero de contato: "))
        FaxineirosDic[cpf]=[nome,sexo,rg,data,num]
        print("Alteração concluída.")
    else:
        print("Cpf não encontrado.")

def excluir_f(cpf):
    FaxineirosDic={'42565796901':['Victor Hugo Zivas','Homem',3393984,'16/09/2006',1499093210],'67765732652':['Leonardo Almeida Quente','Homem', 1243753,'10/02/2007',14996627901],'34155646432':['Pedro Boschetti Chongas','Mulher',2136778, '14/12/2006',14996001179],'65266576523':['Teo Brazola Tolis','Homem',7643423,'23/09/2006',14995632020],'36786543701':['Pedro Peres Penis','Mulher',3231000,'21/04/2007',19059237312]}    
    if cpf in FaxineirosDic:
        del FaxineirosDic[cpf]
        print("Remoção concluída.")
    else:
        print("Cpf não encontrado.")

#cliente -moita
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

#serviços -moita
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

#relatorios - eu

#main/menu
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