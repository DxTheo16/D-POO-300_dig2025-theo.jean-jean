
# print_transactions[1:4]
# for x in range(len(a)):
#     print a[x]
# print("You received", print_transactions[0], "euros")
# print("You spent", print_transactions[1], "euros")
# print("you received", print_transactions[2], "euros")

def print_transactions(list):
    for i in list:
        if i > 0:
            print("You received ", i, " euros")
        else:
            print("You spent ", abs(i), " euros")


print_transactions([512, -12, 42.08])