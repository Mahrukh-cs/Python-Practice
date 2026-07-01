# for loop (if you know in advance: how many times you want to execute this loop)
# # 1st approach
# for i in [1, 2, 3]:
#     print("meow")


# # better approach
# for i in range(5):
#     print("meow")


# # better approach (if you are not using variable later on in your code, it's better to use underscore '_')
# for _ in range(3):
#     print("meow")


# # without loops 
# print("meow" * 3)

# # to print on newline '\n'
# print("meow\n" * 3)


# # if you don't want a blank line in last
# print("meow\n" * 3, end="")


# # 1st approach 
# while True:
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break
# for _ in range(n):
#     print("meow")




# # 2nd approach(better)
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")



# # 3rd approach using my own function
# def main():
#     meow(6)

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()


# 4th approach 
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()