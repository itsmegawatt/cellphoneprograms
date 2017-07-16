import random
def main():
    result = "Your lucky numbers are: "
    for i in range(6):
        result += str(random.randint(1,46)) + ", "
    print(result)

if __name__ == '__main__':
    main()
