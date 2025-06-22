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
    grava_dados(FaxineirosDic,"./faxineiros.txt")

def listartd_f(dic):
    print("Faxineiros:")
    for i in dic:
        print("Cpf:",i)
        listar_f(dic,i)
        print()
        
def listar_f(dic,cpf):
    dados=['Nome:','Sexo:','RG:','Data de nascimento:','Telefones:']
    if cpf in dic:
        for i in range(len(dic[cpf])):
            print(f"\t {dados[i]} {dic[cpf][i]}")
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
    else:
        print("Digite uma opção válida.")
    grava_dados(clientes, "./clientes.txt")
        
def listar_clientes(ClientesDic):
    for cpf, info in ClientesDic.items():
        print(f"{cpf}")
        for j in info:
            print(j)
        print()

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
        ClientesDic[cpf]=[nome,dn,end,cep,cidade,email,tel]

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
        print("Alteração concluida!")
        
    else:
        print("CPF não registrado!")

def excl_cliente(cpf,dicio):
    ClientesDic= dicio
    if cpf in ClientesDic:
        del ClientesDic[cpf]
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
    print("Escolha uma ação:")
    opção=int(input())
    serviços(opção)

def carregar_dados_servico(nome_arq):
    dicio_servicos = {}
    if existe_arq(nome_arq):
        arq=open(nome_arq, "r")
        for linha in arq:
            linha = linha.replace("\n", " ")
            linha = linha.split(";")
            dicio_servicos[linha[0],linha[1],linha[2]] = []
            linha[3] = linha[3].strip()
            dicio_servicos[linha[0],linha[1],linha[2]].append(linha[3])
        arq.close()
    else:
        print("Arquivo não encontrado! ")
    return dicio_servicos

def grava_dados_sevico(dicio,nome_arq):
    arq = open(nome_arq, "w")
    for chave in dicio:
        arq.write(f"{chave[0]};{chave[1]};{chave[2]};{dicio[chave][0]}\n")
    arq.close()

def listar_servicos(servicos):
    for chave, valor in servicos.items():
        print(f"{chave[0]} - {chave[1]} - {chave[2]}: {valor[0]}")
        print()

def listar_1servico(servicos):
    cpffax = input("Insira o cpf do prestador de serviço: ")
    cpfcliente = input("Insira o cpf do cliente: ")
    data= input("Insira a data do serviço (dd/mm/aaaa): ")
    chave = (cpffax, cpfcliente, data)
    if chave in servicos:
        print(f"Serviço encontrado: {chave[0]} - {chave[1]} - {chave[2]}: {servicos[chave][0]}")
    else:
        print("Serviço não encontrado.")

def incluir_servico(servicos):
    cpffax = input("Insira o cpf do prestador de serviço: ")
    cpfcliente = input("Insira o cpf do cliente: ")
    data = input("Insira a data do serviço (dd/mm/aaaa): ")
    preço= input("Insira a preço do serviço: ")
    chave = (cpffax, cpfcliente, data)
    if chave not in servicos:
        servicos[chave] = [preço]
        print("Serviço incluído com sucesso!")
    else:
        print("Serviço já existe.")

def alterar_servico(servicos):
    cpffax = input("Insira o cpf do prestador de serviço: ")
    cpfcliente = input("Insira o cpf do cliente: ")
    data = input("Insira a data do serviço (dd/mm/aaaa): ")
    chave = (cpffax, cpfcliente, data)
    if chave in servicos:
        novo_preco = input("Insira o novo preço do serviço: ")
        servicos[chave] = [novo_preco]
        print("Serviço alterado com sucesso!")
    else:
        print("Serviço não encontrado.")

def excluir_servico(servicos):
    cpffax = input("Insira o cpf do prestador de serviço: ")
    cpfcliente = input("Insira o cpf do cliente: ")
    data = input("Insira a data do serviço (dd/mm/aaaa): ")
    chave = (cpffax, cpfcliente, data)
    if chave in servicos:
        del servicos[chave]
        print("Serviço excluído com sucesso!")
    else:
        print("Serviço não encontrado.")

def serviços(op):
    nome_arq = "./servicos.txt"
    servicos = carregar_dados_servico(nome_arq) 
    if op == 1:
        print("Listando todos os serviços...")
        listar_servicos(servicos)
    elif op == 2:
        print("Listando um serviço específico...")
        listar_1servico(servicos)
    elif op == 3:
        print("Incluindo um novo serviço...")
        incluir_servico(servicos)
    elif op == 4:
        print("Alterando serviços...")
        alterar_servico(servicos)
    elif op == 5:
        print("Excluindo um serviço...")
        excluir_servico(servicos)
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
    grava_dados_sevico(servicos, "./servicos.txt")  

#relatorios - eu

