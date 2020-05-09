#Yuchen Zheng Csc101
#Final project

#import random
import random


#set image of six tries as a list
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''','''
 +---+
 0   |
     |
     |
    ===   ''','''
 +---+
 0   |
 |   |
     |
    ===   ''','''
 +---+
 0   |
/|   |
     |
    ===   ''','''
 +---+
 0   |
/|\  |
     |
    ===   ''','''
 +---+
 0   |
/|\  |
/    |
    ===   ''','''
 +---+
 0   |
/|\  |
/ \  |
    ===   ''']


#get a random word from myGuessWords file
def get_word():
    with open('myGuessWords.txt','r') as f:
        words = f.readlines()
        num = random.randint(1,len(words))
        #return this word
        return (words[num-1])


#set a for loop to check if user's guess in this word
def check_Character(word, character):
    for c in range(len(word)):
        if word[c] == character:
            return c
    return -1
#set sevral variable for processing the game
def Guess(word):
    count = 0
    rightNum = 0
    out = ['_'for _ in range(len(word) - 1)]
    miss = ''
    guess = ''
    #set a list for store user's guess and result
    guess_dic = []
    game = True

    #set a while lopp for processing the game, check whether win or lost
    while game:
        print(HANGMAN_PICS[count])
        print('Missed letter: ' + miss)
        print(out)
        print('Guess a character')
        character = input().lower()
        guess += character
        check = check_Character(word, character)

        #use if/elis/else condition to check does game should keep or finish
        #and use the return value of check_Character function to check results
        if check == -1 and count < len(HANGMAN_PICS)-2:
            miss += character
            count += 1
        elif count>=len(HANGMAN_PICS)-2:
            print(HANGMAN_PICS[count + 1])
            print('You failed! The letter is '+word.upper())
            game = False
            guess_dic.append(guess)
            guess_dic.append('lost')
        else:
            out[check] = character
            rightNum += 1
        if rightNum == len(word):
            print('You win! The latter is '+word.upper())
            game = False
            guess_dic.append(guess)
            guess_dic.append('won')
            
    #return the list of user's guess and game result       
    return guess_dic

def main():
    print("H A N G M A N")
    output = {}
    word = get_word()
    guess_dic = Guess(word)
    #move the data from list to a dictionary
    output[guess_dic[0]] = guess_dic[1]
    #set a while loop to check if user want to play again
    while input('Do you want to play again? (y/n) ').lower() == 'y':
        word = get_word()
        guess_dic = Guess(word)
        output[guess_dic[0]] = guess_dic[1]
    #put all of the user's guess to an txt from
    with open('myGameResults.txt', 'w') as wf:
        for key, value in output.items():
            wf.write(key)
            wf.write('\r\n')
            wf.write('\r\n')
            wf.write('Game ' + value + '!')
            wf.write('\r\n')
            wf.write('\r\n')

if __name__ == "__main__":
    main()


