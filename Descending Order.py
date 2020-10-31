def descending_order(num):
    num = str(num)
    sorted_num = sorted(num, reverse=True)
    sorted_num1 = ''.join(sorted_num)
    sorted_num1 = int(sorted_num1)
    return sorted_num1

descending_order(0)
