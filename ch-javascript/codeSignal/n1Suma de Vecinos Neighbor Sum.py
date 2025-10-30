def solution(a):
    padded = [0] + a + [0]
    return [padded[i] + padded[i+1] + padded[i+2] for i in range(len(a))]
