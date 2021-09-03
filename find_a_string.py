#Method 01
def count_substring(string, sub_string):
  count = 0;
  for i in range(0,len(string) - len(sub_string)):
    l = i
    for j in range(0,len(string)):
      if string[l] == sub_string[j]:
        l += 1
        if j == len(sub_string)-1:
          count = count + 1
        else:
          continue
      else:
        break
    return count
  
  
  
if __name__ == "__main__":
  string = input().strip()
  sub_string = input().strip()
  count = count_substring(string,sub_string)
  print(count)
  
  
 #Method 02

def count_substring(string, sub_string):
        count = 0
        for i in range(len(string)):
                count += string.startswith(sub_string, i)
        return count
