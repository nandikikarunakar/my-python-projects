import random
import hangmanpics
import booknames
lives=6
print("""                                  
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     """)
choosen_name=random.choice(booknames.books).lower()

display=[]
for i in range(len(choosen_name)):
    display.append("_")
print(display) 

gameover=False

while not gameover:
    guessed_letter=input("Guess a letter:").lower()
    for position in range(len(choosen_name)):
        letter = choosen_name[position]
        if(letter == guessed_letter):
            display[position]=guessed_letter
            print(display)
    if(guessed_letter not in choosen_name):
        lives-=1
        if(lives==0):
            gameover=True
            print("You lose,Game Over.")        
    if '_' not in display:
        gameover=True
        print("You won the game.")
    print(hangmanpics.Hangman_pics[lives])
    print(f"Only {lives} lives left.")
print(f"Your word is {choosen_name}.\nYou guessed it right!")
    