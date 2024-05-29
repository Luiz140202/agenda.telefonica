class AgendaTelefonica:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print("O contato já existe.")
        else:
            self.contatos[nome] = telefone
            print("Contato adicionado com sucesso.")

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print("Contato removido com sucesso.")
        else:
            print("O contato não foi encontrado.")

    def pesquisar_contato(self, nome):
        if nome in self.contatos:
            print(f"Nome: {nome}, Telefone: {self.contatos[nome]}")
        else:
            print("O contato não foi encontrado.")

    def listar_contatos(self):
        if not self.contatos:
            print("A agenda está vazia.")
        else:
            print("Lista de contatos:")
            for nome, telefone in self.contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")

def menu():
    agenda = AgendaTelefonica()
    while True:
        print("\nMENU DE OPCOES:")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Pesquisar Contato")
        print("4. Listar Contatos")
        print("5. Sair do Programa")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome do contato que deseja adicionar: ")
            telefone = input("Digite o telefone do contato: ")
            agenda.adicionar_contato(nome, telefone)
        elif escolha == "2":
            nome = input("Digite o nome do contato que deseja remover: ")
            agenda.remover_contato(nome)
        elif escolha == "3":
            nome = input("Digite o nome do contato que deseja pesquisar: ")
            agenda.pesquisar_contato(nome)
        elif escolha == "4":
            agenda.listar_contatos()
        elif escolha == "5":
            print("Obrigado por usar a Agenda Telefônica. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

menu()
