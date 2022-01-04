
def solution(stones, k):

    '''
    맨처음에는 stones의 순서대로 진행
    그 다음부터는 가장 작은 돌무더기 찾아서 올려주면서, k개 돌이 있는 돌무더기가 한개 일때까지 진행
    k개 남으면 stones의 다음으로 진행
    '''
    result = []

    g_idx = 0
    init = True
    seq = ""
    stones_test = []
    while True:

        if init == True:
            stones_test = stones[:]
            print(g_idx)
            print(stones_test)
            stones_test[g_idx] += 1
            seq += str(g_idx)
            init = False

            for i in range(len(stones)):
                if g_idx == i:
                    continue
                stones_test[i] -= 1
            g_idx += 1
            print(stones_test)

        idx = 0
        val_min = min(stones_test)
        val_max = max(stones_test)
        if stones_test.count(val_min) < 2:
            idx = stones_test.index(val_min)
        else:
            idx = stones_test.index(val_max)

        seq += str(idx)
        stones_test[idx] += 1
        for i in range(len(stones)):
            if idx == i:
                continue
            stones_test[i] -= 1
        print(stones_test)
        print(g_idx)

        if stones_test.count(-1) > 0:
            seq = ""
            init = True
            continue

        if stones_test.count(k) == 1:
            print(seq)
            result.append(seq)
            seq = ""
            init = True
            continue

        if g_idx == len(stones) or len(seq) == len(stones):
            break

        continue

    answer = sorted(result)[-1]
    return answer if len(answer) == len(stones) else -1

def main():
    stones = [1, 3, 2]
    k = 3
    print(solution(stones, k))  # return ["022", "202"]


main()
