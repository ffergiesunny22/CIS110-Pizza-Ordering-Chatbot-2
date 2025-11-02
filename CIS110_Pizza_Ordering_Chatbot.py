print("Hello, my name is Faith your virtual assistant. I will help you order a pizza")
print(" I am going to ask you a few questions. After typing an answer,")
name = input("\nEnter your name: ")
print(f"\nHello, Gwen. Nice to meet you")
size = input("\nWhat size do you want? Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
crustType = input("\nWhat type of crust do you want:  ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value:  ")
quantity = int(quantity)
input("\nIs this carry out or delivery:  ")

salesTax = 1.1
pizzaCost = 14.99
total = quantity * pizzaCost * salesTax

print("*" * 10)  # Line 15, fixed
print(f"Thank you, {name}, for your order.")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:.2f}")  # Line 18, fixed
print("*" * 10)
