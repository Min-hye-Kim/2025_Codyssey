def main():

    numbers = list(map(float, input("숫자를 입력하세요: ").split()))
    # 리스트 mapping 공부

#————————————————————————————————

    def Sorting():

        try:
            for i in range(len(numbers)):
                for j in range(len(numbers) - i - 1):  # ← 여기 중요
                    if numbers[j]>numbers[j+1]:
                        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                        # 리스트 안 요소를 지정하는 방법? 가리키는 방법 알아두기
            return "Sorted:", *numbers
                # loop 구문에서는 항상 들여쓰기 주의!!!!
                # print( f"Sorted:{*numbers}") → 문법적으로 금지된 형태?

        except ValueError:
            print ("Invalid input.")

    print(*Sorting())
    #여기 좀 헷갈림.. 앞에서 * 붙여줬는데 또 해줘야 되는지?

#————————————————————————————————

if __name__ == "__main__":
    main()