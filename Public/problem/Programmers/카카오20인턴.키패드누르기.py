def solution(numbers, hand):
    left_hand = 10
    right_hand = 12
    answer = ''
    left_flag = False
    right_flag = False
    for i in range(len(numbers)):
        if numbers[i] == 0:
            num = 11
        else:
            num = numbers[i]
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            answer += 'L'
            left_hand = numbers[i]
            left_flag = False
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            answer += 'R'
            right_hand = numbers[i]
            right_flag = False
        else:
            target_num = int(num/3.1)
            target_left = int(left_hand/3.1)
            target_right = int(right_hand/3.1)
            left_dist = abs(target_num - target_left)
            right_dist = abs(target_num - target_right)
            if left_flag == True:
                left_dist -= 1
            if right_flag == True:
                right_dist -= 1
            if left_dist > right_dist:
                answer += 'R'
                right_hand = num
                right_flag = True
            elif right_dist > left_dist:
                answer += 'L'
                left_hand = num
                left_flag = True
            elif right_dist == left_dist:
                if hand == 'left':
                    answer += 'L'
                    left_hand = num
                    left_flag = True
                else:
                    answer += 'R'
                    right_hand = num
                    right_flag = True
    return answer