S=0
while True:
    n=input()
    if n=='0':
        break
    m=input()
    if n=='1':
        if m=='1':
            print("Medium Wac 4")
            S+=4
        elif m=='2':
            print("WChicken Nugget 8")
            S+=8
        elif m=='3':
            print("Geez Burger 7")
            S+=7
        elif m=='4':
            print("ButtMilk Crispy Chicken 6")
            S+=6
        else:
            print("Plastic Toy 3")
            S+=3
    else:
        if m=='1':
            print("German Fries 2")
            S+=2
        elif m=='2':
            print("Durian Slices 3")
            S+=3
        elif m=='3':
            print("WcFurry 5")
            S+=5
        else:
            print("Chocolate Sunday 7")
            S+=7
print(f"Total: {S}")
