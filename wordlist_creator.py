import timeit
# Python program to print all permutations with 
# duplicates allowed 
# saving into file

def toString(List):
  return ''.join(List[0:8]) #replace 8 with any no for more complicated password

# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 

def permute(a, l, r): 
  if l==r:
    char=toString(a)
    print(char)
    with open("wordlist8.txt","a") as f: #for writing into file
      f.write(char)
      f.write("\n")
      f.close() #
  else:
    for i in range(l,r+1): 
      a[l], a[i] = a[i], a[l] #swap
      permute(a, l+1, r) 
      a[l], a[i] = a[i], a[l] # backtrack 
  
# Driver program to test the above function
start = timeit.default_timer()
string = """ABCDEFGHIJKLMNOPQRSTUVWXYZ `~!@#$%^&*()_-+={[}]|\:;"'<,>.?/abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ `~!@#$%^&*()_-+={[}]|\:;"'<,>.?/abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ `~!@#$%^&*()_-+={[}]|\:;"'<,>.?/abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ `~!@#$%^&*()_-+={[}]|\:;"'<,>.?/abcdefghijklmnopqrstuvwxyz0123456789"""
n = len(string) 
a = list(string) 
permute(a, 0, n-1)
stop = timeit.default_timer()
print("\n")
print('Time: ', ((stop - start))) #time in seconds
