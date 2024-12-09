class Solution:
    def __init__(self, input_file: str):
        self.page_map = {}
        self.page_orders = []
        
        with open(input_file, 'r') as file:
            reached_newline = False

            for line in file:
                line = line.strip()
                if reached_newline:
                    self.page_orders.append([int(x) for x in line.split(",")])
                elif not line:
                    reached_newline = True
                    continue
                else:
                    x, y = line.split("|")
                    self.page_map[int(x)] = int(y)

if __name__ == "__main__":
    solution = Solution("./data/input_small.txt")
    print(solution.page_map)
    print(solution.page_orders)