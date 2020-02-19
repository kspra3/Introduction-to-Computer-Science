"""
K. Sharsindra Pratheen
Computer Science, Monash University
"""
import random
import timeit

def sum_items(a_list):
    """
    sum_items return the sum of the list
    :param a_list:
    :return:sum of the list
    :complexity: Best Case : O(1)  :Worst Case:O(n)
    """
    assert len(a_list) >= 0, "Length of List cannot be negative"
    sum = 0
    if len(a_list) == 0:
        return sum
    else:
        for i in range(len(a_list)):
            sum += a_list[i]
        return sum

def time_sum_items(a_list):
    start = timeit.default_timer()
    sum_items(a_list)
    taken = timeit.default_timer() - start
    return taken

def table_time_sum_items():
    list1 = []
    list2 = []
    n = 2
    for i in range(1,11,1):
        n2 = n**i
        list1.append(n2)

    for i in range(len(list1)):
        variable = list1[i]
        new_list = []
        random.seed(789)
        for j in range(variable):
            #creates a list of n items then sums it up
            rand = random.random()
            new_list.append(rand)
        a = time_sum_items(new_list)
        list2.append(a)
    print(list2)

table_time_sum_items()