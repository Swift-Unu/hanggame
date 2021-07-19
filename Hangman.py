import sys
from random_words import RandomWords



class HangGame():
    players=[]
    turns = 5
    r = RandomWords()
    word = r.random_word()
    failed=0
    guesses = ''
    # def _init_(self):
    #     turns = 5
    #     user = len(self.players)

    def inputplayers(self, nrofplayers):
        if 0 < nrofplayers < 5:
            for i in range(1, nrofplayers + 1):
                username = input("Enter username\t" + str(i) + ":")
                self.players.append(username)
            print("Welcome:" + str(self.players)[1:-1])
        elif nrofplayers >= 5:
            print("Too many gamers")
        else:
            print("No gamers, no game")
        return self.players


    def playerturn(self):
        user = len(self.players)
        while user > 0:
            for x in range(0, user):
                print("Player:" + self.players[x])
                guess = input("inputguess:")
                self.correctguess(guess)
                self.guessing()
            break


    def guessing(self):
        for char in self.word:
            if char in self.guesses:
                print(char)
            else:
                print("_")
                self.failed += 1
        return self.failed

    def correctguess(self, guess):
        if self.failed == 0:
            print("You win!")
            print("The word is:", self.word)
        self.guesses += guess
        print(self.guesses)
        if guess not in self.word:
            self.turns -= 1
            print ("Wrong")
            if self.turns == 0:
                print ("Lose")
        return self.turns

    def roundcount(self):
        while self.turns>0:
            for turn in range(1, self.turns+1):
                print("Round:" + str(turn))
                self.playerturn()
            break




    # def gamecountrule(self, ):
    #     #number of turns
    #     turns = 5
    #     while turns > 0:





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numberofplayers = int(input("number of players:"))
    game = HangGame()
    game.inputplayers(numberofplayers)
    #game.playerturn()
    game.roundcount()

    # user = len(game.inputplayers(numberofplayers))
    # print(user)

    # for x in range(0, user):
    #     print("Player:", HangGame.inputplayers(numberofplayers[x]))




    # for i in range(0,4):
    #     usernumber = str(i)
    #     print("Hello player" + usernumber)
    # expected_word = 'gigi'
    # my_new_word = ''
    #
    # for c in expected_word:
    #     while True:
    #         if input('introdu o litera') == c:
    #             my_new_word += c
    #             print(my_new_word)
    #             break
    #         else:
    #             print('mai incearca')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
