# return
def plus(val1, val2):
    return val1+val2

def print_hello3(val1, val2):
    print(val1,val2)

result = print_hello3(10, 20)
result_return = plus(10, 20)


print("result:",result)
print("result_return:",result_return)

# for 반복문
for item in range(0,10) :
    print(item)

for item in [0,1,2,2]:
    print(item)

for item in range(2,10):
    print(item,"단================")
    for item2 in range(1,10):
        print(item, "*",item2,"=",item*item2)

# 배열
print(list(range(0,10)))

# for each