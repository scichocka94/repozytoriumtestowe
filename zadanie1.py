mlist = [1, 2, [4, [8, [9]], 10, 15], 16]

new_list = []


def number():
    for i in mlist:
        if type(i) is list:
            new_list.extend(i)
        else:
            new_list.append(i)

    return new_list


print(number())