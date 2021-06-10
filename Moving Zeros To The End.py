# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

def move_zeros(array):
    final_list = []
    y = 0
    for i in array:
        if type(i) == bool:
            final_list.append(i)
            y += 1
        if i != 0 or (i != 0 and type(i) == bool) or (i !=0 and type(i) is not None):
            final_list.append(i)
            y += 1
        else:
            pass
    for x in range(len(array) - y):
        final_list.append(0)
    return final_list

print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]))
move_zeros(["a",0,0,"b","c","d",0,1,0,1,0,3,0,1,9,0,0,0,0,9])
move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])
move_zeros([0,1,None,2,False,1,0])