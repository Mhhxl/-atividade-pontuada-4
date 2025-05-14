import os
os.system('cls || clear')
import time
from dataclasses import dataclass
import csv

#criando lista
lista_funcionarios= []

#funções
def limpar_terminal():
    os.system('cls || clear')


#Classe de funcionarios@dataclass
class funcionario:
    nome: str
    cargo: str
    salario: str



#CRUD
def verificar_lista_vazia(lista_funcionarios):
    if not lista_funcionarios:
        return True
    return False



def adicionar_funcionario(lista_funcionarios):
    limpar_terminal()
    print("Carregando...")
    time.sleep(2)
    limpar_terminal()
    nome= input("Digite o seu nome: ")
    cargo= input("Digite o cargo que ocupa na empresa: ")
    salario= input("Digite o seu salário: ")

    limpar_terminal()
    print("Adicionando Funcionario...")
    Funcionarios= funcionario(nome, cargo, salario)
    lista_funcionarios.append(funcionario)
    print(f"Funcionario '{nome}' Adicionado com sucesso! ")




def listar_funcionarios(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        print("A lista de funcionarios está vazia! Adicione um funcionario antes de listar.")
        return
    

    limpar_terminal()
    print("Carregando...")
    time.sleep(2)
    limpar_terminal(2)
    print("\n= Lista de Funcionarios =")


    for funcionario in lista_funcionarios:
        print(f"""
            Nome= {funcionario.nome}
            Cargo= {funcionario.cargo}
            Salario= {funcionario.salario}""")
        print("--------------------------------------------------------------------")

def atualizar_funcionarios(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        print("A lista de funcionarios está vazia! Adicione um funcionario antes de atualizar.")
        return
    
    limpar_terminal()
    print("Carregando....")
    time.sleep(2)
    limpar_terminal()
    listar_funcionarios(lista_funcionarios)
    nome_antigo= input("Digite o nome do funcionario que  deseja atualizar:")
    cargo_antigo= input("Digite o cargo do funcionario que deseja atualizar: ")
    salario_antigo= input("Digite o salario do funcionario que deseja atualizar")

    limpar_terminal()
    print("Atualizando Funcionarios...")
    time.sleep(2)
    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_antigo and funcionario.cargo == cargo_antigo and funcionario.salario == salario_antigo:
            print("Funcionario encontrado! ")
            print("Digite os novos dados do funcionario: ")

            novo_nome= input("Digite o novo nome: ")
            novo_cargo= input("Digite o novo cargo: ")
            novo_salario= input("Digite o novo salario: ")

            funcionario.nome= novo_nome
            funcionario.cargo= novo_cargo
            funcionario.salario= novo_salario

            print("Atualizando Dados....")
            time.sleep(2)
            print("Dados atualizados com sucesso! ")
            return
        else:
            print(f"Funcionario '{nome_antigo}' não encontrado na lista.")



def excluir_funcionario(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        print("A lista de funcionarios estpa vazia! Adicione um funcionario antes de excluir.")
        return
    
    limpar_terminal()
    print("Carregando...\n")
    limpar_terminal()
    listar_funcionarios(lista_funcionarios)
    nome_remover= input("Digite o nome que deseja excluir: ")
    cargo_remover= input("Digite o cargo que dejesa excluir: ")
    salario_remover= input("Digite o salario que deseja excluir: ")


    limpar_terminal()
    print("Removendo Funcionario...")
    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_remover and funcionario.cargo == cargo_remover and funcionario.salario == salario_remover:
            lista_funcionarios.remove(funcionario)
            print(f"As informações do funcionario '{nome_remover}' foram excluídas com sucesso! ")
            return
        else:
            print(f"Funcionario '{nome_remover}' não encontrado na lista.")

def main():
    limpar_terminal()
    while True:
        print("===Seja Bem Vindo ao Sistema de Funcionarios====")
        print()
        print("-=<Menu principal<=-")
        menu=int(input("""
    1- Adicionar Funcionario 
    2- Listar Funcionarios
    3- Atualizar Funcionarios
    4- Remover Funcionarios
    5- Sair
    
    Digite a opção desejada: """))

        match menu:
            case 1:
                adicionar_funcionario(lista_funcionarios)
            case 2:
                listar_funcionarios(lista_funcionarios)
            case 3:
                atualizar_funcionarios(lista_funcionarios)
            case 4:
                excluir_funcionario(lista_funcionarios)
            case 5:
                print("Saindo do programa...")
                time.sleep(1)
                limpar_terminal()
                return
            case _:
                print("Opção inválida! Tente novamente.")
                time.sleep(2)
                limpar_terminal()
if __name__ == "__main__":
    main()



