class Budget:

    def __init__(self):
        self.__transactions = []

    def add_transactions(self,list):
        self.__transactions += list

    def print_transactions(self):
        print(self.__transactions)
        for i in self.__transactions:
            if i > 0:
                print("You received ", i, " euros")
            else:
                print("You spent ", abs(i), " euros")

    def print_sorted_transactions(self):
        self.__transactions.sort(reverse=True)
        self.print_transactions()


myBudget = Budget()
myBudget.add_transactions([512 , 42.08 , -12])
myBudget.add_transactions([ -9000])
myBudget.print_transactions()
myBudget.print_sorted_transactions()