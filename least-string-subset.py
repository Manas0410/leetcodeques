def least_str_subset(string):
    count = 1
    unique = set()

    for i in string:
        if i in unique:
            count += 1
            unique = set()  # to again empty the set to create new substring
        unique.add(i)
    return count


str = 'abacaba'
print(least_str_subset(str))
