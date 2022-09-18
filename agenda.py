import csv
from enum import Enum,auto

class IndexContato(Enum):
    NOME=0
    IDADE=auto()
    SEXO=auto()
    CPF = auto()
    TELEFONE = auto()
    EMAIL = auto()

class Pessoa:
    def __init__(self,nome,idade,sexo,CPF):
        self.__nome=nome
        self.__idade=idade
        self.__sexo=sexo
        self.__CPF = CPF

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_sexo(self):
        return self.__sexo

    def get_CPF(self):
        return self.__CPF

class InfoPessoa:
    def __init__(self,telefone,email):
        self.__telefone = telefone
        self.__email = email

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email
    
class Agenda(Pessoa,InfoPessoa):
    def __init__(self,file,nome=None,idade=None,sexo=None,CPF=None,telefone=None,email=None):
        Pessoa.__init__(self,nome,idade,sexo,CPF)
        InfoPessoa.__init__(self,telefone,email)
        self.__file=file

    def get_agenda(self):
        print("***************   AGENDA  ATULIZADA   ***************")
        with open(self.__file, 'r') as f:
            filezao = csv.reader(f,delimiter=",")
            for i in filezao:
                print(i)

    def cadastro(self):
        data=[self.get_nome(),self.get_idade(),self.get_sexo(),self.get_CPF(),self.get_telefone(),self.get_email()]
        with open(self.__file, 'a',newline='\n') as f:
            write=csv.writer(f)
            write.writerow(data)
        print("Cadastro realizado!")

    def limpar_agenda(self):
        header=["Nome","Idade","Sexo","CPF","Telefone","Email"]
        with open(self.__file, 'w',newline='\n') as f:
            write=csv.writer(f)
            write.writerow(header)
        print("Agenda limpa!")
    
    def __file_to_list(self):
        filezao = csv.reader(open(self.__file))
        return list(filezao)

    def info_do_contato(self,referencia):
        data = self.__file_to_list()
        ret=False
        for line in data:
            if referencia in line:
                print(line)
                ret=True
                break
        if ret == False:
            print("Contato não encontrado!")
        return ret

    def editar_contato(self,contato,index,novo_valor):
        data = self.__file_to_list()
        for line in data:
            if contato in line:
                line[index] = novo_valor
                print("***************   CONTATO  ATULIZADO   ***************")
                print(line)
        self.__reescrever_arquivo(data)             
    
    def excluir_contato(self,name):
        filezao = self.__file_to_list()
        for line in filezao:
            if name in line:
                filezao.remove(line)
                print("Contato Deletado!")
        self.__reescrever_arquivo(filezao)

    def __reescrever_arquivo(self,arquivo):
        with open(self.__file, 'w+',newline='\n') as f:
            write=csv.writer(f)
            write.writerows(arquivo)
        
def start():               
    lbl="""                                      _               ______
            /\                       | |             |___  /                    
           /  \   __ _  ___ _ __   __| | __ _  ___      / / ___   ___ _ __ __ _ 
          / /\ \ / _` |/ _ \ '_ \ / _` |/ _` |/ _ \    / / / _ \ / _ \ '__/ _` |
         / ____ \ (_| |  __/ | | | (_| | (_| | (_) |  / /_| (_) |  __/ | | (_| |
        /_/    \_\__, |\___|_| |_|\__,_|\__,_|\___/  /_____\___/ \___|_|  \__,_|
                  __/ |                                                         
                 |___/                                                          
    """
    opt="""
        1 - Vizulizar Agenda
        2 - Cadastrar Contato
        3 - Deletar Contato
        4 - Editar Contato
        5 - Buscar Contato
        6 - Limpar Agenda
        """
    print(lbl)
    print(opt)

edit="""
            0 - Editar Nome
            1 - Editar Idade
            2 - Editar Sexo
            3 - Editar CPF
            4 - Editar Telefone
            5 - Editar Email
"""
