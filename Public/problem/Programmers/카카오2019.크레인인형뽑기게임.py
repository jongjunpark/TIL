def solution(board, moves):
    global answer
    answer = 0
    basket = []
    doll_catch(board, moves, 0, basket, len(moves), 0)
    return answer

def doll_catch(arr, moves, t, basket, f, s):
    global answer
    cnt = s
    if t >= f:
        answer = cnt
        return 
    for i in range(len(arr)):
        if arr[i][moves[t]-1]:
            if basket and basket[-1] == arr[i][moves[t]-1]:
                cnt += 2
                basket.pop()
                arr[i][moves[t]-1] = 0
                while len(basket)>=2 and basket[-1] == basket[-2]:
                    basket.pop()
                    basket.pop()
                    cnt += 2
            else:
                basket.append(arr[i][moves[t]-1])
                arr[i][moves[t]-1] = 0
            break
    doll_catch(arr, moves, t+1, basket, f, cnt)