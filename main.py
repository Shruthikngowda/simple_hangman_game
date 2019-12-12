import sys

secret_word = "beaful"
no_of_guesses = 10
alphabet_set = "abcdefghijklmnopqrstuvwxyz"
print("YOur secret word contains ", len(secret_word) , " letters")
to_show_user = []
for i in secret_word:
    to_show_user.append("-")

while no_of_guesses > 0:
  if '-' in to_show_user:
    user_guess = input("Please enter a word ").lower()
    no_of_guesses = no_of_guesses - 1
    if len(user_guess) > 1:
      print("Error! Only 1 character allowed!")
      sys.exit
    else:
      if not user_guess in alphabet_set:
        print("Error! Only letters a-z allowed!")
        sys.exit

  #
    if user_guess in secret_word:
      for x in range(len(secret_word)):
        if secret_word[x] == user_guess:
          to_show_user[x] = user_guess
      print("Guessed correctly")
    else:
      print("Wrong guess !")
    print("the secret word now is ",to_show_user)
  else:
    no_of_guesses = -1
    print("Hurray! You won !")
    sys.exit()