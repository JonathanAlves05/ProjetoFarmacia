import datetime

class Medicamento:
    def __init__(self, nome, numero_lote, quantidade, validade):
        """
        Inicializa um medicamento.

        Args:
            nome (str): Nome do medicamento.
            numero_lote (str): Número do lote.
            quantidade (int): Quantidade disponível.
            validade (datetime.date): Data de validade.
        """
        self.nome = nome
        self.numero_lote = numero_lote
        self.quantidade = quantidade
        self.validade = validade

    def __repr__(self):
        """
        Retorna uma representação em string do medicamento.

        Returns:
            str: Representação em string.
        """
        return f"{self.nome} (Lote: {self.numero_lote}) - Quantidade: {self.quantidade} - Validade: {self.validade}"

class Farmacia:
    def __init__(self):
        """
        Inicializa uma farmácia.
        """
        self.estoque = []

    def cadastrar_medicamento(self, nome, numero_lote, quantidade, validade):
        """
        Cadastra um medicamento.

        Args:
            nome (str): Nome do medicamento.
            numero_lote (str): Número do lote.
            quantidade (int): Quantidade disponível.
            validade (datetime.date): Data de validade.
        """
        medicamento = Medicamento(nome, numero_lote, quantidade, validade)
        self.estoque.append(medicamento)
        print(f"Medicamento {nome} cadastrado com sucesso!")

    def consultar_estoque(self):
        """
        Consulta o estoque.
        """
        if not self.estoque:
            print("Estoque vazio.")
            return
        print("Medicamentos em estoque:")
        for medicamento in self.estoque:
            print(medicamento)

    def dispensar_medicamento(self, nome, quantidade):
        """
        Dispensa um medicamento.

        Args:
            nome (str): Nome do medicamento.
            quantidade (int): Quantidade a dispensar.
        """
        for medicamento in self.estoque:
            if medicamento.nome == nome and medicamento.quantidade >= quantidade:
                medicamento.quantidade -= quantidade
                print(f"Medicamento {nome} dispensado com sucesso. Quantidade restante: {medicamento.quantidade}")
                return
        print(f"Medicamento {nome} não encontrado ou quantidade insuficiente.")

    def verificar_validade(self):
        """
        Verifica a validade dos medicamentos.
        """
        print("Medicamentos próximos do vencimento:")
        hoje = datetime.date.today()
        for medicamento in self.estoque:
            dias_para_vencer = (medicamento.validade - hoje).days
            if dias_para_vencer <= 30:
                print(f"{medicamento.nome} (Lote: {medicamento.numero_lote}) - Vence em {dias_para_vencer} dias.")

    def remover_vencidos(self):
        """
        Remove os medicamentos vencidos.
        """
        hoje = datetime.date.today()
        self.estoque = [medicamento for medicamento in self.estoque if medicamento.validade > hoje]
        print("Medicamentos vencidos removidos do estoque.")

# Exemplo de uso do programa
if __name__ == "__main__":
    farmacia = Farmacia()

    # Cadastrando medicamentos
    farmacia.cadastrar_medicamento("Paracetamol", "12345", 100, datetime.date(2024, 12, 1))
    farmacia.cadastrar_medicamento("Ibuprofeno", "67890", 50, datetime.date(2024, 11, 15))

    # Consultando estoque
    farmacia.consultar_estoque()

    # Dispensando medicamentos
    farmacia.dispensar_medicamento("Paracetamol", 10)

    # Verificando validade dos medicamentos
    farmacia.verificar_validade()

    # Removendo medicamentos vencidos
    farmacia.remover_vencidos()

    # Consultando estoque atualizado
    farmacia.consultar_estoque()