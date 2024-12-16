class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f'Nome: {self.nome} || Categoria: {self.categoria} || Ativo: {'Sim' if self.ativo == True else 'Não'}'

restaurante_teste = Restaurante('Holy Pizza', 'Pizzaria')
print(restaurante_teste)