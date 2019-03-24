# python3
import random

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_first = 0
    max_second = 0
    for first in range(n):
        if numbers[first] > numbers[max_first]:
            max_first = first
            
    if max_first == 0:
        max_second = 1

    for second in range(n):
        if second != max_first and numbers[second] > numbers[max_second]:
            max_second = second
    
    return numbers[max_first] * numbers[max_second]

def swap(numbers, num1, num2):
    numbers[num1], numbers[num2] = numbers[num2], numbers[num1]
    return numbers

def max_pairwise_product_swap(numbers):
    n = len(numbers)
    index = 1

    for first in range(n):
        if numbers[first] > numbers[index]:
            index = first
    
    numbers = swap(numbers, index, n - 1)
    
    index = 1
    
    for second in range(n - 1):
        if numbers[second] > numbers [index]:
            index = second
    
    numbers = swap(numbers, index, n - 2)

    return numbers[n - 1] * numbers [n - 2]

if __name__ == '__main__':
    #input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    array_size = input_numbers[0]
    max_number = input_numbers[1]

    while True:
        input_numbers = []
        for i in range(array_size):
            input_numbers.append(random.randint(1, max_number))

        print(input_numbers)
        result1 = max_pairwise_product_fast(input_numbers)
        result2 = max_pairwise_product_swap(input_numbers)

        if result1 == result2:
            print("OK")
        else:
            print("Wrong answer: " + str(result1) + " " + str(result2))
            break
