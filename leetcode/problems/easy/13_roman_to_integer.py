class Solution:
    def romanToInt(self, s: str) -> int:
        roman_single_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman_double_numbers = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        sum = 0
        while s:
            current_single_number = s[0]
            if len(s) > 1:
                current_double_number = s[:2]
            else:
                current_double_number = ''

            if current_single_number in roman_single_numbers and current_double_number not in roman_double_numbers:
                sum += roman_single_numbers[current_single_number]
                s = s[1:]
            elif current_double_number in roman_double_numbers:
                sum += roman_double_numbers[current_double_number]
                s = s[2:]

        return sum


def main():
    solution = Solution()
    # s = "MCMXCIV"
    s = "MDCXCV"
    print(solution.romanToInt(s))


if __name__ == '__main__':
    main()
