#Weight Calculator

weight=float(input("Enter your Weight: "))
unit=input("Kilograms or Pounds ?(K or L):")

if(unit=="K" or unit=="k"):
    weight*=2.204
    unit="Lbs."
elif(unit=="L" or unit=="l"):
    weight/=2.204
    unit="Kgm"
else:
    print(f"{unit} was not Valid.")

print(f"The Weight: {weight} {unit}")
