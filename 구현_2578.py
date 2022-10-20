chulsoo = [list(map(int, input().split())) for _ in range(5)]
MC = [list(map(int, input().split())) for _ in range(5)]

count = 0 # 사회자가 번호 부른 횟수

#빙고 개수 세기
def solution(array: list):
    bingo_number = 0
    
    #가로빙고
    for i in range(5):
        if sum(array[i]) == 0:
            bingo_number +=1
    
    #세로빙고
    for i in range(5):
        count_temp = 0
        for j in range(5):
            if array[j][i] == 0:
                count_temp +=1
        if count_temp == 5:
            bingo_number += 1
    
    # 대각선이 빙고일 때
    temp_up = []
    temp_down = []
    for i in range(5):
        temp_up.append(array[i][i])
        temp_down.append(array[i][4-i])
        
    if sum(temp_up) == 0:
        bingo_number +=1
    if sum(temp_down) == 0:
        bingo_number +=1
        
    return bingo_number


for i in range(5):
    for j in range(5):
        for k in range(5):
            for h in range(5):
                if MC[i][j] == chulsoo[k][h]: 
                    chulsoo[k][h] = 0 # 번호 0으로 만들기
                    count +=1 # 부른횟수를 1 더해줌
                if count >= 12: #12가 3빙고 울리는 최소한 조건
                    if solution(chulsoo) >=3: #빙고 3개이상이면
                        print(count)
                        exit()
                        
                        
#풀이
#1.철수, mc 값 받기
#2.4중 for문으로 mc값과 철수값 비교 > 일치시 철수의 배열 0으로 변경
#3.3빙고 최소값 12  이므로 0의 개수가 12 넘으면 함수타기
#4. 함수만들기
#5. 함수는 가로빙고, 세로빙고, 대각선빙고로 나뉘어짐
#6. 함수에서 bingo_number return 하는데 3이 안되면 계속 count 셈
#7. 3되면 print(count) 정답 출력