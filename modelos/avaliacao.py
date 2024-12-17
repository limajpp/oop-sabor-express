class Avaliacao:
    def __init__(self, cliente, nota):
        """
        Inicializa uma instância de avaliação.

        Parâmetros:
        - cliente (str): O nome do cliente.
        - nota (float): A nota atribuída ao restaurante.
        """
        self._cliente = cliente
        self._nota = float(5 if nota >= 5 else 0 if nota <= 0 else nota)