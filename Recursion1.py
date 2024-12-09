
def factorial(n):
    if n== 1:
        return 1
    return n*factorial(n-1)


def is_palindrome(to_check:str):
    if len(to_check) == 1:
        return True
    if len(to_check) == 0:
        return True
    if to_check[0] != to_check[-1]:
        return False
    return is_palindrome(to_check[1:-1])

def tell_a_fib(numb):
    if numb == 1:
        return 1
    if numb == 2:
        return 1
    return tell_a_fib(numb-1) + tell_a_fib(numb-2)

def loop_fib(numb):
    prev = 1
    before_that = 1
    answer = 0
    for i in range(2, numb):
        answer = prev + before_that
        before_that = prev
        prev = answer
    return answer


def main():
    choice = int(input("Enter a number: "))
    print(factorial(choice))
    print(loop_fib(choice))
    print(tell_a_fib(choice))
    # to_check = input("Enter string for palindrome check: ")
    # print(is_palindrome(to_check))

if __name__ == '__main__':
    main()
