from django.test import TestCase

# Create your tests here.

import random

class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        self.deposit_count = 0
        self.deposit_amount_history = []
        self.withdraw_amount_history = []

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = self.balance * 1.01
        self.deposit_amount_history.append(amount)

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        self.withdraw_amount_history.append(amount)

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

    def deposit_history(self):
        print(f'{self.name} deposit history: {self.deposit_amount_history}')

    def withdraw_history(self):
        print(f'{self.name} withdraw history: {self.withdraw_amount_history}')

account_list = []
kim = Account("kim", 10000)
account_list.append(kim)
lee = Account("lee", 100000)
account_list.append(lee)
choi = Account("choi", 10000000)
account_list.append(choi)
kim.deposit(10000000)
kim.deposit(1000)
lee.deposit(50000000)
choi.deposit(78000000)
kim.deposit(10500)
choi.withdraw(100)
lee.withdraw(15000)
lee.withdraw(10000)
choi.withdraw(50000)
kim.withdraw(105000)


kim.deposit_history()
lee.deposit_history()
choi.deposit_history()
kim.withdraw_history()
lee.withdraw_history()
choi.withdraw_history()
