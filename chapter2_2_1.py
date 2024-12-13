
def solution(array):
    result = -1
    sum = 0
    for i in range(len(array)):
        num = array[i]
        if num == 1:
            sum = sum + 1
            result = max(sum, result)
        else:
            sum = 0

    return result


if __name__ == '__main__':
    array = [1, 1, 0, 1, 1, 1]
    print(solution(array))
