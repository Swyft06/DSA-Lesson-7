text = input("Enter any word")
stack = []


for letter in text:
    stack.append(letter)

print(stack)

reversedword = ""
while stack:
    reversedword += stack.pop()

print(reversedword)