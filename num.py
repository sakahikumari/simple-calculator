while True:
    a=int(input("entre first number:"))
    b=int(input("entre second number:"))
    if a<1 or b<1:
        print("entre only whole no.")
        continue

    print("\n---what you want to calculate---")
    print("1. ➕ addition")
    print("2. ➖ subtraction")
    print("3. ✖️ multiplication")
    print("4. ➗ division")

    choose = input("entre which no. :")

    if choose == "1":
        print(a+b)
    elif choose == "2":
        print(a-b)
    elif choose == "3":
        print(a*b)
    elif choose == "4":
        print(a/b)
    else :
        print("❌ invalid no.")   
    
    user=input("you want repeat calculation y/n:")
    if user != "y":
        print("🧮 calclution is stoped now")
        print("thank you for using  our system 💕")
        break
        
