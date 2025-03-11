import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_card():
    card = random.choice(cards)
    return card

def deal_hand():
    hand = []
    for _ in range(2):
        card = get_card()
        hand.append(card)
    return hand

def detect_blackjack(hand):
    total = sum(hand)
    is_blackjack = len(hand) == 2 and total == 21
    return is_blackjack

def score_hand(hand):
    total = sum(hand)
    for card in hand:
        # check if ace value should be 1 or 11
        if card == 11:
            if total > 21:
                total -= 10
    return total

def prompt_card():
    wants_a_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    return wants_a_card

def print_hands(your_hand, dealer_hand):
    your_score = score_hand(your_hand)
    print(f"Your cards: {your_hand}, current score: {your_score}\n")
    print(f"Computer's first card: {dealer_hand[0]}")

def compare_scores(your_hand, dealer_hand):
    player_blackjack = detect_blackjack(your_hand)
    dealer_blackjack = detect_blackjack(dealer_hand)
    your_score = score_hand(your_hand)
    dealer_score = score_hand(dealer_hand)
    keep_playing = True
    print_hands(your_hand, dealer_hand)
    if dealer_blackjack:
        print("Computer has Blackjack! Game over. You lose. 😭")
        keep_playing = False
        start_game()
    elif player_blackjack:
        print("You got Blackjack! Game over. You win! 😀")
        keep_playing = False
        start_game()
    elif your_score > 21:
        print("You went over! Game over. You lose! 😭")
        keep_playing = False
        start_game()
    else:
        while keep_playing:
            if dealer_score < 16 and dealer_score <= your_score:
                while dealer_score < 16 and dealer_score <= your_score:
                    card = get_card()
                    dealer_hand.append(card)
                    dealer_score = score_hand(dealer_hand)
            wants_a_card = prompt_card()
            if wants_a_card == 'y':
                card = get_card()
                your_hand.append(card)
                compare_scores(your_hand, dealer_hand)
            else:
                if your_score == dealer_score and your_score <= 21:
                    print(f"Your final hand: {your_hand}, final score: {your_score}\n")
                    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}. You tied. 😑")
                elif your_score > dealer_score and your_score <= 21:
                    print(f"Your final hand: {your_hand}, final score: {your_score}\n")
                    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}. You won! 😀")
                elif your_score <= 21 and dealer_score > 21:
                    print(f"Your final hand: {your_hand}, final score: {your_score}\n")
                    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}.\nComputer went over. You won! 😀")
                elif your_score > 21 and dealer_score <= 21:
                    print(f"Your final hand: {your_hand}, final score: {your_score}\n")
                    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}.\nYou went over. You lose! 😭")
                else:
                    print(f"Your final hand: {your_hand}, final score: {your_score}\n")
                    print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}. You lose! 😭")
                keep_playing = False
        start_game()

def clear_console():
    print("\n" * 100)

def start_game():
    wants_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if wants_to_play == 'y':
        clear_console()
        print(art.logo)
        your_hand = deal_hand()
        dealer_hand = deal_hand()
        compare_scores(your_hand, dealer_hand)
    else:
        print("Goodbye!)")
        exit()

start_game()

