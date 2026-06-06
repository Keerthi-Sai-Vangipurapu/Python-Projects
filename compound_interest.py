n=int(input("Enter: "))

principle=0
time=0
rate=0

while principle<=0:
    principle=float(input("enter principle amount:"))
    if principle<=0:
        print(f"Principle amount cant be less than or equal to 0.")

while rate<=0:
    rate=float(input("enter rate:"))
    if rate<=0:
        print(f"Rate cant be less than or equal to 0.")

while time<=0:
    time=float(input("enter Time:"))
    if time<=0:
        print(f"Time cant be less than or equal to 0.")

Total= principle * pow(1 + (rate/n),time)
print(f"Balance after {time} year/s: ${Total:.2f}")