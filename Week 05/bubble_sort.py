a_list = [5,6,2,3,1]

def bubble_sort(a_list):
    n = len(a_list)
    for i in range(n-1):
        for j in range(n-1):
            if a_list[j] > a_list[j+1]:
                swap(a_list,j,j+1)
    return a_list

def swap(the_list,i,j):
    the_list[i],the_list[j] = the_list[j], the_list[i]

print(bubble_sort(a_list))