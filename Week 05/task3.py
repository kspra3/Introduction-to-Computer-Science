"""
K. Sharsindra Pratheen
Computer Science, Monash University
"""
import timeit
import random
a_list = [5,6,2,3,1]

def shaker_sort(a_list):
    """
    function uses shaker sort to sort the list
    :param: a_list is a numeric list
    :return:sorted list
    Exception: None
    Precondition: None
    :complexity: Best Case : O(n)  :Worst Case:O(n2)
    where n is the size of the list
    """
    n = len(a_list)
    for i in range(n-1,0,-1):
        for j in range(n-1,0,-1):
            if a_list[j] < a_list[j-1]:
                swap(a_list,j,j-1)
    #return a_list

def swap(the_list,i,j):
    """
    function swaps elements in a list
    :param: the_list, the position of the two elements to be swapped
    :return:None
    Exception: None
    Precondition: None
    :complexity: Best Case : O(1)  :Worst Case:O(1)
    No loops
    """
    the_list[i],the_list[j] = the_list[j], the_list[i]


def time_shaker_sort(a_list):
    """
    function measures the time elapsed
    when running the shaker sort function
    :param: a_list
    :return:Time Taken
    Exception: None
    Precondition: None
    :complexity: Best Case : O(1)  :Worst Case:O(1)
    No loops
    """
    start = timeit.default_timer()
    shaker_sort(a_list)
    taken = timeit.default_timer() - start
    return taken

def table_time_shaker_sort():
    """
    function creates a random list by using the imported
    random python module
    :param: None
    :return: The list containing the
    Exception: None
    Precondition: None
    :complexity: Best Case : O(n2)  :Worst Case:O(n2)
    Nested loops which has no way to finish execution earlier
    """
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
            rand = random.random()
            new_list.append(rand)
        a = time_shaker_sort(new_list)
        list2.append(a)
    print(list2)

table_time_shaker_sort()
