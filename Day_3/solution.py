import re

class Solution:
    def find_mul(self, input_file: str) -> int:
        product = 0

        with open(input_file, 'r') as file:
            for line in file:
                matches = re.findall(r'mul\((\d+),(\d+)\)', line)
                for op in matches:
                    num1, num2 = map(int, op)
                    product += num1 * num2
        
        return product

if __name__ == "__main__":
    solution = Solution()
    print(f'Total Product: {solution.find_mul("input.txt")}')