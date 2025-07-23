def main():

    numbers = list(map(float, input("숫자를 입력하세요: ").split()))
    # 리스트 mapping 공부

#————————————————————————————————

    def Sorting():

        try:
            for i in range(len(numbers)):
                for j in range(i):
                    if numbers[j]>numbers[j+1]:
                        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                        # 리스트 안 요소를 지정하는 방법? 가리키는 방법 알아두기
            return("Sorted:", *numbers)
                # 구문에서는 항상 들여쓰기 주의!!!!

        except ValueError:
            print ("Invalid input.")

#————————————————————————————————

    print(Sorting())

if __name__ == "__main__":
    main()
