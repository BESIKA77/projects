import random

def play_roulette(balance):
    print("Welcome to Roulette!")
    while True:
        bet = input(f"Your current balance is ${balance}. Place your bet on a number (0-36) or type 'exit' to return: ")
        if bet.lower() == 'exit':
            return balance
        if not bet.isdigit() or not (0 <= int(bet) <= 36):
            print("Invalid bet. Please choose a number between 0 and 36.")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance for this bet.")
            continue
        print("Spinning the wheel...")
        winning_number = random.randint(0, 36)
        print(f"The winning number is: {winning_number}")
        if bet == winning_number:
            print("Congratulations! You won!")
            balance += bet * 35
        else:
            print("Sorry, you lost. Better luck next time!")
            balance -= bet

def play_slots(balance):
    print("Welcome to Slots!")
    symbols = ['🍒', '🍋', '🍊', '🍉', '⭐', '🍀']
    while True:
        bet = input(f"Your current balance is ${balance}. Place your bet (or type 'exit' to return): ")
        if bet.lower() == 'exit':
            return balance
        if not bet.isdigit():
            print("Please enter a valid amount to bet or 'exit' to return.")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance for this bet.")
            continue
        spin_result = random.choices(symbols, k=3)
        print("You spun:", ' '.join(spin_result))
        
        if spin_result[0] == spin_result[1] == spin_result[2]:
            if spin_result[0] == '🍀':
                print("Congratulations! You hit the jackpot with 🍀🍀🍀!")
                balance += bet * 20
            else:
                print(f"Congratulations! You got three {spin_result[0]}!")
                balance += bet * 10
        else:
            print("No match. Better luck next time!")
            balance -= bet

def evaluate_hand(hand):
    total = sum(hand)
    if total == 21:
        return "blackjack"
    elif total > 21:
        return "bust"
    else:
        return total

def play_poker(balance):
    print("Welcome to Poker!")
    while True:
        bet = input(f"Your current balance is ${balance}. Place your bet (or type 'exit' to return): ")
        if bet.lower() == 'exit':
            return balance
        if not bet.isdigit():
            print("Invalid bet. Please enter a valid amount.")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance for this bet.")
            continue
        player_hand = random.sample(range(1, 14), 2)
        dealer_hand = random.sample(range(1, 14), 2)
        print(f"Your hand: {player_hand} (Total: {evaluate_hand(player_hand)})")
        print(f"Dealer's hand: {dealer_hand[0]} and a hidden card.")
        action = input("Do you want to (call, raise, or fold)? ").strip().lower()
        if action == "fold":
            print("You folded. You lose your bet.")
            balance -= bet
            continue
        elif action == "raise":
            raise_amount = input("How much do you want to raise? ")
            if not raise_amount.isdigit():
                print("Invalid amount. You lose your bet.")
                balance -= bet
                continue
            raise_amount = int(raise_amount)
            if raise_amount + bet > balance:
                print("Insufficient balance for this raise.")
                continue
            bet += raise_amount
            balance -= raise_amount
        print(f"Dealer's hand: {dealer_hand} (Total: {evaluate_hand(dealer_hand)})")
        player_total = evaluate_hand(player_hand)
        dealer_total = evaluate_hand(dealer_hand)
        if player_total == "bust":
            print("You busted! Dealer wins.")
            balance -= bet
        elif dealer_total == "bust":
            print("Dealer busted! You win!")
            balance += bet * 2
        elif player_total > dealer_total:
            print("You win!")
            balance += bet * 2
        elif player_total < dealer_total:
            print("Dealer wins.")
            balance -= bet
        else:
            print("It's a tie!")

def play_baccarat(balance):
    print("Welcome to Baccarat!")
    while True:
        bet = input(f"Your current balance is ${balance}. Place your bet (or type 'exit' to return): ")
        if bet.lower() == 'exit':
            return balance
        if not bet.isdigit():
            print("Invalid bet. Please enter a valid amount.")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance for this bet.")
            continue
        player_hand = random.sample(range(1, 14), 2)
        banker_hand = random.sample(range(1, 14), 2)
        print(f"Player's hand: {player_hand} (Total: {sum(player_hand)})")
        print(f"Banker's hand: {banker_hand} (Total: {sum(banker_hand)})")
        if sum(player_hand) > sum(banker_hand):
            print("Player wins!")
            balance += bet
        elif sum(player_hand) < sum(banker_hand):
            print("Banker wins.")
            balance -= bet
        else:
            print("It's a tie!")

def play_blackjack(balance):
    print("Welcome to Blackjack!")
    while True:
        bet = input(f"Your current balance is ${balance}. Place your bet (or type 'exit' to return): ")
        if bet.lower() == 'exit':
            return balance
        if not bet.isdigit():
            print("Invalid bet. Please enter a valid amount.")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient balance for this bet.")
            continue
        player_hand = [random.randint(1, 11), random.randint(1, 11)]
        dealer_hand = [random.randint(1, 11), random.randint(1, 11)]
        print(f"Your hand: {player_hand} (Total: {sum(player_hand)})")
        print(f"Dealer's hand: {dealer_hand[0]} and a hidden card.")
        while sum(player_hand) < 21:
            action = input("Do you want to hit or stand? ").strip().lower()
            if action == "hit":
                player_hand.append(random.randint(1, 11))
                print(f"Your hand: {player_hand} (Total: {sum(player_hand)})")
                if sum(player_hand) > 21:
                    print("You busted! Dealer wins.")
                    balance -= bet
                    break
            elif action == "stand":
                break
        if sum(player_hand) <= 21:
            print(f"Dealer's hand: {dealer_hand} (Total: {sum(dealer_hand)})")
            while sum(dealer_hand) < 17:
                dealer_hand.append(random.randint(1, 11))
                print(f"Dealer hits: {dealer_hand} (Total: {sum(dealer_hand)})")
            if sum(dealer_hand) > 21:
                print("Dealer busted! You win!")
                balance += bet
            elif sum(player_hand) > sum(dealer_hand):
                print("You win!")
                balance += bet
            elif sum(player_hand) < sum(dealer_hand):
                print("Dealer wins.")
                balance -= bet
            else:
                print("It's a tie!")

balance = 100

while True:
    age_check = input('Are you over 18 years old? (Yes or No) ').strip()
    if age_check.lower() == "no":
        print("It's not your place, boy. Bye Bye")
        quit()
    elif age_check.lower() == 'yes':
        print("Hello to Our casino! Here's games to play!")
        print("1) Roulette")
        print("2) Slots")
        print("3) Poker")
        print("4) Baccarat")
        print("5) Blackjack")
        choose_game1 = input("Choose a game: ").strip()
        if choose_game1.lower() == "roulette":
            balance = play_roulette(balance)
        elif choose_game1.lower() == "slots":
            balance = play_slots(balance)
        elif choose_game1.lower() == "poker":
            balance = play_poker(balance)
        elif choose_game1.lower() == "baccarat":
            balance = play_baccarat(balance)
        elif choose_game1.lower() == "blackjack":
            balance = play_blackjack(balance)
        else:
            print("Game not available yet.")
        if balance <= 0:
            print("You have run out of money! Game over.")
            break
    else:
        print("Please type 'Yes' or 'No'.")
