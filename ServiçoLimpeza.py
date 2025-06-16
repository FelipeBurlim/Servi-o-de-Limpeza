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

def carregar_dados_faxineiros(nome_arq):
    FaxineirosDic = {}
    if existe_arq(nome_arq):
        arq=open(nome_arq, "r")
        for linha in arq:
            linha = linha.replace("\n", " ")
            linha = linha.split(";")
            FaxineirosDic[linha[0]]=[]
            FaxineirosDic[linha[0]].append(linha[1])
            FaxineirosDic[linha[0]].append(linha[2])
            FaxineirosDic[linha[0]].append(linha[3])
            FaxineirosDic[linha[0]].append(linha[4])
            FaxineirosDic[linha[0]].append(linha[5])
    else:
            print("Arquivo não encontrado! ")
    arq.close()
    return FaxineirosDic

def faxineiros(op):
    nome_arq="./faxineiros.txt"
    FaxineirosDic=carregar_dados_faxineiros(nome_arq)
    if op==1:
        listartd_f(FaxineirosDic)
    elif op==2:
        print("Cpf do faxineiro:")
        cpf=input()
        listar_f(FaxineirosDic,cpf)
    elif op==3:
        incluir_f(FaxineirosDic)
    elif op==4:
        print("Cpf do faxineiro: ")
        cpf=input()
        alterar_f(FaxineirosDic,cpf)
    elif op==5:
        print("Cpf do faxineiro: ")
        cpf=input()
        excluir_f(FaxineirosDic,cpf)
    else:
        print("Digite uma opção válida")

def listartd_f(dic):
    print("Faxineiros:")
    for i in dic:
        print(f"\t {dic[i][0]}:")
        for j in range(1,len(dic[i])):
            print(f"\t\t {dic[i][j]}")
        print()
        
def listar_f(dic,cpf):
    if cpf in dic:
        print(dic[cpf][0],":")
        for i in range(1,len(dic[cpf])):
            print(f"\t {dic[cpf][i]}")
    else:
        print("Cpf inválido: faxineiro inexistente ou cpf incorreto.")
    
def incluir_f(dic):
    print("Entre com os dados do faxineiro: ")
    cpf=input("Cpf: ")
    if cpf in dic:
        print("Cpf ja cadastrado.")
    else:
        nome=input("Nome: ")
        sexo=input("Sexo: ")
        rg=int(input("RG: "))
        data=input("Data de nascimento: ")
        num=int(input("Numero de contato: "))
        dic[cpf]=[nome,sexo,rg,data,num]
        if cpf in dic:
            print("Faxineiro incluído com sucesso.")
        else:
            print("Erro no cadastro do faxineiro.")

def alterar_f(dic,cpf):
    if cpf in dic:
        print("Insira os dados novos: ")
        nome=input("Nome: ")
        sexo=input("Sexo: ")
        rg=int(input("RG: "))
        data=input("Data de nascimento: ")
        num=int(input("Numero de contato: "))
        dic[cpf]=[nome,sexo,rg,data,num]
        print("Alteração concluída.")
    else:
        print("Cpf não encontrado.")

def excluir_f(dic,cpf):
    if cpf in dic:
        del dic[cpf]
        print("Remoção concluída.")
    else:
        print("Cpf não encontrado.")

#cliente -moita
def carregar_dados_clientes(nome_arq):
    dicio_clientes = {}
    if existe_arq(nome_arq):
        arq=open(nome_arq, "r")
        for linha in arq:
            linha = linha.replace("\n", " ")
            linha = linha.split(";")
            dicio_clientes[linha[0]]=[]
            dicio_clientes[linha[0]].append(linha[1])
            dicio_clientes[linha[0]].append(linha[2])
            dicio_clientes[linha[0]].append(linha[3])
            dicio_clientes[linha[0]].append(linha[4])
            dicio_clientes[linha[0]].append(linha[5])
            dicio_clientes[linha[0]].append(linha[6])
            dicio_clientes[linha[0]].append(linha[7])
    else:
            print("Arquivo não encontrado! ")
    arq.close()
    return dicio_clientes

