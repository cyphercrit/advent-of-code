class Solution:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.board = []

        with open(self.input_file, 'r') as file:
            for line in file:
                line = line.replace("\n", "") # gets rid of the problematic newline character
                self.board.append(list(line))
        
        self.rows = len(self.board)
        self.cols = len(self.board[0])

    def check_index(self, row_index: int, col_index: int, dx: int, dy: int) -> int:
        col_bounds, row_bounds =  col_index + (dx * 3), row_index + (dy * 3) 
        if col_bounds > self.cols - 1 or col_bounds < 0 or row_bounds > self.rows - 1 or row_bounds < 0:
            return 0
        
        rest_of_word = "MAS"
        for i in range(len(rest_of_word)):
            row_index += dy
            col_index += dx
            if self.board[row_index][col_index] != rest_of_word[i]:
                return 0
        
        return 1
    
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

        for dx, dy in directions:
            num_found += self.check_index(row_index, col_index, dx, dy)
            
        return num_found
    
    def find_all_matches(self) -> int:
        total_found = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == "X":
                    total_found += self.find_matches_of_index(row, col)
        
        return total_found
    
    def check_cross(self, row_index: int, col_index: int) -> int:
        if row_index < 1 or row_index > self.rows - 2 or col_index < 1 or col_index > self.rows - 2:
            return 0
        
        # four corners
        indices = [
            (row_index + 1, col_index + 1),
            (row_index - 1, col_index - 1),
            (row_index + 1, col_index - 1),
            (row_index - 1, col_index + 1)
        ]

        for i in range(2):
            available_set = {"M", "S"}
            j, k = indices.pop()
            x, y = indices.pop()
            letter1 = self.board[j][k]
            letter2 = self.board[x][y]

            if letter1 not in available_set:
                return 0
            available_set.remove(letter1)

            if letter2 not in available_set:
                return 0
        
        return 1
    
    def find_all_crosses(self) -> int:
        total_found = 0

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == "A":
                    total_found += self.check_cross(row, col)
        
        return total_found

if __name__ == "__main__":
    solution = Solution("./data/input_large.txt")
    print(f'XMAS Matches Found: {solution.find_all_matches()}')
    print(f'X-MAS Cross Matches Found: {solution.find_all_crosses()}')