# def sumList(list):
#     total = 0
#     for l in list:
#         total += l
#     return total
    
def sumList(list):
    if list == []:
        return 0
    return list[0] + sumList(list[1:])
    
print(sumList([1,20,3,4,5,6,7,8,9,10]))