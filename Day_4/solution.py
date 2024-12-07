class Solution:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.board = []

        with open(self.input_file, 'r') as file:
            for line in file:
                self.board.append(line.split())
        
        self.rows = len(self.board)
        self.cols = len(self.board[0])

    def check_index(self, row_index: int, col_index: int, dr: int, dc: int) -> int:
        pass
    
    def find_matches_of_index(self, row_index: int, col_index: int) -> int:
        num_found = 0

        directions = [
            (-1, 0), # up
            (1, 0), # down
            (0, -1), # left
            (0, 1), # right
            (1, 1), # down-right
            (1, -1), # down-left
            (-1, 1), # up-right
            (-1, -1), # up-left
        ]

        for dr, dc in directions:
            pass
            
        return num_found
    
    def find_all_matches(self) -> int:
        total_found = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == "X":
                    total_found += self.find_matches_of_index(row, col)
        
        return total_found

if __name__ == "__main__":
    solution = Solution("./data/input_small.txt")
    solution.find_matches_of_index(1,2)
