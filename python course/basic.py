# print("hello")

# def chai(n):
#     print(n)

# chai(4)

# chai_one = "lemon tea"
# chai_two = "milk tea"





# Write to a file
with open("data.txt", "w") as file:
    file.write("Hello, this is a text file.\n")
    file.write("Second line.")


with open("data.txt", "r") as file:
    content = file.read()
    print(content)
