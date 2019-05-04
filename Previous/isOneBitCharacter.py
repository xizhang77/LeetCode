def isOneBitCharacter(bits):
    """
    :type bits: List[int]
    :rtype: bool
    """
    n = len(bits)
    if n<=1:
        return True
    else:
        if ( bits[-2] == 0 ):
            return True
        else:
            countone = 0;
            pointer = -3;
            while( abs(pointer)<=len(bits) and bits[pointer]==1 ):
                pointer -= 1
                countone += 1
            if countone%2:
                return True
            else:
                return False

print isOneBitCharacter([0])