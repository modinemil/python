import random

balance = int(1000)
input1 = int(input(f"Place a bet ur balance is {balance} "))

def my_balance():
    if int(input1) > balance:
        print("Ur broke!")
        exit()
    elif input1 <= 0:
        print("More!")
        exit()
    else:
        new_balance = balance - input1
        print(f"Your new balance is {new_balance}")
    





def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_score(hand):
    score = sum([11 if card['rank'] == 'A' else 10 if card['rank'] in ['K', 'Q', 'J'] else int(card['rank']) for card in hand])
    for card in hand:
        if card['rank'] == 'A' and score > 21:
            score -= 10
    return score

def display_board(player_hand, dealer_hand, player_score, dealer_score, game_over=False):
    print("\n===== BLACKJACK =====")
    
    if game_over:
        print("\n--- Final Results ---")
        print(f"Player's hand: {player_hand} (Score: {player_score})")
        print(f"Dealer's hand: {dealer_hand} (Score: {dealer_score})")
    else:
        print("\n--- Current Status ---")
        print(f"Player's hand: {player_hand} (Score: {player_score})")
        print(f"Dealer's hand: [{dealer_hand[0]}, *hidden*]")

def blackjack():
    global balance
    
    
    player_hand = []
    dealer_hand = []
    deck = create_deck()

    for _ in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    game_over = False

    while not game_over:
        display_board(player_hand, dealer_hand, player_score, dealer_score)

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if should_continue == 'y':
                player_hand.append(deck.pop())
                player_score = calculate_score(player_hand)
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deck.pop())
        dealer_score = calculate_score(dealer_hand)

    display_board(player_hand, dealer_hand, player_score, dealer_score, True)

    if player_score > 21:
        print("You went over. You lose.")
        balance -= input1
        print(f"Your balance is now {balance}")
   
    elif dealer_score > 21:
        print("Dealer went over. You win!")
        balance -=(input1)
        balance +=(input1 * 2)
        print(f"Your balance is now {balance}")
    
    elif player_score > dealer_score:
        print("You win!")
        balance -=(input1)
        balance += (input1 * 2)
        print(f"Your balance is now {balance}")
    
    elif player_score < dealer_score:
        print("You lose.")
        balance -= input1
        print(f"Your balance is now {balance}")
    
    else:
        print("It's a draw.")
        balance -= input1
        print(f"Your balance is now {balance}")






my_balance()

blackjack()
