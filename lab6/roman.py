class Roman(object):
    value = 0

    @staticmethod
    def atoi(roman_number_str):
        figures = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1
        }
        value = 0 
        number_len = len(roman_number_str)
        for i in range(number_len):
            if i+1 < number_len:
                if figures[roman_number_str[i]] < figures[roman_number_str[i+1]]:
                    value -= figures[roman_number_str[i]]
                    continue
            value += figures[roman_number_str[i]]
        return value

    @staticmethod
    def itoa(number):
        val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        roman_num = ''
        i = 0
        while  number > 0:
            for _ in range(number // val[i]):
                roman_num += syb[i]
                number -= val[i]
            i += 1
        return roman_num

    def __init__(self, roman_number_str):
        self.value = Roman.atoi(roman_number_str)

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __floordiv__(self, other):
        return self.value // other.value
        
    def __mod__(self, other):
        return self.value // other.value


roman1 = Roman('XL')
roman2 = Roman('IX')
print(str(roman1.value) + ' and ' + str(roman2.value))
print(str(roman1 + roman2) + ' ' + Roman.itoa(roman1 + roman2))
print(str(roman1 - roman2) + ' ' + Roman.itoa(roman1 - roman2))
print(str(roman1 * roman2) + ' ' + Roman.itoa(roman1 * roman2))
print(str(roman1 // roman2) + ' ' + Roman.itoa(roman1 // roman2))
print(str(roman1 % roman2) + ' ' + Roman.itoa(roman1 % roman2))




    