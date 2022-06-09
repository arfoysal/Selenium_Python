'''
def all_equals(lst):
    ele = lst[0]
    chk = True

    for item in lst:
        if ele != item:
            chk = False
            break;
    print(chk)


all_equals([1, 1, 1])
'''


def all_equals(lst):
    return len(set(lst)) == 1


print(all_equals([1, 1, 3]))