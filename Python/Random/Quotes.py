import random
import time

q = [
        ["The greatest glory in living lies not in never falling, but in rising every time we fall.","Nelson Mandela"],
        ["The way to get started is to quit talking and begin doing.","Walt Disney"],
        ["Life is what happens when you're busy making other plans.","John Lennon"],
        ["The purpose of our lives is to be happy.","Dalai Lama"],
        ["Get busy living or get busy dying.","Stephen King"],
        ["You only live once, but if you do it right, once is enough."],
        ["In three words I can sum up everything I've learned about life: it goes on.","Robert Frost"],
        ["To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment.","Ralph Waldo Emerson"],
        ["The only impossible journey is the one you never begin.","Tony Robbins"],
        ["Life is either a daring adventure or nothing at all. ","Helen Keller"],
        ["The future belongs to those who believe in the beauty of their dreams.", "- Eleanor Roosevelt"],
        ["It does not matter how slowly you go as long as you do not stop. ", "Confucius"],
        ["You miss 100 percent of the shots you don't take.", "Wayne Gretzky"],
        ["The best way to predict the future is to create it.","Peter Drucker"],
        ["Success is not final, failure is not fatal: It is the courage to continue that counts.", "Winston Churchill"],
        ["Believe you can and you're halfway there.","Theodore Roosevelt"]
    ]

def main():
    print("="*50)
    print("\tWelcome to the Quote Generator!")
    print("="*50)
    print()
    rounds = int(input("How many quotes would you like to see? "))

    if rounds >= 1:
        print("Here are some more quotes for you:")
        get_random_quote(rounds)
    else:
        print("No quotes to show. Goodbye!")
        exit()

def get_random_quote(rounds):
    for i in range(rounds):
        quote = random.choice(q)
        random.shuffle(quote)
        print(f"\n{quote[0]} - \n {quote[1]}\n")
while True:
    main()
    time.sleep(5)

