from player import Player
from typing import List
class Board:

    def __init__(self, n, players):
        self.total_players = players
        self.players: List[Player] = []
        self.board = [[' ' for _ in range(n)] for _ in range(n)]
        self.n = n
        self.winner = None
        self.index = 0
        self.total_moves = 0
        
        for _ in range(players):
            self.players.append(Player(n))
    
    def move(self, row, col):
        index = self.index
        if index < 0 or index >= len(self.players):
            print("Player does not exist")
            return
        if row >= self.n or col >= self.n or row < 0 or col < 0:
            print("Incorrect Input")
            return
        player: Player = self.players[index]
        if self.winner:
            print(f"Player f{self.winner} already won the game")
            return
        if self.board[row][col] != ' ':
            print("That position is already occupied. Try again")
            return
        self.board[row][col] = index
        
        if player.addRow(row) or player.addCol(col) or player.addDiagonal(row, col) or player.addReverseDiagonal(row, col):
            self.winner = index
            print(f"Player {index} wins")
        self.index = (self.index + 1) % self.total_players
        self.total_moves += 1
        if self.total_moves == self.n * self.n:
            print("Game is a draw")
            self.winner = "Draw"
    
    def printBoard(self):
        print("    ", end="")
        for col in range(self.n):
            print(f"{col}   ", end="")
        print()

        for i in range(self.n):
            print("   " + "+---" * self.n + "+")
            print(f"{i}  |", end="")
            for j in range(self.n):
                print(f" {self.board[i][j]} |", end="")
            print()
        print("   " + "+---" * self.n + "+")


    
    def reset(self):
        self.board = [[' ' for _ in range(self.n)] for _ in range(self.n)]
        self.players: List[Player] = []
        for _ in range(self.total_players):
            self.players.append(Player(self.n))
        self.winner = None
        self.total_moves = 0