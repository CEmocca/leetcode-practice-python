class RomanToInteger:
    def __init__(self) -> None:
        self.roman_dict = dict([('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000)])

    def roman_to_integer(self, s: str) -> int:
        previous_value = 0
        sum = 0
        for i_value in s:
            if self.roman_dict[i_value] > previous_value:
                sum += self.roman_dict[i_value] - previous_value - previous_value
            else:
                sum += self.roman_dict[i_value]

            previous_value = self.roman_dict[i_value]
        return sum


def main():
    roman = RomanToInteger()
    print(roman.roman_to_integer("III"))
    print(roman.roman_to_integer("LVIII"))
    print(roman.roman_to_integer("MCMXCIV"))

main()