# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

def decimal_to_binary(decimal_number):
    my_list = []
    while decimal_number > 0:
        rem = decimal_number % 2
        my_list.insert(0, str(rem))
        decimal_number = decimal_number // 2
    return '0b' + ''.join(my_list)

number = int(input('Enter a number: '))
print('The binary representation is ' + decimal_to_binary(number))
