### Method 1
def solve(s):
  for i in s.split():
    s = s.replace(i,i.capitalize())
   return s

if __name__ = "__main__":
  fptr = open(os.environ["Output Path"], "w")
  s = input()
  result = solve(s)
  fptr.write(result + "\n")
  fptr.close()
  
###Method 2
def solve_it(s):
    for i in s.split():
        s = s.title()
    return s

s = input()
result = solve_it(s)
print(result)
