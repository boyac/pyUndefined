FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
​
def checkio(number):
    spoken = []
    
    hundred_bit = number / 100 
    
    if hundred_bit > 0:
        spoken.append(FIRST_TEN[hundred_bit - 1])
        spoken.append(HUNDRED)
    
    remain = number % 100
    if remain >= 10 and remain <= 19:
        spoken.append(SECOND_TEN[remain % 10])
    else:
        decade = remain / 10 
        if decade > 0:
            spoken.append(OTHER_TENS[decade - 2])
        
        unit = remain % 10
        if unit > 0:
            spoken.append(FIRST_TEN[unit-1])
    
    return ' '.join(spoken)
