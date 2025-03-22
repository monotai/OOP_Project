import pygame
import json

pygame.init()

class Shop:
    def __init__(self):
        self._seed_inventory = self._load_seed_inventory()
        self._harvest_prices = self._load_harvest_prices()

    def _load_seed_inventory(self):
        seed_inventory = {}
        try:
            with open("../data/Plant_Stardew.json", "r") as file:
                data = json.load(file)
                for crop_id, crop_data in data["Crops"].items():
                    seed_name = crop_data["Name"]
                    seed_inventory[seed_name] = crop_data["Price"]
        except (FileNotFoundError, KeyError):
            print("Error loading seed inventory.")
            return {}
        return seed_inventory

    def _load_harvest_prices(self):
        harvest_prices = {}
        try:
            with open("../data/Plant_Stardew.json", "r") as file:
                data = json.load(file)
                for crop_id, crop_data in data["Crops"].items():
                    harvest_name = crop_data["HarvestName"]
                    harvest_prices[harvest_name] = crop_data["HarvestPrice"]
        except (FileNotFoundError, KeyError):
            print("Error loading harvest prices.")
            return {}
        return harvest_prices

    def __getitem__(self, item):
        return self._seed_inventory.get(item, None)

    def __str__(self):
        seeds = "\n".join([f"{item}: ${price}" for item, price in self._seed_inventory.items()])
        return f"Available Seeds:\n{seeds}"

    def buy(self, item, kg, money):
        if item in self._seed_inventory:
            total_price = self._seed_inventory[item] * kg
            if money >= total_price:
                return True, money - total_price  # Successful purchase
        return False, money  # Not enough money or item not available

    def sell(self, item, weight, money):
        if item in self._harvest_prices:
            return True, money + (self._harvest_prices[item] * weight)
        return False, money

class Player:
    def __init__(self, money=100):
        self.money = money
        self.inventory = {}

    def __str__(self):
        inventory_str = "\n".join([f"{item}: {count}kg" for item, count in self.inventory.items()]) or "Empty"
        return f"Money: ${self.money}\nInventory:\n{inventory_str}"

    def buy_item(self, shop, item, kg):
        success, self.money = shop.buy(item, kg, self.money)
        if success:
            self.inventory[item] = self.inventory.get(item, 0) + kg
            print(f"Bought {kg}kg of {item}. Remaining money: ${self.money:.2f}")
        else:
            print("Not enough money or item not available.")

    def sell_item(self, shop, item, weight):
        if item in self.inventory and self.inventory[item] >= weight:
            success, self.money = shop.sell(item, weight, self.money)
            if success:
                self.inventory[item] -= weight
                if self.inventory[item] == 0:
                    del self.inventory[item]
                print(f"Sold {weight}kg of {item}. Money: ${self.money:.2f}")
            else:
                print("Sale failed.")
        else:
            print("Not enough items to sell or item not in inventory.")

def shop_interface():
    shop = Shop()
    player = Player()

    running = True
    while running:
        print("\nWelcome to the Shop!")
        print("1. Buy Seeds")
        print("2. Sell Harvest")
        print("3. View Inventory")
        print("4. Exit Shop")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n--- Buy Seeds ---")
            print(shop)  # Display only seed inventory

            item_to_buy = input("Enter the name of the seed you want to buy: ")
            if item_to_buy in shop._seed_inventory:
                try:
                    kg = float(input(f"Enter how many kg of {item_to_buy} you want to buy: "))
                    if kg > 0:
                        player.buy_item(shop, item_to_buy, kg)
                    else:
                        print("Invalid quantity. Please enter a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("Item not available.")

        elif choice == '2':
            print("\n--- Sell Harvest ---")
            print(player)

            item_to_sell = input("Enter the name of the vegetable you want to sell: ")
            if item_to_sell in player.inventory:
                try:
                    weight = float(input(f"Enter the kilograms of {item_to_sell} you want to sell: "))
                    if weight > 0:
                        player.sell_item(shop, item_to_sell, weight)
                    else:
                        print("Invalid quantity. Please enter a positive number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("Item not found in inventory.")

        elif choice == '3':
            print("\n--- Player Info ---")
            print(player)

        elif choice == '4':
            running = False
            print("Exiting the shop.")

        else:
            print("Invalid choice.")

    print("\n--- After Shop ---")
    print(player)

if __name__ == '__main__':
    shop_interface()