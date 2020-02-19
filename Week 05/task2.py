"""
K. Sharsindra Pratheen
Computer Science, Monash University
"""
import timeit

size= int(input("Enter size of the list: "))
list = [0] * size
#putting items into the list
for i in range(size):
    list[i] = int(input("Enter Values: "))

def time_sum_items(a_list):
    start = timeit.default_timer()
    def sum_items(a_list):
        """
        sum_items return the sum of the list
        :param a_list:
        :return:sum of the list
        :complexity: Best Case : O(1)  :Worst Case:O(n)
        """
        assert len(a_list)>=0,"Length of List cannot be negative"
        sum = 0
        if len(a_list) == 0:
            return sum
        else:
            for i in range(len(a_list)):
                sum += a_list[i]
            return sum

    taken = timeit.default_timer() - start
    return taken

print(time_sum_items(list))