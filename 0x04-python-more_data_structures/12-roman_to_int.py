#!/usr/bin/python3
#from romanian to int
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000,\
	    'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    if roman_string and type(roman_string) == str:
        num = 0
        for s in range(len(roman_string)):
            for r in romans.keys():
                if roman_string[:] is r:
                    num = romans[r]
                    return num
                if roman_string[s:s+1] is r:
                    num += romans[r]
                    break
        return num
    else:
        return 0