def submenu_clientes():
    print("Submenu de clientes:")
    print("1. Listar todos clientes")
    print("2. Listar um cliente")
    print("3. Incluir cliente")
    print("4. Alterar clientes")
    print("5. Excluir cliente")
    print("Escolha uma ação:")
    opção=int(input())
    return opção

def clientes():
    nome_arq = "./clientes.txt"
    clientes= carregar_dados_clientes(nome_arq)
    op=submenu_clientes()
    if op ==1:
        listar_clientes(clientes)
    elif op ==2:
        cpf=input("Insira o CPF do cliente : ")
        listar_1cliente(cpf,clientes)
        if listar_1cliente:
            print("Aqui estão os dados do cliente!")
        else:
            print("CPF não cadastrado!")
    elif op ==3:
        print("Cadastrando novo cliente... ")
        cpf = input(" Inisira seu CPF: ")
        add_cliente(cpf,clientes)
    elif op==4:
        cpf = input(" Inisira o CPF do cliente que deseja alterar os dados : ")
        alterar_cliente(cpf,clientes)
    elif op == 5:
        cpf = input(" Inisira o CPF do cliente que deseja excluir : ")
        excl_cliente(cpf,clientes)
        
def listar_clientes(ClientesDic):
    for cpf, info in ClientesDic.items():
        print(f"{cpf}")
        for j in info:
            print(j)
        print("----------------------------------------------------------")

def listar_1cliente(cpf,clientes):
    ClientesDic= clientes
    if cpf in ClientesDic:
        for i in range(len(ClientesDic[cpf])):
            print(ClientesDic[cpf][i])
        return True
    else:
        return False
    
def add_cliente(cpf,dicio):
    ClientesDic= dicio
    if cpf in ClientesDic:
        print("Cpf ja cadastrado.")
    else:
        nome=input("Insira seu nome : ")
        dn=input("Insira sua data de nascimento : ")
        end=input("Insira seu endereço : ")
        cep=input("Insira seu CEP : ")
        cidade=input("Insira sua cidade : ")
        email=input("Insira seu e-mail : ")
        tel=input("Insira seu telefone : ")
        ClientesDic[cpf]=[nome,dn,end,cidade,email,tel]
        grava_dados(ClientesDic, "./clientes.txt")

def alterar_cliente(cpf,dicio):
    ClientesDic= dicio
    if cpf in ClientesDic:
        print("Insira os novos dados do cliente : ")
        nome=input("Insira seu nome : ")
        dn=input("Insira sua data de nascimento : ")
        end=input("Insira seu endereço : ")
        cep=input("Insira seu CEP : ")
        cidade=input("Insira sua cidade : ")
        email=input("Insira seu e-mail : ")
        tel=input("Insira seu telefone : ")
        ClientesDic[cpf]=[nome,dn,end,cep,cidade,email,tel]
        grava_dados(ClientesDic, "./clientes.txt")
        print("Alteração concluida!")
        
    else:
        print("CPF não registrado!")

def excl_cliente(cpf,dicio):
    ClientesDic= dicio
    if cpf in ClientesDic:
        del ClientesDic[cpf]
        grava_dados(ClientesDic, "./clientes.txt")
        print(ClientesDic)
        print("Remoção concluida com sucesso!")
    else:
        print("CPF não registrado!")  

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
    print()

#relatorios - eu

#main/menu

def existe_arq(nome_arq):
    import os
    if os.path.exists(nome_arq):
        return True
    else:
        return False
    

def grava_dados(dicio,nome_arq):
    arq = open(nome_arq, "w")
    for cpf in dicio:
        arq.write(cpf + ";")
        for i in range(len(dicio[cpf])):
            arq.write(dicio[cpf][i]+ ";")
        arq.write("\n")
    arq.close()
    
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
            clientes()
        elif op==3:
            submenu_serviços()        
        elif op==4:
            print()
            # submenu_relatórios()
        elif op==5:
            print("Encerrando programa...")
        else:
            print("Digite uma opção válida!")

main()
