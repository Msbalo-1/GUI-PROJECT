


def acronyms():
    
    word = str(input("Enter The Words: "))
    text = word.split()
    a = " "
    for i in text:
        a = a+str(i[0]).upper()
        print(a)


acronyms()



tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    # specify more numerals if you wish
}

def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left = romanNumeral[i]
        right = romanNumeral[i + 1]
        if tallies[left] < tallies[right]:
            sum -= tallies[left]
        else:
            sum += tallies[left]
    sum += tallies[romanNumeral[-1]]
    return sum


RomanNumeralToDecimal()
