model = input("Enter the plane model\n")

if model == "B737" or model == "B757" or model == "B727":
    print("Boeing, narrow body airliner")
elif model == "A320" or model == "A321" or model == "A319":
    print("Airbus, Narrow body airliner")
elif model == "B787" or model == "B777":
    print("Boeing, Wide body airliner")
elif model == "D8 prob":
    print("Bombardiar Prop airliner")

else:
    print("unknown Model")
    
