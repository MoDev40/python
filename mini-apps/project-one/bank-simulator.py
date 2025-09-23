bank = {
    "name": "St ex bank",
    "address": "123 Main St.",
    "accounts": {
        "127091256": {
            "name": "John Doe",
            "address": "19 St.",
            "balance": 1500,
            "transactions": [
                {
                    "date": "2018-01-31",
                    "amount": 500,
                    "currency": "USD",
                    "type": "deposit",
                },
                {
                    "date": "2018-06-22",
                    "amount": 500,
                    "currency": "USD",
                    "type": "withdrawal",
                },
                {
                    "date": "2018-09-22",
                    "amount": 1500,
                    "currency": "USD",
                    "type": "deposit",
                },
                {
                    "date": "2018-01-31",
                    "amount": 500,
                    "currency": "USD",
                    "type": "send",
                },
            ],
            "transfers": [
                {
                    "date": "2018-01-31",
                    "amount": 500,
                    "currency": "USD",
                    "type": "send",
                    "from": "12709125",
                    "to": "89120071",
                }
            ],
        },
        "89120071": {
            "name": "Jane",
            "address": "143 London St.",
            "balance": 500,
            "transactions": [
                {
                    "date": "2018-01-31",
                    "amount": 500,
                    "currency": "USD",
                    "type": "receive",
                }
            ],
            "transfers": [
                {
                    "date": "2018-01-31",
                    "amount": 500,
                    "currency": "USD",
                    "type": "receive",
                    "from": "12709125",
                    "to": "89120071",
                }
            ],
        },
    },
}


def show_my_balance(account_number):
    print(bank["accounts"][account_number]["balance"])


def show_my_transactions(account_number):
    print(bank["accounts"][account_number]["transactions"])


def show_my_transfers(account_number):
    print(bank["accounts"][account_number]["transfers"])


def deposit(account_number, amount, currency="USD"):
    bank["accounts"].get(account_number)["balance"] += amount
    bank["accounts"].get(account_number)["transactions"].append(
        {
            "date": "2019-01-31",
            "amount": amount,
            "currency": currency,
            "type": "deposit",
        }
    )
    print("You successfully deposited ${}{}".format(amount, currency))


def withdraw(account_number, amount, currency="USD"):
    bank.get("accounts").get(account_number)["balance"] -= amount
    bank.get("accounts").get(account_number)["transactions"].append(
        {
            "date": "2019-07-11",
            "amount": amount,
            "currency": currency,
            "type": "withdrawal",
        }
    )
    print("You successfully withdrawn ${}{}".format(amount, currency))


is_end = False
while not is_end:
    account = input("What is the account number? ").strip().lower()
    if account not in bank["accounts"]:
        print("Invalid account number")
        continue

    actions = [
        "show_my_balance",
        "deposit",
        "withdrawal",
        "transfer",
        "show_my_transactions",
        "show_my_transfers",
    ]
    for x in range(len(actions)):
        print(f"{x}:{actions[x]}")

    index: int = int(input("What would you like to do? ") or "0")
    action: str = actions[index]

    match action:
        case "deposit":
            amount = input("What is the amount you want to deposit? ").strip()
            deposit(account, float(amount))
        case "withdrawal":
            amount = input("What is the amount you want to withdraw? ").strip()
            withdraw(account, float(amount))
        case "show_my_balance":
            show_my_balance(account)
        case "show_my_transactions":
            show_my_transactions(account)
        case "show_my_transfers":
            show_my_transfers(account)

    choice = input("Would you like to continue? (Y/N): ").strip().lower()
    if choice == "n":
        is_end = True
else:
    print("Thanks for using our bank")
