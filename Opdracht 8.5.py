def tafels(n):
    tafel = 1
    for i in range(n-1):
        for j in range(n):
            if j != 0:
                uitkomst = tafel * j
                print(tafel, ' x ', j, ' = ', uitkomst)
                print()
        print()
        tafel += 1


n = 11
print(tafels(n))