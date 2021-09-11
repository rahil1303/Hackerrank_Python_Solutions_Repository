s = input()
vowel = "AEIOU"
k = 0
si = 0
for i in range(len(s)):
  if s[i] in vowels:
    k += (len(s) - 1)
   else:
    si += (len(s) - 1)
if k > s:
  print("Kevin",k)
elif k < s:
  print("Sturat:,s)
else:
  print("Draw")
