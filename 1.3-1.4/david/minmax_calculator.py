def main():
    # n개의 입력 받을 때 처리방법
    # 대소비교할 때 어떻게 처리할 것인지

    try:
        numbers = list(map(int, input("숫자를 입력하세요: ").split()))

#———————————————————————————————————————————————————————————

        sorted_numbers = sorted(numbers) 
    # sort 및 sorted 함수 사용법 숙지
    # 파이썬 기본함수 사용법 숙지
        Min = sorted_numbers[0] # 리스트에서 첫번쨰, 마지막 요소 가져오기
        print("Min:", Min, end="")

        Max = sorted_numbers[-1] 
        print(", Max:", Max)
        
#———————————————————————————————————————————————————————————

    except ValueError:
        print ("Invalid input.")

# 아 try-exccept 를 붙여야 한다는 생각에 ---로 둘러싸인 부분을 except 밖으로 빼 버렸음.
    # 그러니까 except가 실행되었을 경우에 numbers 값이 생성되지 않아,
    # except 밖에서 실행되어야 할 코드가 실행되지 않음으로써 오류 발생
# "구문" 사용할 때는 ▶ 반드시 범위 확인을 잘 해야 함에 유의할 것.

if __name__ == "__main__":
    main()
     