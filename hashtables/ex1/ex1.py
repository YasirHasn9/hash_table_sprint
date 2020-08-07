def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    '''
    obj to store all the entries and tracker to see where we are in ?
    so we need a linked list ? entry
      


      ||


      
    make an object 
    iterate through the list of weight
    make each weight as a key in the object

    calculate the different between limit and each value in the obj
    if we find the difference in the obj 

    '''

    nums = {}

    # loop through
    for i in range(len(weights)):
        # set the weight to a key
        nums[weights[i]] = i

    # test propusing
    # for key in nums:
    #     print(key , nums[key])

    # tuple where we can store the values
    values = []
    # loop for the range
    for i in range(len(weights)):
        # get the difference around over all if weights
        weight = limit - weights[i]
        # check the key in nums
        if weight in nums:
            # if weight limit is in the nums, then cool
            # but how can compare them ? --> google
            values.append(max(i, nums[weight]))
            values.append(min(i, nums[weight]))

            return values
    return None


arr = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(arr, 9, 7))
