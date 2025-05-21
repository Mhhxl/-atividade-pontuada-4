import os
import time
from dataclasses import dataclass

def limpar_terminal():
    # Limpar o terminal
    os.system("cls || clear")

# Criando lista de funcionário
lista_funcionarios = []

@dataclass
class Funcionario:
    nome: str
    cpf: str
    cargo: str
    salario: str
                
    def exibir_dados(self):
        print("Dados registrados com sucesso.")

# Verificando se a lista estiver vazia e fazendo o CRUD
def verificar_lista_vazia(lista_funcionarios):
    if not lista_funcionarios:
        return True
    return False

def cadastrando_funcionario(lista_funcionarios):
    limpar_terminal()
    time.sleep(2)
    nome = input("Digite o nome do(a) funcionário(a): ")    
    cpf = input(f"Digite o CPF do(a) funcionário(a) '{nome}': ")    
    cargo = input(f"Digite o cargo atual de '{nome}': ")    
    salario = (input(f"Digite o salário atual de '{nome}': R$ "))

    funcionario = Funcionario(nome, cpf, cargo, salario)
    lista_funcionarios.append(funcionario)
    print(f"O cadastro de '{nome}' foi concluído com sucesso!")

def listar_funcionarios(lista_funcionarios):
    verificar_lista_vazia(lista_funcionarios)
    
    limpar_terminal()
    print("Carregando lista de funcionários...")
    time.sleep(2)
    limpar_terminal()
    print("== Lista de Funcionários ==")
    for funcionario in lista_funcionarios:
        print(f"""
            Nome: {funcionario.nome}
            CPF: {funcionario.cpf}
            Cargo: {funcionario.cargo}
            Salário: R${funcionario.salario}""")
        print("----------------------------------------------")

def atualizar_funcionarios(lista_funcionarios):
    verificar_lista_vazia(lista_funcionarios)

    limpar_terminal()
    time.sleep(2)
    listar_funcionarios(lista_funcionarios)
    print("-- Atualize os dados do funcionário --\n")
    
    nome_antigo = input("Digite o nome do funcionário que deseja atualizar: ")
    cpf_antigo = input(f"Digite o CPF de '{nome_antigo}': ")
    cargo_antigo = input(f"Digite o cargo de '{nome_antigo}': ")
    salario_antigo = (input(f"Digite o salário de '{nome_antigo}': R$ \n"))

    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_antigo and funcionario.cpf == cpf_antigo:
            funcionario.nome = input("Digite o novo nome do(a) funcionário(a): ") 
            funcionario.cpf = input(f"Digite o novo CPF de '{funcionario.nome}': ") 
            funcionario.cargo = input(f"Digite o novo cargo de '{funcionario.nome}': ") 
            funcionario.salario = input(f"Digite o salário atual de '{funcionario.nome}': R$ ")
            print(f"As informações do funcionário {nome_antigo} foram atualizadas!")
            return
    print(f"As informações de {nome_antigo} não foram encontradas na lista.")

def excluir_dados_funcionario(lista_funcionarios):
    verificar_lista_vazia(lista_funcionarios)

    limpar_terminal()
    time.sleep(2)
    listar_funcionarios(lista_funcionarios)
    print("== Insira os dados do funcionário que deseja excluir ==")

    remover_nome = input("Digite o nome do funcionário que deseja remover: ")
    remover_cpf = input(f"Digite o CPF de '{remover_nome}': ")
    remover_cargo = input(f"Digite o cargo de '{remover_nome}': ")
    remover_salario = (input(f"Digite o salário de '{remover_nome}': R$ "))

    for funcionario in lista_funcionarios:
        if (funcionario.nome == remover_nome and funcionario.cpf == remover_cpf and 
        funcionario.cargo == remover_cargo and funcionario.salario == remover_salario):
            print(f"Funcionário {remover_nome} encontrado!")
            lista_funcionarios.remove(funcionario)
            print(f"O funcionário {remover_nome} foi removido com sucesso!")
            return

# Criando funções para salvar e carregar os dados dos funcionários na lista
def salvar_dados(lista_funcionarios):
    verificar_lista_vazia(lista_funcionarios)
     # Salvando em um arquivo .csv
    nome_arquivo = "funcionarios_dende_tech.csv"
    with open(nome_arquivo, "a") as funcionarios_dende_tech:
        for funcionario in lista_funcionarios:
            funcionarios_dende_tech.write(f"""
        == Funcionário==        
        Nome: {funcionario.nome}
        CPF: {funcionario.cpf}
        Cargo: {funcionario.cargo}
        Salário: R$ {funcionario.salario}\n""")    
            funcionarios_dende_tech.write("--------------------------------------------------\n")

def carregando_dados(lista_funcionarios):
    verificar_lista_vazia(lista_funcionarios)
    # Carregando um arquivo .csv
    nome_arquivo = "funcionarios_dende_tech.csv"
    try:
        with open(nome_arquivo, "r") as funcionarios_dende_tech:
            print(funcionarios_dende_tech.read())
    except FileNotFoundError:
        print("Arquivo não encontrado.") 
        
def main():    
    # Função onde o menu será executado
    limpar_terminal()
    print("Bem vindo a Dendê Tech! Para continuar aperte 'Enter'\n")
    input()
    while True:
        menu = int(input("""
    - Menu da Dendê Tech -
    
    1 - Cadastrar Funcionários
    2 - Listar Funcionários
    3 - Atualizar Dados De Um Funcionário
    4 - Excluir Dados De Um Funcionário
    5 - Salvar Dados Dos Funcionários
    6 - Carregar Dados Salvos Dos Funcionários
    7 - Sair do Menu
                                                     
    Digite a opção que deseja acessar:  """))

        match menu:
            case 1:
                cadastrando_funcionario(lista_funcionarios)
            case 2:
                listar_funcionarios(lista_funcionarios)
                input()
            case 3:         
                atualizar_funcionarios(lista_funcionarios)
            case 4:         
                excluir_dados_funcionario(lista_funcionarios)
            case 5:         
                salvar_dados(lista_funcionarios)
            case 6:
                carregando_dados(lista_funcionarios)
            case 7:
                print("Obrigado por ter acessado o menu da Dendê Tech.")
                break
            case _:
                print("Opção errada. Digite mais uma vez (aperte 'Enter').")
                input()
                limpar_terminal()
        
        time.sleep(2)
        limpar_terminal()

if __name__ == "__main__":
    main()
    