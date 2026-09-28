text = input("Enter any word: ")
stack = []

for letter in text:
    stack.append(letter)
reversedword = ""

while stack:
    reversedword += stack.pop()
print(reversedword)

if text == reversedword:
    print("The word is a palindrome!")
else:
    print("The word is not a palindrome!")