cart = {}

while True:
    choice = input("add/remove/show/total/exit: ").lower()

    if choice == "add":
        name = input("item: ")
        price = float(input("price: "))
        qty = int(input("quantity: "))
        if name in cart:
            cart[name][1] += qty
        else:
            cart[name] = [price, qty]

    elif choice == "remove":
        name = input("item: ")
        if name in cart:
            del cart[name]

    elif choice == "show":
        for name, (price, qty) in cart.items():
            print("Item   qty  price  Total")
            print(name, qty, price, qty * price)

    elif choice == "total":
        print(sum(price * qty for price, qty in cart.values()))

    elif choice == "exit":
        break