def submenu_relatorios():
    print("Submenu de relatórios:")
    print("1. Relatório de clientes de determinado faxineiro")
    print("2. Relatório de serviços em determinado dia")
    print("3. Relatório de determinado faxineiro")
    print("Escolha uma ação:")
    opção=int(input())
    relatorios(opção)

def relatorios(op):
    if op==1:
        print("Cpf do faxineiro:")
        cpf=input()
        print("Data inicial:") 
        data_ini=input()
        print("Data final:") 
        data_fin=input()
        relatorio_faxineiro_cliente(cpf,data_ini,data_fin)
    elif op==2:
        print("Digite a data:")
        data=input()
        relatorio_dia(data)
    elif op==3:
        print("Cpf do faxineiro:")
        cpf=input()
        relatorio_faxineiro(cpf)
    else:
        print("Opção inválida.")

def relatorio_faxineiro(cpf):
    if existe_arq("./servicos.txt"):
        arq=open("./servicos.txt","r")
        for linha in arq:
            linha = linha.replace("\n", " ")
            linha = linha.split(";")
            if linha[0]==cpf:
                print(f"Cliente: {linha[1]} , data: {linha[2]} e valor: {linha[3]}")
        arq.close()

def relatorio_dia(data):
    faxcliente=carregar_faxcliente_data(data)
    clientes=carregar_dados_clientes("./clientes.txt")
    faxineiros=carregar_dados_faxineiros('./faxineiros.txt')
    for i in range(len(faxcliente[0])):
        print(f"Serviço {i+1}: {faxineiros[faxcliente[0][i]][0]} e {clientes[faxcliente[1][i]][0]}")
    
def carregar_faxcliente_data(data):
    faxcleinte=[[],[]]
    if existe_arq("./servicos.txt"):
        arq=open("./servicos.txt", "r")
        for linha in arq:
            linha = linha.replace("\n", " ")
            linha = linha.split(";")
            if linha[2]==data:
                faxcleinte[0].append(linha[0])
                faxcleinte[1].append(linha[1])
        arq.close()
    return faxcleinte

def relatorio_faxineiro_cliente(cpf,d_ini,d_fin):
    nome_arq = "./servicos.txt"
    clientes=carregar_cpf_cliente(nome_arq,d_ini,d_fin,cpf)
    if len(clientes)>0:
        dic_clientes=carregar_dados_clientes("./clientes.txt")
        for i in clientes:
            for j in dic_clientes:
                if i==j:
                    print("Cliente: ", dic_clientes[j][0])
                    print("\t email(s): ")
                    for k in dic_clientes[j][5]:
                        print("\t\t",k,)
                    print()
                    print("\t numero(s): ")
                    for k in dic_clientes[j][-1]:
                        print("\t\t",k,)
                    print()
    else:
        print("Nenhum serviço feito por tal faxineiro")


def carregar_cpf_cliente(nome_arq,d_ini,d_fin,cpf):
    clientes=[]
    if existe_arq(nome_arq):
        arq=open(nome_arq, "r")
        d_ini=d_ini.split("/")
        d_fin=d_fin.split("/")
        for i in range(len(d_ini)):
             d_ini[i]=int(d_ini[i])
             d_fin[i]=int(d_fin[i])
        for linha in arq:
            linha = linha.replace("\n", " ")
            linha = linha.split(";")
            del linha[-1]
            if linha[0]==cpf:
                linha[2]=linha[2].split("/")
                for i in range(len(linha[2])):
                    linha[2][i]=int(linha[2][i])
                if linha[2][2]<d_fin[2] and linha[2][2]>d_ini[2]:
                    clientes.append(linha[1])
                elif linha[2][2]<=d_fin[2] and linha[2][2]>=d_ini[2]:
                    if linha[2][1]<d_fin[1] and linha[2][1]>d_ini[1]:
                            clientes.append(linha[1])
                    elif linha[2][1]<=d_fin[1] and linha[2][1]>=d_ini[1]:
                        if linha[2][0]<=d_fin[0] and linha[2][0]>=d_ini[0]:
                            clientes.append(linha[1])
        arq.close() 
    else:
        print("Nenhum serviço encontrado!")
    return clientes

#main/menu
def grava_dados(dicio,nome_arq):
    arq = open(nome_arq, "w")
    for cpf in dicio:
        arq.write(cpf + ";")
        for i in range(len(dicio[cpf])):
            arq.write(dicio[cpf][i]+ ";")
            arq.write("\n")
    arq.close()

def existe_arq(nome_arq):
    import os
    if os.path.exists(nome_arq):
        return True
    else:
        return False
    
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
            submenu_relatorios()
        elif op==5:
            print("Encerrando programa...")
        else:
            print("Digite uma opção válida!")

main()
