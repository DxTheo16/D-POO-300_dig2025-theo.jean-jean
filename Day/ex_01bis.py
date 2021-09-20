# numbers = [512, 34, -123, 0, 42.08, -12]
# transaction = sorted(numbers,reverse=True)
# print(transaction)
def print_sorted_transactions(list):
    for i in sorted(list, reverse=True):
        if i > 0:
            print("You received ", i, "euros")
        elif i < 0:
            print("you spent", abs(i), "euros")
            
print_sorted_transactions([512, 34, -123, 0, 42.08, -12])