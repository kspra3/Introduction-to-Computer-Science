List_size = "Enter size of list:"
size = int(input(List_size))
List = [0]*size
Value = "Enter temperature:"

i = 0
while i < size:
    List[i] = int(input(Value))
    i = i + 1


def minimum1(List, size1):
    j = 0
    minimum = List[0]
    while j < size1:
        if List[j] < minimum:
            minimum = List[j]
        j = j + 1
    return minimum


def maximum1(List, size1):
    j = 0
    maximum = List[0]
    while j < size1:
        if List[j] > maximum:
            maximum = List[j]
        j = j + 1
    return maximum


def freq_temp(List, size1, max_temp, min_temp):
    m = 0
    while m < max_temp:
        freq = 0
        j = 0
        while j < size1:
            if min_temp == List[j]:
                freq = freq + 1
            j = j + 1
        if freq > 0:
            print(str(min_temp) + " appears " + str(freq) + " times. ")
        m = m + 1
        min_temp = min_temp + 1

min_temp = minimum1(List, size)
max_temp = maximum1(List, size)
print(freq_temp(List, size, max_temp, min_temp))
