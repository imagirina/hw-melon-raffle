"""Randomly pick customer and print customer info"""

# Hint: remember to import any functions you need from
# other files or libraries

import random

from customers import get_customers_from_file

def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = random.choice(customers)

    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")


def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)


# To make the raffle run when run as a script, add 
# the condition if __name__ == "__main__" at the bottom of raffle.py.

if __name__ == "__main__":
    run_raffle()