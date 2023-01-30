class Bank:
    def __init__(self, name, balance) -> None:
        self._name = name 
        self._balance = balance
        self._balance_2 = 200 #Баланс второго профиля для метода _plus


    def MoneyX(self):
        balance_add = int(input("Введите сумму пополнения: "))
        self._balance = self._balance + balance_add
        print(f"Баланс успешно пополнен! Ваш баланс: {self._balance}")
    
    def _kill(self):
        self._balance = self._balance * 0    
        print(f"Баланс обнулён. Ваш баланс:{self._balance}")
    
    def __jackpot(self):
        self._balance = self._balance * 10
        print("Баланс:", self._balance)

    def _plus(self):
        self._balance = self._balance + self._balance_2
        print("Баланс:", self._balance)


a = Bank("Aziret", 15000)
a.MoneyX()

