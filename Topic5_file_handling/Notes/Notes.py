
file = open('file.txt', 'r')
content = file.read()
print(content)
file.close()

# 'w' (Write mode):

# Opens the file for writing. If the file already exists, it overwrites the existing content with the new content. If the file doesn't exist, it creates a new file.

with open('file.txt', 'w') as file:
    file.write('What is your language preferance')


# 'a' (Append mode):

# Opens the file for writing.
#  If the file already exists, it appends the new content at the end of the existing content, 
# without removing any previous data. 
# If the file doesn't exist, it creates a new file.

with open('file.txt', 'a') as file:
    file.write(" What is your language preferance")

with open('file.txt', 'r') as file:
    content = file.read()
    print(content)


file = open('file.txt', 'r')
content = file.read()
print(content)
file.close()

file = open('file.txt', 'w')
file.write("Hello")
file.close()

file = open('file.txt', 'r')
content = file.read()
print(content)
file.close()

file = open('file.txt', 'r')
content = file.read()
print(content)
file.close()

file = open('file.txt', 'a')
file.write("Hello")
file.close()

file = open('file.txt', 'r')
content = file.read()
print(content)
file.close()
