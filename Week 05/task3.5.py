"""
K. Sharsindra Pratheen
Computer Science, Monash University
"""
import timeit
import random
a_list = [5,6,2,3,1]

def shaker_sort(a_list):
    n = len(a_list)
    for i in range(n-1,0,-1):
        for j in range(n-1,0,-1):
            if a_list[j] < a_list[j-1]:
                swap(a_list,j,j-1)
    #return a_list

def swap(the_list,i,j):
    the_list[i],the_list[j] = the_list[j], the_list[i]


def time_shaker_sort(a_list):
    start = timeit.default_timer()
    shaker_sort(a_list)
    taken = timeit.default_timer() - start
    return taken
"""
def table_time_shaker_sort():
    list1 = []
    list2 = []
    n = 2
    for i in range(1,11,1):
        n2 = n**i
        list1.append(n2)

    for i in range(len(list1)):
        variable = list1[i]
        new_list = []

        #100 lists
        #for each list go through shaker sort one seed
        random.seed(j)
        for j in range(variable):

            rand = random.random()
            new_list.append(rand)
        a = time_shaker_sort(new_list)
        list2.append(a)
    print(list2)

"""


#table_time_shaker_sort()

def table_avg_time_shaker_sort():
    for i in range(1,10):
        n = 2**i
        total = 0
        for k in range(100):
            a_list = []
            random.seed(k + 289)
            for j in range(n):
                a_list.append(random.random)
            total = total + time_shaker_sort(a_list)
        total = total / 100
        return total


print(table_avg_time_shaker_sort())