nomor_list = [1,2,3]

def sum_sqr(x):
    return x * x

total = list(map(sum_sqr,nomor_list))
print(sum(total))