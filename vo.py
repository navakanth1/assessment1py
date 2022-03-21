vowels="aeiou"
string = input("APPLE IS GOOD")
string = string.casefold()
count = {}.fromkeys(vowels,0)
for char in string:
    if char in count:
        count[char] += 1
print(count)