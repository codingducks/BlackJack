#First player to win 3 hands wins the game

import random

deck = [
'[♥01-ace-11♥]','[♥02-two-02♥]','[♥03-three-03♥]', '[♥04-four-04♥]',
'[♥05-five-05♥]','[♥06-six-06♥]','[♥07-seven-07♥]','[♥08-eight-08♥]',
'[♥09-nine-09♥]','[♥10-ten-10♥]','[♥10-jack-10♥]','[♥10-queen-10♥]',
'[♥10-king-10♥]',
'[♠01-ace-11♠]','[♠02-two-02♠]','[♠03-three-03♠]','[♠04-four-04♠]',
'[♠05-five-05♠]','[♠06-six-06♠]','[♠07-seven-07♠]','[♠08-eight-08♠]',
'[♠09-nine-09♠]','[♠10-ten-10♠]','[♠10-jack-10♠]','[♠10-queen-10♠]',
'[♠10-king-10♠]',
'[♦01-ace-11♦]','[♦02-two-02♦]','[♦03-three-03♦]','[♦04-four-04♦]',
'[♦05-five-05♦]','[♦06-six-06♦]','[♦07-seven-07♦]','[♦08-eight-08♦]',
'[♦09-nine-09♦]','[♦10-ten-10♦]','[♦10-jack-10♦]','[♦10-queen-10♦]',
'[♦10-king-10♦]',
'[♣01-ace-11♣]','[♣02-two-02♣]','[♣03-three-03♣]','[♣04-four-04♣]',
'[♣05-five-05♣]','[♣06-six-06♣]','[♣07-seven-07♣]','[♣08-eight-08♣]',
'[♣09-nine-09♣]','[♣10-ten-10♣]','[♣10-jack-10♣]','[♣10-queen-10♣]',
'[♣10-king-10♣]'
]

random.shuffle(deck)

players_points = 0
dealers_points = 0

dealer = "Dealers Points"
player = "Players Points"

def hit(hand,total):
    card = deck[0]
    card_value = int(card[2:4])
    hand.append(card)
    deck.remove(card)
    if card_value == 1:
        if total + 11 <= 21:
            print(card)
            return total + 11
        elif total + 11 > 21:
            print(card)
            return total + card_value
    else:
        print(card)
        return total + card_value

def print_cards(hand):
     cards = len(hand)
     for card in hand:
         print(card)

def check_split(card1_value,card2_value):
    card1 = players_hand[0]
    card2 = players_hand[1]
    card1_value = int(card1[2:4])
    card2_value = int(card2[2:4])
    if card1_value == card2_value:
        split_variable = "split"
        return split_variable
    else:
        split_variable = "not split"
        return split_variable

def split(split,split_total,which_card):
    card = players_hand[which_card]
    split.append(card)
    hit(split,split_total)

    split_card1 = split[0]
    split_card2 = split[1]
    split_value1 = int(split_card1[2:4])
    split_value2 = int(split_card2[2:4])

    if split_value1 ==1:
        if split_value2 + 11 <= 21:
            split_total = split_value2 + 11
    elif split_value2 ==1:
        if split_value1 + 11 <= 21:
            split_total = split_value1 + 11
    elif split_value1 and split_value2 != 1:
        split_total = split_value1 + split_value2
    print(split[0], "split total =", split_total)
    return split_total



def calc_points(name, points):
    points = points + 1
    print(name, "=", points)
    return points



