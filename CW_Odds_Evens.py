def main():
    print("Enter a number and I will tell you if it is even or odd.")
    number = int(input('Your number:'))
    if number % 2 == 0:
        print('This number is Even.')
    else:
        print('This number is Odd.')
if __name__ == '__main__':
  main()
