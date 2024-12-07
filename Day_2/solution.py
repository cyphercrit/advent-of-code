class Solution:
    def is_safe_report(self, report: list) -> bool:
        increasing = True
        if report[1] - report[0] < 0:
            increasing = False
        
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]

            if (diff <= 0 and increasing) or (diff >= 0 and not increasing) or abs(diff) > 3:
                return False
        
        return True

    def safe_reports(self, input_file: str) -> int:
        num_safe = 0

        with open(input_file, 'r') as file:
            for line in file:
                level_list = list(map(int, line.split()))

                num_safe += self.is_safe_report(level_list)
        
        return num_safe
    
    # this probably isn't entirely optimal
    def somewhat_safe_reports(self, input_file: str) -> int:
        num_safe = 0

        with open(input_file, 'r') as file:
            for line in file:
                level_list = list(map(int, line.split()))
                if not self.is_safe_report(level_list):
                    for i in range(len(level_list)):
                        if self.is_safe_report(level_list[:i] + level_list[i+1:]):
                            num_safe += 1
                            break
                else:
                    num_safe += 1
        
        return num_safe

if __name__ == "__main__":
    solution = Solution()
    print(f'Number of Safe Reports: {solution.safe_reports("input.txt")}')
    print(f'Number of Somewhat Safe Reports: {solution.somewhat_safe_reports("input.txt")}')