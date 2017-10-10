# def even_number_of_evens(nums):
#     number_of_evens = sum([1 for n in nums if n % 2 == 0])
    
#     if number_of_evens == 0:
#         return False
    
#     if number_of_evens % 2 == 0:
#         return True
#     else:
#         return False

def even_number_of_evens(nums):
    evens = 0
    
    for num in nums:
        if num % 2 == 0:
            evens += 1
    
    if evens == 0:
        return False
        
    return evens % 2 == 0
           
    

    

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"
print("All tests passed")