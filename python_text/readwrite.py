with open("name.txt") as f:
    my_name = f.read()

greeting = f"Hello, my name is {my_name}."

with open("output/hello.txt", "w") as f:
    f.write(greeting)