running = True
while running:

    players_total = 0
    dealers_total = 0

    players_hand = []
    dealers_hand = []

    card1_value =0
    card2_value = 0

    split1 =[]
    split2 =[]

    split1_total = 0
    split2_total = 0


    print("Your cards are")
    players_total = hit(players_hand, players_total)
    players_total = hit(players_hand, players_total)
    print("Your total = ", players_total,"\n")

    print("The Dealer Has a")
    dealers_total = hit(dealers_hand, dealers_total)
    print("\n")

    split_variable = check_split(card1_value,card2_value)

    if split_variable == "split":

        splitting = True
        while splitting:
            if split_variable == "split":
                print("Do you wish to split?")
                impp = input("y/n\n")
                if impp == "y":
                    print("Split 1 ")
                    split1_total = split(split1,split1_total,0)
                    print("Split 2")
                    split2_total = split(split2,split2_total,1)
                    print("\n")
                    break
                elif impp == "n":
                    break
                else:
                    print("Please Type Y or N")
                    continue

    if split_variable == "not split" or impp == "n":
        inputting = True
        while inputting:            
            print("Do You Hit or Stick?")
            imp = input(">")
            if imp == "h" or imp == "hit":
                players_total = hit(players_hand,players_total)
                print("Your total =", players_total,"\n")
                if players_total > 21:
                    print("*****YOU BUST!*****","\n")
                    break
            elif imp == "s" or imp == "stick":
                print("You stick with", players_total,"\n")
                inputting = False
            else:
                print("Please Enter a Valid Key")

    print("Dealer Draws")
    dealers_total = hit(dealers_hand,dealers_total)
    print("\n Dealers Hand Is")
    print_cards(dealers_hand)
    print ("Dealers Total Is", dealers_total)


    for cards in dealers_hand:
        is_ace = int(cards[2:4])

    if is_ace == 1:
        while dealers_total <=17:
            print("Dealer Hits")
            dealers_total = hit(dealers_hand, dealers_total)
            print("Dealers Total =", dealers_total)
            if dealers_total > 21:
                print("*****DEALER BUST!*****","\n")
                break
            while dealers_total < 17:
                print("Dealer Hits")
                dealers_total = hit(dealers_hand, dealers_total)
                print("Dealers Total =",dealers_total)
                if dealers_total > 21:
                    print("*****DEALER BUSTS*****")
                    break
            else:
                print("Dealer Sticks with", dealers_total)

        else:
            print("Dealer Sticks with", dealers_total)
    else:
        while dealers_total < 17:
            print("Dealer_hits")
            dealers_total = hit(dealers_hand, dealers_total)
            print("Dealers Total =",dealers_total)
            if dealers_total > 21:
                print("*****DEALER BUST!*****","\n")
                break
        else:
            print("Dealer Sticks With",  dealers_total)

    if split_variable == "not split" or impp =="n":
        if dealers_total > 21:
            if players_total <= 21:
                print("Player Wins Hand")
                players_points = calc_points(player, players_points)
                if players_points >= 3:
                    running = False
                print("-------------------------------------------------------")

            else:
                print("No Points Awarded")
                print("-------------------------------------------------------")

        elif dealers_total <= 21:  
            if players_total <= 21 and players_total > dealers_total:
                print("Player Wins Hand")
                players_points = calc_points(player, players_points)
                if players_points >=3:
                    running = False
                print("-------------------------------------------------------")
            else:
                print("Dealer Wins Hand")
                dealers_points = calc_points(dealer, dealers_points)
                if dealers_points >= 3:
                      running = False
                print("-------------------------------------------------------")

    else:   
        if dealers_total > 21:
            if split1_total <= 21:
                print("Split 1 Beats Dealer")
                players_points = calc_points(player, players_points)
                if players_points >= 3:
                    running = False
            elif split1_total > 21:
                print("Draw, No Points Awarded")
            if split2_total <=21:
                print("Split 2 Beats Dealer")
                players_points = calc_points(player, players_points)

                if players_points >= 3:
                    running = False
                print("-------------------------------------------------------")
            elif split2_total > 21:
                print("Draw, No Points Awarded")
                print("-------------------------------------------------------")
        elif dealers_total <=21:
            if split1_total < 21 and split1_total > dealers_total:
                print("Split 1 beats Dealer")
                players_points = calc_points(player, players_points)
                if players_points >= 3:
                    running = False
            else:
                print("Dealer Wins Hand Over Split 1")
                dealers_points = calc_points(dealer, dealers_points)
                if dealers_points >= 3:
                    running = False
            if split2_total < 21 and split2_total > dealers_total:
                print("Split 2 Beats Dealer")
                players_points = calc_points(player, players_points)
                if players_points >= 3:
                    running = False
                print("-------------------------------------------------------")
            else:
                print("Dealer Wins Hand Over Split 2")
                dealers_points = calc_points(dealer, dealers_points)
                if dealers_points >= 3:
                    running = False
                print("-------------------------------------------------------")            
if players_points > dealers_points:
    print("**** YOU WIN THE GAME *****")
else:
    print("*****DEALER WINS THE GAME*****")
