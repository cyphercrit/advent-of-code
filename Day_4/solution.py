class Solution:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.board = []

        with open(self.input_file, 'r') as file:
            for line in file:
                self.board.append(line.split())
        
        self.rows = len(self.board)
        self.cols = len(self.board[0])

if __name__ == "__main__":
    solution = Solution("./data/input_small.txt")