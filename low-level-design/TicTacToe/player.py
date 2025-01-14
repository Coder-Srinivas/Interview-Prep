from collections import defaultdict

class Player:

    def __init__(self, winSize):
        self.winSize = winSize
        self.row = defaultdict(int)
        self.col = defaultdict(int)
        self.diagonal = 0
        self.reverse_diagonal = 0
    
    def addRow(self, row):
        self.row[row] += 1
        if self.row[row] == self.winSize:
            return True
        return False
    
    def addCol(self, col):
        self.col[col] += 1
        if self.col[col] == self.winSize:
            return True
        
        return False
    
    def addDiagonal(self, row, col):
        if row == col:
            self.diagonal += 1
        
        if self.diagonal == self.winSize:
            return True
        return False
    
    def addReverseDiagonal(self, row, col):
        if col == self.winSize - row - 1:
            self.reverse_diagonal += 1

        if self.reverse_diagonal == self.winSize:
            return True

        return False