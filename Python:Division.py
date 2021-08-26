## Add logic to print two lines. The first line should contain the result of integer division, a // b. 
## The second line should contain the result of float division, a / b.


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    div = a//b;
    divf = a/b;
    
    print(div)
    print(divf)
