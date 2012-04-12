def rabbits(n):
    if n <= 5:
        return [0,1,1,2,3,5][n]
    return rabbits(n-1) + rabbits(n-2) - rabbits(n-5)

