# wap to display unique words from the string
string = input()
string = list(set(string))
res = ""
for i in string:
    res +=i
print(res)
