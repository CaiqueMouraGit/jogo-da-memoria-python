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
qnt_acerto_player1=0

def EmbaralharCartas():
    card_pack=card_pack_original.copy()
    tam = len(card_pack)
    for card in range(30):
        num = random.randint(0, len(card_pack) - 1)
        card_pack_mixed.append(card_pack[num])
        card_pack.pop(num)
        tam -= 1


def EscolherCartas():
    card1 = int(input("Escolha a primeira carta: "))
    card2 = int(input("Escolha a segunda carta: "))

    virarCarta(card1 - 1, card2 - 1)


def virarCarta(pos_card1, pos_card2):
    backCard_pack[pos_card1] = card_pack_mixed[pos_card1]
    backCard_pack[pos_card2] = card_pack_mixed[pos_card2]

    ImprimirBaralho()
    time.sleep(6)

    if (VerificarCarta(card_pack_mixed[pos_card1], card_pack_mixed[pos_card2])):
        PosicoesCobertas(pos_card1, pos_card2)
    else:
        backCard_pack[pos_card1] = pos_card1 + 1
        backCard_pack[pos_card2] = pos_card2 + 1

    print(f"Player 1 acertou: {qnt_acerto_player1}")


def VerificarCarta(card1, card2):
    global qnt_acerto_player1
    if card1.lower() == card2.lower():
        qnt_acerto_player1+=1
        return True
    else:
        return False


def PosicoesCobertas(pos1, pos2):
    packCards_complete.append(pos1)
    packCards_complete.append(pos2)


def ImprimirBaralho():
    pular_linha = 0
    for lin in range(len(backCard_pack)):
        print(f"| {backCard_pack[lin]} |", end="")

        if pular_linha < 5:
            pular_linha += 1
        else:
            pular_linha = 0
            print()


def FluxoJogo():
    t = True
    EmbaralharCartas()
    while t:
        ImprimirBaralho()
        EscolherCartas()



FluxoJogo()
