class Solution:
    def safe_reports(self, input_file: str) -> int:
        num_safe = 0

        with open(input_file, 'r') as file:
            for line in file:
                level_list = map(int, line.split())

                for i in range(len(level_list)):
                    pass
                    
if __name__ == "__main__":
    solution = Solution()
    print(f'Number of Safe Reports: {solution.safe_reports("input.txt")}')