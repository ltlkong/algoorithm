# get prime divisor
from typing import List


def refactorPrimeDivisor(num: int) -> List[int]:
    divisor = 2
    result = []

    def refactor(num, divisor, result):
        if divisor > num:
            return

        if num % divisor == 0 and isPrime(divisor):
            num = num//divisor
            result.append(divisor)
        else:
            divisor += 1
        refactor(num, divisor, result)
    refactor(num, divisor, result)

    return result


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


while True:
    try:
        num = input("Enter a number: ")
        if num.isdigit() == False:
            print("Please enter interger only")
            continue
        print(refactorPrimeDivisor(int(num)))
    except KeyboardInterrupt:
        print("\nExit")
        break
