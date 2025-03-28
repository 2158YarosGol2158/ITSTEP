# Завдання 1
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self, quantity):
        return self.stock >= quantity

    def reduce_stock(self, quantity):
        if self.is_available(quantity):
            self.stock -= quantity
            return True
        return False

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.is_available(quantity):
            if product.name in self.items:
                self.items[product.name]['кількість'] += quantity
            else:
                self.items[product.name] = {'продукт': product, 'кількість': quantity}
            product.reduce_stock(quantity)

    def remove_product(self, product_name, quantity):
        if product_name in self.items:
            if self.items[product_name]['кількість'] > quantity:
                self.items[product_name]['кількість'] -= quantity
            else:
                del self.items[product_name]

    def total_price(self):
        return sum(item['продукт'].price * item['кількість'] for item in self.items.values())

    def show_cart(self):
        for name, item in self.items.items():
            print(f"{name}: {item['кількість']} x {item['продукт'].price} грн = {item['кількість'] * item['продукт'].price} грн")
        print(f"Всього: {self.total_price()} грн\n")


p1 = Product("Ноутбук", 25000, 5)
p2 = Product("Мишка", 500, 10)

cart = Cart()
cart.add_product(p1, 1)
cart.add_product(p2, 2)
cart.show_cart()


cart.remove_product("Мишка",1)
cart.show_cart()

print(f"Всього: {cart.total_price()} грн")

# Завдання 2

class BankAccount:
    def __init__(self, owner: str, account_number: str, balance: float = 0.0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Рахунок {self.account_number}, Власник: {self.owner}, Баланс: {self.balance:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def __add__(self, account: BankAccount):
        if account.account_number in self.accounts:
            return "Рахунок з таким номером вже існує"
        self.accounts[account.account_number] = account
        return f"Рахунок {account.account_number} для {account.owner} додано до банку."

    def deposit(self, account_number: str, amount: float):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                return f"Поповнено {amount:.2f} на рахунок {account_number}. Новий баланс: {account.balance:.2f}"
            return "Сума має бути більше 0"
        return "Рахунок не знайдений"

    def withdraw(self, account_number: str, amount: float):
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                return f"Знято {amount:.2f} з рахунку {account_number}. Новий баланс: {account.balance:.2f}"
            return "Недостатньо коштів або некоректна сума"
        return "Рахунок не знайдений"

    def transfer(self, from_acc: str, to_acc: str, amount: float):
        if from_acc not in self.accounts or to_acc not in self.accounts:
            return "Один або обидва рахунки не існують"
        if amount <= 0:
            return "Сума переказу має бути більше 0"
        sender = self.accounts[from_acc]
        receiver = self.accounts[to_acc]
        if sender.balance < amount:
            return "Недостатньо коштів для переказу"
        sender.balance -= amount
        receiver.balance += amount
        return f"Переказано {amount:.2f} з {from_acc} на {to_acc}"

    def __str__(self):
        return "\n"+"\n".join(str(acc) for acc in self.accounts.values())


bank = Bank()
user1 = BankAccount("Іван Сидоренко", "12345", 1000)
user2 = BankAccount("Петро Іванус", "67890", 500)

print(bank.__add__(user1))
print(bank.__add__(user2))
print(bank.deposit("67890",100))
print(bank.withdraw("12345",100))
print(bank.transfer("12345","67890",900))
print(bank.__str__())