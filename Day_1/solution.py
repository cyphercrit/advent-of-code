class Solution:
    '''
    Takes an input file containting two numbers per line and
    sorts each side of the file into two lists, sorts each list,
    and then compares the sum of the total differences between 
    each number, returning that value.
    '''
    def find_total_distance(self, input_file: str) -> int:
        first, second = [], []

        with open(input_file, 'r') as file:
            for line in file:
                num1, num2 = line.split()
                
                first.append(int(num1))
                second.append(int(num2))
        
        first.sort()
        second.sort()

        total_distance = 0
        for num1, num2 in zip(first, second):
            total_distance += abs(num1 - num2)
        
        return total_distance

if __name__ == "__main__":
    solution = Solution()
    print(solution.find_total_distance("input.txt"))
        