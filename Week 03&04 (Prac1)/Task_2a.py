List_size = "Enter size of list:"
size = int(input(List_size))
List = [0]*size
Value = "Enter value:"

i = 0
while i < size:
    List[i] = int(input(Value))
    i = i + 1


def list_range(List, size1):
    """

    :param List:
    :param size1:
    :return:
    """
    j = 0
    minimum = List[0]
    maximum = List[0]
    while j < size1:
        if List[j] < minimum:
            minimum = List[j]
        if List[j] > maximum:
            maximum = List[j]
        j = j + 1

    range_list = maximum - minimum
    print(range_list)

list_range(List, size)
