def sum_num():
    total = 0
    for i in range(0, 10):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print(total)

sum_num()