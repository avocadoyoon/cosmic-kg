print("Welcome to the Interplanetary Weight Calculator! 🚀")
print("Enter the number for the planet you want to visit:")
print("1. Mercury")
print("2. Venus")
print("3. Mars")
print("4. Jupiter")
print("5. Saturn")
print("6. Uranus")
print("7. Neptune")

# User input
e_weight = float(input("🌍 What is your Earth weight (kg)? "))
planet = int(input("🪐 Choose your planet number (1-7): "))

# Calculate weight based on gravity factors
if planet == 1:
    d_weight = e_weight * 0.38  # Mercury
elif planet == 2:
    d_weight = e_weight * 0.91  # Venus
elif planet == 3:
    d_weight = e_weight * 0.38  # Mars
elif planet == 4:
    d_weight = e_weight * 2.53  # Jupiter
elif planet == 5:
    d_weight = e_weight * 1.07  # Saturn
elif planet == 6:
    d_weight = e_weight * 0.89  # Uranus
elif planet == 7:
    d_weight = e_weight * 1.14  # Neptune
else:
    d_weight = None
    print("❌ Invalid planet number! Please run the program again.")

# Output result
if d_weight is not None:
    print(f"✨ On this planet, you would weigh about {round(d_weight, 2)} kg!")

