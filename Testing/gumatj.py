# Coding a program to convert base 5 numbers to base 10 numbers; convert base 10 numbers to base 5 numbers; find the sum of 2 base 5 numbers; find the product of 2 base 5 numbers
# Author: Dylan Friedman
# FRDDYL002
# 16th April 2022

def gumatj_to_decimal(a):
    # Code to convert quinary to decimal
    stra = str(a)
    if len(stra) == 4:
        basecb = stra[0:1]
        basesq = stra[1:2]
        base = stra[2:3]
        unit = stra[3:4]
        decnum = 125*int(basecb) + 25*int(basesq) + 5*int(base) + int(unit)
        
    elif len(stra) == 3:  # if the quinary number has a multiple of 25
        basesq = stra[0:1]
        base = stra[1:2]
        unit = stra[2:3]
        decnum = 25*int(basesq) + 5*int(base) + int(unit)
        
    elif len(stra) == 2:
        base = stra[0:1]
        unit = stra[1:2]
        decnum = 5*int(base) + int(unit)
    else:
        unit = stra
        decnum = int(unit)
        
    return decnum
    
def decimal_to_gumatj(a): # eg 437
    # Code to convert decimal to quinary
    basecb, basesq, base, rembs = 0, 0, 0, 0
    if a == 0:
        return '0'
    
    basecb = a // 125
    if basecb != 0:
        remcb = a % 125
        basesq = remcb // 25
        if basesq != 0:
            remsq = remcb % 25
            base = remsq // 5
            if base != 0:
                rembs = remsq % 5
                return str(str(basecb) + str(basesq) + str(base) + str(rembs))
            else:
                #rembs = remsq
                return str(basecb) + str(basesq) + str(base) + str(rembs)
        else:
            base = remcb // 5
            if base != 0:
                rembs = remcb % 5    
                return str(basecb) + str(basesq) + str(base) + str(rembs)
            else:
                #rembs = remcb
                return str(basecb) + str(basesq) + str(base) + str(rembs)
    else:
        basesq = a // 25
        if basesq != 0:
            remsq = a % 25
            base = remsq // 5
            if base != 0:
                rembs = remsq % 5
                return str(str(basesq) + str(base) + str(rembs))
            else:
                return str(str(basesq) + str(remsq))
             #   rembs = remsq
        else:
            base = a // 5
            if base != 0:
                rembs = a % 5 
                return str(str(base) + str(rembs))
            else:
                return str(a)
                
    #return str(basecb + basesq + base + rembs)
    
    
def gumatj_add(a, b):
    # Code to add to quinary values together
    adec = gumatj_to_decimal(a)
    bdec = gumatj_to_decimal(b)
    
    added = int(adec) + int(bdec)
    return decimal_to_gumatj(added)

def gumatj_multiply(a, b):
    # Code to sum two quinary values
    adec = gumatj_to_decimal(a)
    bdec = gumatj_to_decimal(b)
    
    mult = int(adec) * int(bdec)
    return decimal_to_gumatj(mult)

    