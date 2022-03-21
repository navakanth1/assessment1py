print("Enter the String: ")
text = input()
text = text.split()
bigWordLen = 0

for wrd in text:
  wrdLen = len(wrd)
  if wrdLen>bigWordLen:
    bigWordLen = wrdLen

print("\nLargest Word: ")
for wrd in text:
  wrdLen = len(wrd)
  if wrdLen==bigWordLen:
    print(wrd)