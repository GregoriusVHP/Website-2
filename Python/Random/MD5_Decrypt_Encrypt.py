import hashlib
import time


def Decrypt():
    # md5 decrypting brute force

    x = str(input("Enter hash: "))
    wordlist = 'rockyou.txt'

    for password in open(wordlist, 'r', encoding='utf-8', errors='ignore').readlines():  
        time.sleep()  # Adding a delay to avoid overwhelming the CPU

        if hashlib.md5(password.strip().encode()).hexdigest() == x:
            print(f"Password found: {password.strip()}")
            break
        else:
            print("Im terribly sorry, password not found.")
            break
        

   

def Encrypt():
    p = input("Enter password: ")
    # md5 hashing
    md5 = hashlib.md5()
    md5.update(p.encode('utf-8'))
    digest = md5.hexdigest()
    print(f"this is your hashed password: {digest} \n\n")
        

def main():
    print("Welcome to the hashing program!")
    print("1. Hash a password")
    print("2. Decrypt a password")
    print("3. Exit \n\n")

    choice = str(input("Enter your choice: "))

    if choice == '1':
        Encrypt()
    elif choice == '2':
        Decrypt()
    elif choice == '3':
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
   main()