def main():
    x = int(input("What's x? "))

    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    # or better way 
    #return True if n % 2 == 0 else False
    # much more better way
    return n % 2 == 0

main()
