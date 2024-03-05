class Player:
    def __init__(self):
        self.name = input("Please enter your name: ")
        self.score = 0
        self.char = input("Choose your symbol: X or O")

    @property 
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name

    @property 
    def score(self):
        return self.__score 
    @score.setter
    def score(self,value):
        if value < 0:
            raise ValueError("Geen geldige score")
        else :
            self.__score = value

    @property
    def char(self):
        return self.__char
    @char.setter
    def char(self,symb):
        if symb.lower() in "xo":
            self.__char = symb.upper()
        else :
            raise ValueError("Da kan ni")
    
class Board : 
    def __init__(self):
        self.clear_board()
        

    def clear_board(self):
        self.__board = [["_"] *7]*6   

    def insert_token(self, userinput, player):
        colindex = int(userinput) - 1 
        for rowidx in range(len(self.__board)):
            if self.__board[rowidx][colindex] == "_":
                 continue
            else:
                self.__board[rowidx -1][colindex] == player.char
                 
                

