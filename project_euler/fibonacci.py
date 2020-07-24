def fibonacci():
    # Initiate the fibonacci sequence
    a = 1
    b = 1
    c = 0
    result = 0
    # While less than 4 million
    while c < 4000000:
        c = a + b
        # Take the sum of all even integers
        if c % 2 == 0:
            result = result + c
        # Loop the fibonacci sequence
        a = b
        b = c
    print(result)

