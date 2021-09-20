Class Budget:









myBudget = Budget ("~/ data . json ")
for category in myBudget . get_categories () :
myBudget . print_sorted_transactions ( category )
myBudget . print_transactions ()