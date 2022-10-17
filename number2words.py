magnitude_dict = {2: 'hundred', 3: 'thousand', 6: 'million', 9: 'billion', 12: 'trillion', 15: 'quadrillion',
                  18: 'quintillion', 21: 'sextillion', 24: 'septillion'}
num_dict = {}
f = open('1-100.txt', "r")
for line in f.readlines():
    l_edit = line.strip().split()
    num_dict.update({int(l_edit[0]): l_edit[2]})


def number_to_words(number):
    digits = len(str(number))
    if digits > max(magnitude_dict.keys()):
        return "Number too large!"
    if digits <= 2:
        return num_dict[number]
    if digits == 3:
        if int(str(number)[1:]) == 0:
            return " ".join([number_to_words(int(str(number)[0])),
                             magnitude_dict[digits - 1]])
        else:
            return " ".join([number_to_words(int(str(number)[0])),
                             magnitude_dict[digits - 1],
                             number_to_words(int(str(number)[1:]))])
    else:
        mag = (3*((digits-1)//3))
        remainder = int(number % 10**mag)
        return ", ".join([" ".join([number_to_words(int(str(number)[:(digits-mag)])),
                         magnitude_dict[3*(mag//3)]]),
                         number_to_words(int(str(remainder)))])
