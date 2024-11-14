def main():
    try:
        number = int(input("Enter any number below:"))
    except ValueError:
        print("invalid input")
        return

    if number % 4 == 0:
        print("The number is divisible by 4.")
    elif number % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is odd")


if __name__ == "__main__":
    main()