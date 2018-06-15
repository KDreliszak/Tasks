

#ponizsza funkcja rozwiazuje zadany problem z wykorzystaniem oglonych narzedzi
def isPalindrome(*numbers):
    l = []
    for number in numbers:
        palindrom = "True"
        number = str(number)
        number_len = int((len(number))/2)
        for n in range(number_len):
            if number[n] != number[-n-1]:
                palindrom = "False"
                break
        l.append(number + " " + palindrom)
    return l


#ponizsza funkcji wykorzystuje odstępną w Pythonie motodę do obracania ciagu znakow
def isPalindrome2(*numbers):
    l = []
    for number in numbers:
        palindrom = "True"
        number = str(number)
        if number != number[::-1]:
            palindrom = "False"
        l.append(number + " " + palindrom)
    return l


print("Is it palindrom?\n",  isPalindrome(128912, 9758905432, 34566543, 96369, 75211267, 76211267))

print("Is it palindrom?\n",  isPalindrome2(128912, 9758905432, 34566543, 96369, 75211267, 76211267))
