import random
import time

card_pack_original = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J',
                      'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o']
card_pack = []
backCard_pack = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
                 '18',
                 '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
packCards_complete = []
card_pack_mixed = []
qnt_acerto_player1 = 0
qnt_acerto_player2 = 0


# Funcao 1 - laço para embaralhar cartas
def EmbaralharCartas():
    card_pack = card_pack_original.copy()
    tam = len(card_pack)
    for card in range(30):
        num = random.randint(0, len(card_pack) - 1)
        card_pack_mixed.append(card_pack[num])
        card_pack.pop(num)
        tam -= 1


# Funcao 2 - imprime o baralho na tela
def ImprimirBaralho():
    pular_linha = 0
    for lin in range(len(backCard_pack)):
        print(f"| {backCard_pack[lin]} |", end="")

        if pular_linha < 5:
            pular_linha += 1
        else:
            pular_linha = 0
            print()


# Funcao 3 - jogador seleciona sua carta
def EscolherCartas():
    jogada=False
    while

                
    card1 = int(input("Escolha a primeira carta: "))
    if PosicoesCobertas(card1)

    VirarCarta(card1 - 1)
    card2 = int(input("Escolha a segunda carta: "))
    VirarCarta(card2 - 1)

    #return card1 - 1, card2 - 1

    GuardarRodada(backCard_pack[card1 - 1], backCard_pack[card2 - 1])

    VerificarDisponibilidade(card1 - 1, card2 - 1)


def GuardarRodada(card1, card2):
    id_card1 = card1
    id_card2 = card2

    return id_card1, id_card2


def VirarCarta(pos_card):
    backCard_pack[pos_card] = card_pack_mixed[pos_card]
    ImprimirBaralho()
    time.sleep(2)


def DesvirarRodada(pos_card1, pos_card2):
    print()


def VerificarDisponibilidade(pos_card1, pos_card2):
    if (VerificarCartaAcerto(card_pack_mixed[pos_card1], card_pack_mixed[pos_card2])):
        PosicoesCobertas(pos_card1, pos_card2)
    else:
        backCard_pack[pos_card1] = pos_card1 + 1
        backCard_pack[pos_card2] = pos_card2 + 1

    print(f"Player 1 acertou: {qnt_acerto_player1}")


def VerificarCartaAcerto(card1, card2):
    global qnt_acerto_player1
    if card1.lower() == card2.lower():
        qnt_acerto_player1 += 1
        return True
    else:
        return False


# Funcao - colocamos posicoes que ja foram reveladas
def CobrirPosicao(card1, card2):
    packCards_complete.append(card1)
    packCards_complete.append(card2)


# Funcao - verifica se posicao já foi descoberta
def PosicoesCobertas(pos_card):
    for i in range(len(packCards_complete)):
        if packCards_complete[i] == pos_card:
            return True
        else:
            return False


def FluxoJogo():
    t = True
    EmbaralharCartas()
    while t:
        ImprimirBaralho()
        EscolherCartas()


FluxoJogo()
