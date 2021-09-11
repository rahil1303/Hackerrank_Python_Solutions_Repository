s = input()
vowel = "AEIOU"
k = 0
si = 0
for i in range(len(s)):
  if s[i] in vowels:
    k += (len(s) - i)
   else:
    si += (len(s) - i)
if k > s:
  print("Kevin",k)
elif k < s:
  print("Sturat:,s)
else:
  print("Draw")
