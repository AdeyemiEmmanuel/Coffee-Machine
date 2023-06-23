# Coffee-Machine

The Coffee Machine project is a simple simulation of a coffee machine that allows users to order and customize their coffee drinks. It provides a user-friendly command-line interface (CLI) where users can interact with the coffee machine and place their orders.

## Features

- **Drink Selection**: Users can choose from a variety of coffee drinks such as espresso, cappuccino, and latte.
- **Payment**: The coffee machine calculates the total cost of the order based on the selected drink and any customizations made by the user.
- **Change Calculation**: If the user provides more money than required, the coffee machine calculates and returns the correct change.
- **Ingredient Management**: The coffee machine keeps track of the available ingredients, such as water, milk, and coffee. It checks the availability of ingredients before processing an order.
- **Reporting**: Users can request a report that shows the current status of available ingredients and the total amount of money made by the coffee machine.

## Usage

To use the Coffee Machine project, follow these steps:

1. Run the Python script:

   ```bash
   python main.py
   ```

2. The coffee machine will prompt you to select a drink or enter 'off' to exit the program.

3. Enter the name of the drink you want or enter 'report' to view the current status of available ingredients and the total amount of money made.

4. If you choose a drink, you will be prompted to insert coins to pay for the order. Enter the number of each coin denomination (quarters, dimes, nickels, pennies) you want to insert.

5. The coffee machine will process your order and check if there are enough ingredients and if the payment is sufficient. If the order is successful, it will dispense the drink and calculate and return the change if necessary.

6. Enjoy your coffee!

## Menu and Resources

The available drinks and their ingredients and costs are defined in the following dictionary:

```python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
```

The current available resources (water, milk, coffee) are defined in the following dictionary:

```python
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
```

## Disclaimer

This project is intended for educational purposes and does not represent a fully functional commercial coffee machine.
