model = input("Enter the aircraft model: \n")

match model:
    case "B777" | "B787" | "B767":
        print("Boeing wide body airliner")
    case "A320" | "A219" | "A318":
        print("Airbus narrow body airliner")
    case "Dash-8":
        print("bombardiar prob airliner")
    case _:
        print("Unknown!")
        