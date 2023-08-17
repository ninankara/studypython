def romanToInt(s):
        sum = 0
        substract = ['IV','IX','XL','XC','CD','CM']

        romanDict = {'I':1, 
                     'V':5,
                     'X':10,
                     'L':50,
                     'C':100,
                     'D':500,
                     'M':1000}

        subRomanDict = {'IV':4,
                        'IX':9,
                        'XL':40,
                        'XC':90,
                        'CD':400,
                        'CM':900}

        for i in substract:
            if i in s:
                sum = sum + subRomanDict[i]
                s = s.replace(i,'')

        for i in s:
            num = romanDict[i]
            sum = sum + num

        return sum