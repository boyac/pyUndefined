def checkio(number):
    #replace this for solution
    ROMANS = (('M',  1000),
          ('CM', 900),
          ('D',  500),
          ('CD', 400),
          ('C',  100),
          ('XC', 90),
          ('L',  50),
          ('XL', 40),
          ('X',  10),
          ('IX', 9),
          ('V',  5),
          ('IV', 4),
          ('I',  1))
    
    roman_numeral = ''
    
    for roman, value in ROMANS:
        while number >= value:
            number -= value
            roman_numeral += roman
            
    return roman_numeral
