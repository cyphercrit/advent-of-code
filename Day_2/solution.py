class Solution:
    def safe_reports(self, input_file: str) -> int:
        num_safe = 0

        with open(input_file, 'r') as file:
            for line in file:
                level_list = list(map(int, line.split()))
                num_to_add = 1

                # assumes there are at least two elements in each line
                increasing = True
                if level_list[1] - level_list[0] < 0:
                    increasing = False

                for i in range(1, len(level_list)):
                    diff = level_list[i] - level_list[i-1]
                    
                    if (diff <= 0 and increasing) or (diff >= 0 and not increasing) or abs(diff) > 3:
                        num_to_add = 0
                        break

                num_safe += num_to_add
        
        return num_safe
    
    # needs work
    def somewhat_safe_reports(self, input_file: str) -> int:
        num_safe = 0

        with open(input_file, 'r') as file:
            for line in file:
                level_list = list(map(int, line.split()))
                num_to_add = 1
                violations = 0

                # assumes there are at least two elements in each line
                increasing = True
                if level_list[1] - level_list[0] < 0:
                    increasing = False

                for i in range(1, len(level_list)):
                    diff = level_list[i] - level_list[i-1]
                    
                    if (diff <= 0 and increasing) or (diff >= 0 and not increasing) or abs(diff) > 3:
                        if violations == 1:
                            num_to_add = 0
                            break
                        else:
                            violations = 1

                num_safe += num_to_add
        
        return num_safe

if __name__ == "__main__":
    solution = Solution()
    print(f'Number of Safe Reports: {solution.safe_reports("input.txt")}')
    print(f'Number of Somewhat Safe Reports: {solution.somewhat_safe_reports("smaller_input.txt")}')