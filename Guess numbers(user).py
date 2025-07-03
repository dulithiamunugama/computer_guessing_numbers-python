import random
low = 1
high = 10
comment = ""
while True:
    guess  = random.randint(low, high)
    print(f"Comuter guess : {guess}")
    comment = input("Enter low(l) or high(h) or correct(c): ")
    if comment == "c":
        print("Compurt guessed the corrct number. 🥳") 
        break 
    elif comment == "h":
        high = guess-1
    elif comment == "l":
        low = guess+1
          
 
