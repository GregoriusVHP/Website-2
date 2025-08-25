import time
from tqdm import tqdm

def main():
    print()
    print("\t Hello, welcome to the store!")
    print()
    time.sleep(0.2)
    x = int(input(""" what do you want to buy?\n
1. Machiato\n
2. Banana Shake\n
3. Orange Punch\n
4. Chunky Bar\n\n
(please select the number of the item you want to buy): """))
    
    if x == 1:
        print("\nYou have selected Machiato")
        time.sleep(2)
        print("Your order will be ready in 5 minutes")
        for _ in tqdm(range(int(100)),):
            time.sleep(0.7)
        print("Your order is ready!\n")
    elif x == 2:
        print("\nYou have selected Banana Shake")
        time.sleep(2)
        print("Your order will be ready in 5 minutes")
        for i in tqdm(range(int(100))):
            time.sleep(0.18)
        print("Your order is ready!\n")
    elif x == 3:    
        print("\nYou have selected Orange Punch")
        time.sleep(2)
        print("Your order will be ready in 5 minutes")
        for i in tqdm(range(int(100))):
            time.sleep(0.25)
        print("Your order is ready!\n")
    elif x == 4:
        print("\nYou have selected Chunky Bar")
        time.sleep(2)
        print("Your order will be ready in 5 minutes")
        for i in tqdm(range(int(100))):
            time.sleep(0.5)
        print("Your order is ready!\n")
    else:
        print("\nInvalid selection. Please try again.")
        time.sleep(0.5)
        print("Redirecting to the main menu...")
        time.sleep(0.5)
        main()
    
def looping():
    while True:
        z = str(input("\nmau pesan lagi? y/n: "))
        if z == "y" or z == "Y":
            main()
            print()
        elif z == "n" or z == "N":
            print("Thank you for your order!")
            return  # Add a return statement to exit the function
        else:
            print("Invalid input. Have a nice day!")
            return  # Add a return statement to exit the function
 
main()
looping()