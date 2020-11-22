x = "This "

def add_is_a():
    global x
    x+="is "
    x+="a "

def add_function():
    global x
    x += "function"

add_is_a()
add_function()

print(x)