def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # if you wanna get fired then do this lol
    # result = []
    # for i in range(len(a)-1):
    #     for j in range(i + 1 , len(a)):
    #         if a[i] + a[j] == 0:
    #             result.append(abs(a[i]))

    
    result = []
    # add each number to dict
    # access a key/value on obj is O(1)
    d_numbers = {}
    for num in a:
        d_numbers[num] = 1
        if num != 0 and -num in d_numbers:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
