List_size = "Enter size of list:"
size = int(input(List_size))
List = [0]*size
i = 0
j = 0
exceed = 0

Value = "Enter value:"

while i < size:
    List[i] = int(input(Value))
    i = i + 1


Target_inspect = "Enter target number to inspect: "
Target_value = int(input(Target_inspect))

while j < size:
    if Target_value >= List[j]:
        exceed = exceed + 1
    j = j + 1
print(exceed)
