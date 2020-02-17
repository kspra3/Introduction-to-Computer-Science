List_size = "Enter size of list:"
size = int(input(List_size))
List = [0]*size

i = 0

Value = "Enter value:"

while i < size:
    List[i] = int(input(Value))
    i = i + 1

minimum = List[0]
maximum = List[0]

j = 0
while j < size:
    if List[j] < minimum:
        minimum = List[j]
    if List[j] > maximum:
        maximum = List[j]
    j = j + 1

range_List = maximum - minimum
print(range_List)
