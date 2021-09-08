#Method 1:
x,y = map(int,input().split())
items = list(range(1,x+1,2))
items = items + items[::-1][1:]
for i in items:
  text = "Welcome" if i == x else ".|."*i
  print(text.centre(y,'-'))
