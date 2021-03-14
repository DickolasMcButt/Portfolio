num_list = [1, 2, 3, 4, 5]
 
while True:
    answer = input("Guess a number, or type q to quit: ")
    
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("answer must be q or an integer.")
        continue
    if answer in num_list:
        print("You guessed right!")
    else:
        print("You guessed wrong!")