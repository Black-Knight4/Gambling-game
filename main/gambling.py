import random
def spin_choice():
    symbols = ["🥀", "💔", "😭", "💀", "🥰"]
    slot = []
    for i in range(3):
        slot.append(random.choice(symbols))
    return slot
def print_slot(slot_list):
    print("*******************")
    n=0
    for i in slot_list:
        n+=1
        if n != 3:
            print(i, end=" |  ")
        else:
            print(i, end=" ")
    print()
    print("*******************")

def payout(slot_playout, balance1, bet):
    bet = int(bet)
    if slot_playout[0] == slot_playout[1] == slot_playout[2]:
        if slot_playout[0] == "😭":
            bet = bet * 2
            balance1 +=bet
            print("You won * 2!! 🤑")
        elif slot_playout[0] == "💔":
            bet = bet * 3
            balance1 += bet
            print("You won * 3!! 🤑")
        elif slot_playout[0] == "🥀":
            bet = bet * 4
            balance1 += bet
            print("You won * 4!! 🤑")
        elif slot_playout[0] == "💀":
            bet = bet * 5
            balance1 += bet
            print("You won * 5!! 🤑")
        elif slot_playout[0] == "🥰":
            bet = bet * 6
            balance1 += bet
            print("You won * 6!! 🤑")
    else:
        balance1 = balance1-int(bet)
        print("You lost :(")
        print("*******************")
    return balance1
def main():
    balance = 100
    print("Welcome to the slots! ")
    print("Symbols: 🥀 💔 😭 💀 🥰")
    while balance > 0:
        print(f"Current balance: ${balance}")
        quit1 = input("Would you like to quit(before you go broke)Y/N: ")
        if (quit1.upper() == "Y"):
            break
        bet_amount = input("Place your bet amount: ")
        if not bet_amount.isdigit():
            print("Incorrect input")
            continue
        slot1 = spin_choice()
        print_slot(slot1)
        balance = payout(slot1, balance, bet_amount)


if __name__ == '__main__':
    main()
    print("Goodbye! You are broke now")