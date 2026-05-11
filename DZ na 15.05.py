# ОНО - это количество подсток в строке
S = input()
ans = set()
for i in range(1, len(S)):
    for j in range(len(S)-i+2):
        ans.add(S[j:i+j])
print(len(ans))