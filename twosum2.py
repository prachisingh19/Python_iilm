def twosum(num,t):
    x=0
    while (x < len(num)):
        z=x+1
        while (z < len(num)):
            if num[x]+num[z]==t:
                return [x,z]
            z=z+1
        x=x+1
    return []                                                                                                                                                                   
