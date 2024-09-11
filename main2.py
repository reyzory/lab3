def remove_adjacent_duplicates(x):
    result = x[0]

    for i in range(1, len(x)):
        if x[i] != x[i - 1]:
            result += x[i]

    return result

zxc = "ssssttttuuuuuddddeeeeeeennnnt"
result = remove_adjacent_duplicates(zxc)
print(result)

