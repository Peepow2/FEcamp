import random
# ----------------------------- #
def stable_choice(L):
    if L == []: return False
    for i in range(1, 6):
        if not (4 <= L.count(i) <= 6):
            return False
    return True

def GEN_TESTCASE():
    L = list()
    N = 0
    while not stable_choice(L):
        N += 1
        L = [int(((random.random()) * 317) % 5) + 1 for i in range(25)]

    for i in range(5):
        ANS = (str(((int(random.random() * 1e6) + 623571) % int(1e6))) + '000000')[0:6]
        ANS = ANS[:4] + '.' + ANS[4:]
        L.append(ANS)
    return L

def Answer_sheet_check():
    L = [1, 2, 1, 2, 4, 2, 5, 2, 3, 4, 5, 5, 4, 1, 4, 3, 5, 1, 1, 5, 3, \
         4, 3, 5, 4, '1426.60', '1690.55', '6985.43', '3624.19', '1217.33']
    return 

def Scoreing(A, Sol):
    S = 0
    for i in range(25): S += (A[i] == Sol[i]) * 3
    for i in range(5):  S += (A[i] == Sol[i]) * 5
    return S
# ----------------------------- #
Solution = GEN_TESTCASE()
Ans = Answer_sheet_check()
Score = Scoreing(Ans, Solution)
print(Score)
