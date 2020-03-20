N = input()
S = input()

score = 0
for idx, value in enumerate(S):
    if value == 'O':
        if idx != 0 and S[idx - 1] == "O":
            bonus_score += 1
        else:
            bonus_score = 0
        score += idx + 1
        score += bonus_score
print(score)
