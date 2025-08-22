# slowo = input("Podaj slowo: ")
# # print(len(slowo))
# # print(range(len(slowo)))
#
# for i in range(len(slowo), 0, -1):
#     print(slowo[i-1])
#
# # for letter in slowo:
#     print(letter)
#

liczba = int(input("Podaj liczba: "))
if 0 < liczba < 51:
    for i in range(1, liczba):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
#ctrl+alt+ l formatowanie poprawia