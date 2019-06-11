#without argument
def prompt():
    name = input("Enter your name:")
    print('Hello',name)
prompt()

#with argument
def prompt(n):
    print('Hello',n)
prompt('tanu')