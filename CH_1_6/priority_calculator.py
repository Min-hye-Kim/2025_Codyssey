from CH_1_3_to_1_4.david.calculator import add, subtract, multiply, divide
# 헉 파이썬에서 .와 -는 모듈 이름으로 안 되는구나.. 숫자로 시작하는 이름도 안 된다고 한다.
# 이렇게 하려면 파이썬을 프로젝트 최상위 폴더 기준으로 실행해야 한다고 함.

def main():
    formula = input().split()  # 괄호 필수!
    
    # def serch_cal (formula, *)
    #     if '*' in formula:
    #         multiply
    #     elif '/' in formula:
    #         divide
    #     elif '+' in formula:
    #         add
    #     elif '-' in formula:
    #         subtract
 #————————————————————————————————   
    i = 0
    while i < len(formula):
        if formula[i] == '*' or formula[i] == '/':
            a = float(formula[i-1])
            b = float(formula[i+1])

        if formula[i] == '*':
            result = multiply(a, b)
        else:
            result = divide(a, b)

        # 결과를 가운데 넣고, 좌우 항목 삭제
        formula[i-1:i+2] = [str(result)]  # 리스트 3개를 1개로 치환

        # 인덱스를 다시 앞으로 돌림
        i = 0
    
    else:
        i += 1

#————————————————————————————————

if __name__ == "__main__":
    main()

