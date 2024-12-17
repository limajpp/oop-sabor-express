from modelos.restaurante import Restaurante

restaurante_teste = Restaurante('Holy Pizza', 'Pizzaria')
restaurante_teste.alternar_status()

restaurante_teste.receber_avaliacao('Gui', 10)
restaurante_teste.receber_avaliacao('Lais', 8)
restaurante_teste.receber_avaliacao('Emy', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()