def area(length, width):
    print(str((length * width)) + " square feet")
    return length * width

def main():
    houseArea = area(20, 50)
    yardArea = area(50, 50)
    totalArea = houseArea + yardArea
    print(str(totalArea) + " square feet")

main()