def fun1(n):
    return n*(n+1)/2
print(fun1(4))
# time complexity = 1
# most eficient

def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
print(fun2(4))
#time complexity = n

def fun3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum += 1
    return sum
print(fun3(4))
# time complexity = n^2
# least eficient