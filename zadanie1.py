new_list = []


def number():
    for i in mlist:
        if type(i) is list:
            new_list.extend(i)
        else:
            new_list.append(i)

    return new_list


print(number())