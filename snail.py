#  https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python


def snail(snail_map):
    if not snail_map:
        return []
    if not snail_map[0]:
        return []
    res_list = []
    current_move = 'forward'
    current_step = 0

    while len(res_list) < (len(snail_map)**2):

        if current_move == 'forward':
            for index in range(current_step, len(snail_map)-current_step):
                res_list.append(snail_map[current_step][index])
            current_move = 'down'

        if current_move == 'down':
            for index in range(current_step+1, len(snail_map)-current_step):
                element = snail_map[index][len(snail_map)-current_step-1]
                res_list.append(element)
            current_move = 'back'

        if current_move == 'back':
            for index in range(current_step+1, len(snail_map)-current_step):
                res_list.append(snail_map[len(snail_map)-current_step-1][-(index+1)])
            current_move = 'up'

        if current_move == 'up':
            for index in range(current_step+1, len(snail_map)-current_step-1):
                res_list.append(snail_map[index][current_step])
            current_step += 1
            current_move = 'forward'
    return res_list
