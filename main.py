#!/usr/bin/env python3
from agenda import *

def procurar(ag):
    for i in range(3):
        nome = str(input("Digite o Nome do contato: "))
        if ag.info_do_contato(nome):
            break
        if i == 2:
            exit(1)
    return nome

start()
arquivo="agenda.csv"
opt = int(input("Digite a opção desejada: "))
ag=Agenda(arquivo)

if opt == 1:
    ag.get_agenda()
    exit(1)
elif opt == 2:
    nome = str(input("Nome: "))
    idade = str(input("Idade: "))
    while True:
        sexo = str(input("Sexo (M ou F): ")).upper()
        if sexo == "M" or sexo == "F":
            break
        else:
            print("Sexo inválido!")
    while True:
        cpf = str(input("CPF: "))
        if len(cpf) == 11:
            break
        else:
            print("CPF inválido!")
    tel = str(input("Telefone: "))
    email = str(input("E-mail: "))
    ag=Agenda(arquivo,nome,idade,sexo,cpf,tel,email)
    ag.cadastro()
elif opt ==3:
    delete=str(input("Digite o nome do Contato que deseja remover:"))
    ag.excluir_contato(delete)
    ag.get_agenda()
elif opt == 4:
    nome=procurar(ag)
    print(edit)
    opt_edit = int(input("Digite a opcao para editar o contato: "))
    enumContato = IndexContato(opt_edit)
    if enumContato:
        valor = str(input(f"Digite o novo valor para {enumContato.name}: "))
        ag.editar_contato(nome,enumContato.value,valor)
        ag.get_agenda()
    else:
        print("Opção inválida!")
elif opt == 5:
    procurar(ag)
elif opt == 6:
    opt_edit = str(input("Deseja zerar a lista de contatos (S) ou (N)?"))
    if opt_edit == "S":
        ag.limpar_agenda()
    else:
        exit(1)
else:
    print("Opção inválida!")