import sys

secret_word = "beaful"
no_of_guesses = 10
alphabet_set = "abcdefghijklmnopqrstuvwxyz"
print("YOur secret word contains ", len(secret_word) , " letters")
to_show_user = []
repeated_letters = []
for i in secret_word:
    to_show_user.append("-")

while no_of_guesses > 0:
    user_guess = input("Please enter a letter ").lower()
    no_of_guesses = no_of_guesses - 1
    if len(user_guess) > 1:
      print("Error! Only 1 character allowed!")
      sys.exit
    elif user_guess not in alphabet_set:
      print("Error! Only letters a-z allowed!")
      sys.exit
    elif user_guess in repeated_letters:
      print("letter already used")
    else:
      repeated_letters.append(user_guess)
      if user_guess in secret_word:
        for x in range(len(secret_word)):
          if secret_word[x] == user_guess:
            to_show_user[x] = user_guess
        print("Guessed correctly")
        if not '-' in to_show_user:
          no_of_guesses = -1
          print("Hurray! You won !")
          sys.exit()
      else:
        print("Wrong guess !")

    #print(no_of_guesses)
    if no_of_guesses != 0:
      print("the secret word now is ",to_show_user)
    

print("Sorry, you lost the game ")
