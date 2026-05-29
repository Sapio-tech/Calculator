import math
from Scient import *

history = []

def show_menu():
    print("\n=== Scientific Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Log (base 10)")
    print("11. Ln (natural log)")
    print("12. View History")
    print("0. Exit")

while True:
  show_menu()
  choice = input("Choose option: ")

  if choice == "0":
      print("Goodbye!")
      break
  elif choice in ["1","2","3","4","5"]:
    a = float(input("Enter first number: "))
    b = float(input(" Enter second number:"))
    if choice == "1": result = add(a, b)
    elif choice == "2": result = subtract(a, b)
    elif choice == "3": result = multiply(a, b)
    elif choice == "4": result = divide(a, b)
    elif choice == "5": result = power(a, b)
elif choice in ["6","7","8","9","10","11"]:
    a = float(input("Enter number:"))
    if choice == "6": result = sqrt(a)
    elif choice == "7": result = sin(a)
    elif choice == "8": result = cos(a)
    elif choice == "9": result = tan(a)
    elif choice == "10": result = log(a)
    elif choice == "11": result = ln(a)
elif choice == "12":
    print("\n--- History ---")
    for h in history: print(h)
    continue
else:
    print("Invalid option!")
    continue
  
print(f"Result:{result}")
history.append(f"Option {choice}: {result}")

    
