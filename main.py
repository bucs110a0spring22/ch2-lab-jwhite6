import random

#Part A

weeks = 16
classes = 5
tuition = 6000
classes_per_week = 13 
cost_per_week = ((tuition / classes) / weeks)
cost_per_class = ((classes_per_week)/(cost_per_week))
print("Cost per week:", cost_per_week)
print("Cost per class:", cost_per_class)
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))

#Part B

num = [5, 10, 15, 20, 25]
pick = random.choice(num)
print(pick)