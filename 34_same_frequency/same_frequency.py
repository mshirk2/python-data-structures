def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    count1 = {}
    for i in str(num1):
        count1[i] = count1.get(i, 0) + 1

    count2 = {}
    for j in str(num2):
        count2[j] = count2.get(j, 0) + 1

    return count1 == count2

