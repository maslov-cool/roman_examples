def roman():
    global one, two, three

    def translation_to_roman_num_sys(n):
        new_n = ''
        for i in range(len(str(n))):
            num = int(str(n)[i])
            if len(str(n)) - i == 4:
                new_n += 'M' * num
                continue
            elif len(str(n)) - i == 3:
                if 0 < num < 4:
                    new_n += 'C' * num
                    continue
                elif num == 4:
                    new_n += 'CD'
                    continue
                elif num == 5:
                    new_n += 'D'
                    continue
                elif 6 <= num <= 8:
                    new_n += ('D' + ('C' * (num - 5)))
                    continue
                elif num == 9:
                    new_n += 'CM'
                    continue
            elif len(str(n)) - i == 2:
                if 0 < num < 4:
                    new_n += 'X' * num
                    continue
                elif num == 4:
                    new_n += 'XL'
                    continue
                elif num == 5:
                    new_n += 'L'
                    continue
                elif 6 <= num <= 8:
                    new_n += ('L' + ('X' * (num - 5)))
                    continue
                elif num == 9:
                    new_n += 'XC'
                    continue
            else:
                if 0 < num < 4:
                    new_n += 'I' * num
                    continue
                elif num == 4:
                    new_n += 'IV'
                    continue
                elif num == 5:
                    new_n += 'V'
                    continue
                elif 6 <= num <= 8:
                    new_n += ('V' + ('I' * (num - 5)))
                    continue
                elif num == 9:
                    new_n += 'IX'
                    continue
        return new_n

    three = one + two
    print(f'{translation_to_roman_num_sys(one)} + {translation_to_roman_num_sys(two)} = '
          f'{translation_to_roman_num_sys(three)}')
