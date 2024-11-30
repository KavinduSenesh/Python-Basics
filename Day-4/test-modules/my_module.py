def add(a, b):
    return a + b

# __name__: This is a special built-in variable in Python. When a Python script is run, the __name__ variable is set to "__main__". When a script is imported as a module in another script, the __name__ variable is set to the name of the script/module.
if __name__ == "__main__":
    print(add(1, 2))