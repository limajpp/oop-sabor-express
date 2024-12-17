from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_teste = Restaurante('Holy Pizza', 'Pizzaria')

bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Paozinho', 2.00, 'O melhor da cidade')
prato_paozinho.aplicar_desconto()

restaurante_teste.adicionar_ao_cardapio([bebida_suco, prato_paozinho])

def main():
    restaurante_teste.exibir_o_cardapio

if __name__ == '__main__':
    main()