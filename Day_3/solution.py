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
    
    def find_mul_strict(self, input_file: str) -> int:
        product = 0

        with open(input_file, 'r') as file:
            corrupted_file = file.read()

        corrupted_file = re.sub(r"don't\(\).*?(?=do\(\)|$)", "", corrupted_file, flags=re.DOTALL)    
        matches = re.findall(r'mul\((\d+),(\d+)\)', corrupted_file)

        for op in matches:
            num1, num2 = map(int, op)
            product += num1 * num2    

        return product

if __name__ == "__main__":
    solution = Solution()
    print(f'Total Product: {solution.find_mul("input.txt")}')
    print(f'Total Product (strict): {solution.find_mul_strict("input.txt")}')