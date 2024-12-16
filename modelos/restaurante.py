class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self._nome} || Categoria: {self._categoria}'

    def alternar_status(self):
        self._ativo = not self._ativo

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome:'.ljust(25)} || {'Categoria:'.ljust(25)} || {'Status:'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} || {restaurante._categoria.ljust(25)} || {restaurante.ativo.ljust(25)}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo == True else 'Inativo'

restaurante_teste = Restaurante('Holy Pizza', 'Pizzaria')
restaurante_exemplo = Restaurante('Kina', 'Comida Nordestina')
restaurante_teste.alternar_status()
Restaurante.listar_restaurantes()
