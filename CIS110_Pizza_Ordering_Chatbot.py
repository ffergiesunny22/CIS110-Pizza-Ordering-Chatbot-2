userName = input("\nEnter your name:  ")
if userName.lower()== "ffergiesunny22":
    print(f"\Hello,{userName}. Pleasure to serve you!")
else:
    print(f"\nHello, {userName}. Nice to meet you!")
name = input("\nEnter your name: ")
print(f"\nHello, ffergiesunny22. Nice to meet you")
size = input("\nWhat size do you want? Enter small, medium, or large:  ")
flavor = input("\nEnter the flavor of pizza:  ")
crustType = input("\nWhat type of crust do you want:  ")
quantity = input("\nHow many of these do you want to order? Enter a numeric value:  ")
quantity = int(quantity)
method = input("\nIs this carry out or delivery:  ")
if method.lower() == "delivery":
    deliveryFee = 5
else: 
    deliveryFee = 0
salesTax = 1.1
if size.lower() == "small":
    pizzaCost = 8.99
elif size.lower() == "medium":
    pizzaCost = 14.99
elif size.lower() == "large":
    pizzaCost = 17.99
total = quantity * pizzaCost * salesTax + deliveryFee

print("*" * 10)  # Line 15, fixed
print(f"Thank you, {name}, for your order.")
print(f"Your {quantity} {size} {flavor} pizza(s) with {crustType} crust costs ${total:.2f}")  # Line 18, fixed
if total >= 50:
    print("\nCongratulations! You've been awarded a $10 Off coupon for your next order.")
else:
    print("\nOrder over $50 will receive a free $10 Off coupon!")
print("*" * 10)
