print("Select your ride")
print("1.Bike")
print("2. Car")
choice = int(input("Enter your choice"))
if(choice == 1):
    print("What type of bike?")
    print("1. Scotty\n")
    print("2. Scooter")
    bike = int(input("Enter your choice"))
    if bike == 1:
     print("You have selected scotty")
    else:
     print("your have selected scooter")
elif(choice == 2):
    print("what type of car?")
    print("1. sedan")
    print("2. xuv")
    car = int(input("enter your choice"))
    if car ==1:
     print("you have selected sedan")
    else:
     print("you have selected xuv")
else:
 print("wrong choice!")