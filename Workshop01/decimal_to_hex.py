# K. Sharsindra Pratheen
# 25636626
# Advanced Computer Science, Monash University

def decimal_to_hex(decimal_number):
    my_list = []
    while decimal_number > 0:
        rem = decimal_number % 16
        if rem > 9:
            if rem == 10:
                rem = 'A'
            elif rem == 11:
                rem = 'B'
            elif rem == 12:
                rem = 'C'
            elif rem == 13:
                rem = 'D'
            elif rem == 14:
                rem = 'E'
            else:
                rem = 'F'
        my_list.insert(0, str(rem))
        decimal_number = decimal_number // 16
    return '0x' + ''.join(my_list)
number = int(input('Enter a number: '))
print('The hexadecimal representation is ' + decimal_to_hex(number))
