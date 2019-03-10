
def ret_true():
    return True


def ret_false():
    return False


a = ret_true() | ret_false()
print(a)

a = ret_true() & ret_false()
print(a)

a = ret_false() & ret_false()
print(a)

data1 = {1, 2, 3}
data2 = {3, 4, 5}
data = data1 | data2
print(data)

data = data1 & data2
print(data)