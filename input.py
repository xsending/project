import pyinputplus as pyip


cost = 0

while True:
    print("Hello and welcome! Time to create your own sandwich")
    bread = pyip.inputMenu(('wheat', 'white', 'sourdough'))
    if bread == 'wheat':
        cost += 15
    elif bread == 'white':
        cost += 20
    else:
        cost += 25
    protein = pyip.inputMenu(('chicken', 'turkey', 'ham', 'tofu'))
    if protein == 'chicken':
        cost += 45
    elif protein == 'turkey':
        cost += 65
    elif protein == 'ham':
        cost += 35
    else:
        cost += 30
    cheese = pyip.inputYesNo(prompt= "Do you want cheese[yes/no]?: ")
    if cheese == "yes":
        cheese_type = pyip.inputMenu(('cheddar', 'swiss', 'mozarella'))
        if cheese_type == 'cheddar':
            cost += 15
        elif cheese_type == 'swiss':
            cost += 20
        else:
            cost += 30
    else:
        pass
    condiment = pyip.inputYesNo(prompt= "Do you want to add condiments[yes/no]?: ")
    if condiment == "yes":
        condiment_type = pyip.inputMenu(('mayo', 'mustard', 'lettuce', 'tomato'))
        if condiment_type == 'mayo':
            cost += 7
        elif condiment_type == 'mustard':
            cost += 7
        elif condiment_type == 'lettuce':
            cost += 12
        elif condiment_type == 'tomato':
            cost += 9
    else:
        pass
    amount = pyip.inputInt(prompt="How many sandwiches?: ")
    print(f"Amount: {amount} Cost: {cost * amount}")
    break
