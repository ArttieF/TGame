# define easy to use clear screen that works on multiple os
def clear():
    import os
    if(os.name =='posix'):
        os.system('clear')
    else:
        os.system('cls')

# define sleep as an easy to call function
def sleep(n):
    from time import sleep
    sleep(n)