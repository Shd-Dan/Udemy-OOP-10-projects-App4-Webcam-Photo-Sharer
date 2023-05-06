final_list = []
while True:
    the_dict = {i: ' ' for i in range(1, 81)}

    row_input = input("row is: ")
    if row_input == 'x':
        break
    else:
        the_row = [int(i) for i in row_input.split()]
        for num in the_row:
            the_dict[num] = num
        final_list.append(the_dict)

for i in final_list:
    print(*i.values(), sep=' ')
