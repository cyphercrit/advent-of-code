class Solution:
    def __init__(self, input_file: str):
        self.input_file = input_file

    '''
    Takes an input file containting two numbers per line and
    sorts each side of the file into two lists, sorts each list,
    and then compares the sum of the total differences between 
    each number, returning that value.
    '''
    def find_total_distance(self) -> int:
        first, second = [], []

        with open(self.input_file, 'r') as file:
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
    
    '''
    Reads a file containing pairs of integers and calculates a similarity score.
    The function processes each line in the input file, where each line consists
    of two integers. The first integer is added to a list, and the second integer
    is counted using a dictionary. The similarity score is computed by summing
    the product of each integer from the first list and its corresponding count 
    in the dictionary.
    '''
    def calculate_similarity_score(self) -> int:
        first, second_counter = [], {}

        with open(self.input_file, 'r') as file:
            for line in file:
                num1, num2 = map(int, line.split())

                if num2 in second_counter:
                    second_counter[num2] += 1
                else:
                    second_counter[num2] = 1
                
                first.append(num1)
            
        
        similarity_score = 0
        for num in first:
            if num in second_counter:
                similarity_score += num * second_counter[num]
        
        return similarity_score

if __name__ == "__main__":
    solution = Solution("input.txt")
    print(f'Total Distance: {solution.find_total_distance()}')
    print(f'Similarity Score: {solution.calculate_similarity_score()}')
        