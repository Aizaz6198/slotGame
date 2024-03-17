import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

SYMBOL_COUNT = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

SYMBOL_VALUE = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def get_input(prompt, validator):
    while True:
        value = input(prompt)
        if validator(value):
            return value
        else:
            print("Invalid input. Please try again.")

def validate_positive_integer(value):
    return value.isdigit() and int(value) > 0

def validate_integer_range(value, min_val, max_val):
    return value.isdigit() and min_val <= int(value) <= max_val

def deposit():
    amount = get_input("What would you like to deposit? $", validate_positive_integer)
    return int(amount)

def get_number_of_lines():
    lines = get_input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ", 
                      lambda x: validate_integer_range(x, 1, MAX_LINES))
    return int(lines)

def get_bet():
    amount = get_input(f"What would you like to bet on each line? (${MIN_BET}-${MAX_BET}): ", 
                       lambda x: validate_integer_range(x, MIN_BET, MAX_BET))
    return int(amount)

def get_slot_machine_spin():
    symbols = [symbol for symbol, count in SYMBOL_COUNT.items() for _ in range(count)]
    return [[random.choice(symbols) for _ in range(ROWS)] for _ in range(COLS)]

def print_slot_machine(columns):
    for row in zip(*columns):
        print(" | ".join(row))

def check_winnings(columns, lines, bet):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(symbol == column[line] for column in columns):
            winnings += SYMBOL_VALUE[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin()
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer.lower() == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()
