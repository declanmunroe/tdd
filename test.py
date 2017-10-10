# def count_upper_case(message):
#     return sum([1 for c in message if c.isupper()]) #this is called a list comprehensio
def count_upper_case(message):
    upper = sum([2 for c in message if c.isupper()])
    lower = sum([1 for c in message if c.islower()])
    space = sum([5 for c in message if c == " "])
    result = upper + lower + space
    return result
    
assert count_upper_case("") == 0, "Empty String"
assert count_upper_case(" ") == 5, "Space String"
assert count_upper_case("A") == 2, "One upper case"
assert count_upper_case("ABCa") == 7, "One upper case"
assert count_upper_case("Ba") == 3, "One lower case"
assert count_upper_case("a") == 1, "One lower case"
assert count_upper_case("aB") == 3, "One lower case"
assert count_upper_case("$%^&") == 0, "Only special caracters"
    
print(count_upper_case("DeclAn MArk James Munroe"))

print("All tests pass")

# def count_upper_case(message):
#             count = 0
#             for c in message:
#                 if c.isupper():
#                     count += 1
#             return count


# assert count_upper_case("") == 0, "Empty String"
# # assert count_upper_case(123) == 0, "Fail Number"
# assert count_upper_case("A") == 1, "One upper case"
# assert count_upper_case("ABCa") == 3, "One upper case"
# assert count_upper_case("Ba") == 1, "One lower case"
# assert count_upper_case("a") == 0, "One lower case"
# assert count_upper_case("aB") == 1, "One lower case"
# assert count_upper_case("$%^&") == 0, "Only special caracters"

# print(count_upper_case("DeclAn MArk James Munroe"))

# print("All tests pass")