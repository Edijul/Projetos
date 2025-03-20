class Despesa:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor

    def __str__(self):
        return f"{self.descricao}: R${self.valor:.2f}"

class GerenciadorDespesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesa(self, descricao, valor):
        despesa = Despesa(descricao, valor)
        self.despesas.append(despesa)
        print(f"Despesa '{descricao}' de R${valor:.2f} adicionada com sucesso!")

    def listar_despesas(self):
        if not self.despesas:
            print("Nenhuma despesa registrada.")
        else:
            print("Lista de Despesas:")
            for despesa in self.despesas:
                print(despesa)

    def total_gasto(self):
        total = sum(despesa.valor for despesa in self.despesas)
        print(f"Total gasto: R${total:.2f}")

def main():
    gerenciador = GerenciadorDespesas()

    while True:
        print("\n--- Gerenciador de Despesas ---")
        print("1. Adicionar Despesa")
        print("2. Listar Despesas")
        print("3. Calcular Total Gasto")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição da despesa: ")
            valor = float(input("Digite o valor da despesa: "))
            gerenciador.adicionar_despesa(descricao, valor)
        elif opcao == "2":
            gerenciador.listar_despesas()
        elif opcao == "3":
            gerenciador.total_gasto()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()