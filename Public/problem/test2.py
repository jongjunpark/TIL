def solution(board, moves):
    answer = 0
    basket = []
    doll_catch(board, moves, 0, basket, len(moves))
    answer = len(basket)
    print(answer)
    return answer

def doll_catch(arr, moves, t, basket, f):
    if t >= f:
        return
    for i in range(len(arr)):
        if arr[i][moves[t]-1]:
            if basket and basket[-1] == arr[i][moves[t]-1]:
                basket.pop()
                arr[i][moves[t]-1] = 0
                while len(basket)>=2 and basket[-1] != basket[-2]:
                    basket.pop()
                    basket.pop()
            else:
                basket.append(arr[i][moves[t]-1])
                arr[i][moves[t]-1] = 0
            break
    doll_catch(arr, moves, t+1, basket, f)

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)
            
            