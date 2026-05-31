import math
from Scient import *

history = []

def show_menu():
    print("\n=== Scientific Calculator ===")
    print("1. Add 2. Subtract")
    print("3. Multiply 4. Divide")
    print("5. Power 6. Square Root")
    print("7. Sin 8. Cos")
    print("9. Tan 10. Log")
    print("11. Ln 12. History")
    print("0. Exit")

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "0":
        print("Goodbye!")
        break

    elif choice in ["1","2","3","4","5"]:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    if choice=="1": print("Result:", add(a,b))
    elif choice=="2": print("Result:", subtract(a,b))
    elif choice=="3": print("Result:", multiply(a,b))
    elif choice=="4": print("Result:", divide(a,b))
    elif choice=="5": print("Result:", power(a,b))

    elif choice in ["6","7","8","9","10","11"]:
        a = float(input("Enter number: "))
    if choice=="6": print("Result:", sqrt(a))
    elif choice=="7": print("Result:", sin(a))
    elif choice=="8": print("Result:", cos(a))
    elif choice=="9": print("Result:", tan(a))
    elif choice=="10": print("Result:", log(a))
    elif choice=="11": print("Result:", ln(a))

    elif choice=="12":
        for h in history: print(h)

else:
    print("Invalid!")


