import random

def randomize_board(self):
  self.display = ""
  for i in range(len(self.board)):
    random_letter = self.board[i][random.randint(0, 5)]
    self.letters_showing[i].clear()
    self.letters_showing[i].append(random_letter)
    self.display += f"{random_letter} "
    if (i+1) % 4 == 0:
      self.display += "\n"
      
      
class BoggleBoard:
  
  def __init__(self):
    self.board = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    self.display = ""
    self.letters_showing = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(16):
      for j in range(6):
        self.board[i].append('_')
    randomize_board(self)
      
  def shake(self):
    if '_' in self.board[0]:
      for i in range(16):
        self.board[i].clear()
        for j in range(6):
          random_letter = chr(random.randint(65, 90))
          if random_letter == "Q":
            random_letter = "Qu"
          self.board[i].append(random_letter)
    randomize_board(self)      
      
  def include_word(self, word):  
    temp = ""
    #check rows for word
    for i in range(16):
      temp += self.letters_showing[i][0]
      if temp == word or temp[::-1] == word:
        return True
      if (i+1) % 4 == 0:
        temp = ""
    # check columns for word    
    for i in range(4):
      for j in range(0, 16, 4):
        temp += self.letters_showing[j+i][0]
        if temp == word or temp[::-1] == word:
          return True
      temp = ''
    # check diagonal left to right for word
    for i in range(0, 16, 5):
      temp += self.letters_showing[i][0]
      if temp == word or temp[::-1] == word:
        return True
    # check diagonal right to left
    for i in range(3, 13, 3):
      temp += self.letters_showing[i][0]
      if temp == word or temp[::-1] == word: 
        return True
    return False  
          
  
game = BoggleBoard()
print(game.display)
game.shake()
print(game.display)
print(game.include_word('SHOE'))