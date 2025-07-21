def main():
    numbers = list(map(int, input("숫자를 입력하세요: ").split())) 
    # n개의 입력 받을 때 처리방법
    # 대소비교할 때 어떻게 처리할 것인지
    
    sorted_numbers = sorted(numbers) 
    # sort 및 sorted 함수 사용법 숙지
    # 파이썬 기본함수 사용법 숙지

    Min = sorted_numbers[0] # 리스트에서 첫번쨰, 마지막 요소 가져오기
    print("Min:", Min, end="")

    Max = sorted_numbers[-1] 
    print(", Max:", Max)
     
if __name__ == "__main__":
    main()
     