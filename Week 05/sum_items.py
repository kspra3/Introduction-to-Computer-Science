"""
Code by Nabil Ahmed
Task 1
"""

#Reading in the size of the list
size= int(input("Enter size of the list: "))
list = [0] * size
#putting items into the list
for i in range(size):
    list[i] = int(input("Enter Values: "))


def sum_items(a_list):
    """
    function return the sum of the list
    :param: a_list is a numeric list
    :return:sum of the list
    Exception: None
    Precondition: None
    :complexity: Best Case : O(1)  :Worst Case:O(n)
    where n is the size of the list
    """
    assert len(a_list)>=0,"Length of List cannot be negative"
    sum = 0
    if len(a_list) == 0:
        return sum
    else:
        for i in range(len(a_list)):
            sum += a_list[i]
        return sum

print(sum_items(list))