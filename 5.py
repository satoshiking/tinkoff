def how_many(my_string):
    if len(my_string) < 2:
        return 1
    else:
        letter = my_string[-2:]

        if letter[0] != '0' and (0 <= int(letter) <= 33):
            return how_many(my_string[0:-2]) + how_many(my_string[0:-1])
        else:
            return how_many(my_string[0:-1])

encrypted = input()
print(how_many(encrypted))