##The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

## The first line contains the sum of the two numbers.
## The second line contains the difference of the two numbers (first - second).
## The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    add = a+b
    sub = a-b
    mult = a*b
    
    print(add)
    print(sub)
    print(mult)
