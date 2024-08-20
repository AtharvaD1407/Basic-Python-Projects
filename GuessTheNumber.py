import random as r

num = r.randint(1, 10)
attempt = 1

while True:
    guess_num = int(input("Guess Number: "))

    if guess_num == num:
        if attempt == 1:
          print("God or Wot")
        break
      
    else:
        if guess_num > num:
            print("Guess Lower.")
        else:
            print("Guess Higher!")
        attempt += 1

print(f"Attempts = {attempt}")