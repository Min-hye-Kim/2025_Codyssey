def main():

    numbers = list(input("숫자를 입력하세요: ").split())
    def Sorting():
        try:
            for i in range(len(numbers)):
                if numbers[j]>numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            print("Sorted:", Sorting)
        except ValueError:
            print ("Invalid input.")


if __name__ == "__main__":
    main()
