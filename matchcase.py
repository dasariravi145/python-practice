a = int(input("enter the lucky number"))

match a:
    case 1: 
        print("you won the charger")
    case 3:
         print("you won $3")
    case 4:
         print("you won the camera")
    case _:
         print(" better luck next time ")