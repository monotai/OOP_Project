import pygame
import json
pygame.init()
class Shop:
    def __init__(self):
        self.font = pygame.font.Font(None, 24)
        self.seed_inventory = self.load_seed_inventory()
        self.harvest_prices = self.load_harvest_prices()

    def load_seed_inventory(self):
        seed_inventory = {}
        try:
            with open("../data/data.json", "r") as file:
                data = json.load(file)
                for vegetable in data["Vegetables"]:
                    seed_name = vegetable["Vegetable Name"] + " Seeds"
                    seed_inventory[seed_name] = 5  # Example price
        except FileNotFoundError:
            print("Error: data.json not found. Please ensure it's in the correct location.")
            return {}
        except KeyError:
            print("Error: 'Vegetables' key not found in data.json. Check the file structure.")
            return {}
        return seed_inventory

    def load_harvest_prices(self):
        harvest_prices = {}
        try:
            with open("../data/data.json", "r") as file:
                data = json.load(file)
                for vegetable in data["Vegetables"]:
                    harvest_prices[vegetable["Vegetable Name"]] = vegetable["Price per KG (USD)"][0]
        except FileNotFoundError:
            print("Error: data.json not found. Please ensure it's in the correct location.")
            return {}
        except KeyError:
            print("Error: 'Vegetables' key not found in data.json. Check the file structure.")
            return {}
        return harvest_prices

    def buy(self, item, money):
        if item in self.seed_inventory and money >= self.seed_inventory[item]:
            return True, money - self.seed_inventory[item]
        return False, money

    def sell(self, item, money):
        if item in self.harvest_prices:
            return True, money + self.harvest_prices[item]
        return False, money

def shop_interface(player_money, player_inventory):
    shop = Shop()
    running = True
    while running:
        print("\nWelcome to the Shop!")
        print("1. Buy")
        print("2. Sell")
        print("3. Exit Shop")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n--- Buy ---")
            print("Available seeds:")
            for item, price in shop.seed_inventory.items():
                print(f"- {item}: ${price}")

            item_to_buy = input("Enter the name of the seed you want to buy: ")
            if item_to_buy in shop.seed_inventory:
                success, player_money = shop.buy(item_to_buy, player_money)
                if success:
                    if item_to_buy in player_inventory:
                        player_inventory[item_to_buy] += 1
                    else:
                        player_inventory[item_to_buy] = 1
                    print(f"Bought {item_to_buy}. Remaining money: ${player_money}")
                else:
                    print("Not enough money!")
            else:
                print("Invalid item name.")

        elif choice == '2':
            print("\n--- Sell ---")
            if not player_inventory:
                print("Your inventory is empty. Nothing to sell.")
            else:
                print("Your inventory:")
                for item, count in player_inventory.items():
                    if item in shop.harvest_prices:
                        print(f"- {item} ({count}): ${shop.harvest_prices[item]}/kg")

                item_to_sell = input("Enter the name of the vegetable you want to sell: ")
                if item_to_sell in shop.harvest_prices and item_to_sell in player_inventory:
                    try:
                        kilograms = float(input(f"Enter the kilograms of {item_to_sell} you want to sell: "))
                        if kilograms > 0 and kilograms <= player_inventory[item_to_sell]:
                            price_per_kg = shop.harvest_prices[item_to_sell]
                            earned_money = price_per_kg * kilograms
                            player_money += earned_money
                            player_inventory[item_to_sell] -= kilograms
                            print(f"Sold {kilograms}kg of {item_to_sell} for ${earned_money:.2f}. Remaining money: ${player_money}")
                            if player_inventory[item_to_sell] == 0:
                                del player_inventory[item_to_sell]
                        else:
                            print("Invalid amount to sell.")
                    except ValueError:
                        print("Invalid input for kilograms. Please enter a number.")
                else:
                    print("Invalid item name or item not in inventory.")

        elif choice == '3':
            running = False
            print("Exiting the shop.")

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    return player_money, player_inventory

if __name__ == '__main__':
    player_money = 100
    player_inventory = {"Carrot": 2, "Potato": 1}

    player_money, player_inventory = shop_interface(player_money, player_inventory)

    print("\n--- After Shop ---")
    print(f"Remaining Money: ${player_money}")
    print(f"Inventory: {player_inventory}")
