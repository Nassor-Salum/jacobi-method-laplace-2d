import matplotlib.pyplot as plt

n = 100
dt = 0.001
dx = dy = 1 / n
itt = 0

P = []

for i in range(n):
    Pr = []
    for j in range(n):
        if (j == 0 and (35 <= i <= 65)) or (i == n - 1 and (0 <= j <= 30)):
            Pr.append(1)
        else:
            Pr.append(0)
    P.append(Pr)

xlist = [dx * i for i in range(n)]
ylist = [dx * j for j in range(n)]

while True:
    Pn = []
    diff = 0
    for i in range(n):
        Pr = []
        for j in range(n):
            if (j == 0 and (35 <= i <= 65)) or (i == n - 1 and (0 <= j <= 30)):
                Pr.append(1)
            else:
                Pr.append(0)
        Pn.append(Pr)

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            Pn[i][j] = 1 / 4 * (P[i + 1][j] + P[i - 1][j] + P[i][j + 1] + P[i][j - 1])
            diff = max(diff, abs(Pn[i][j] - P[i][j]))
    itt += 1

    P = Pn

    if itt % 1000 == 0:
        print("I am still alive, peach", itt)
        plt.contourf(xlist, ylist, P)
        plt.show()

    if diff < 0.00001:
        break

print(itt)
plt.contourf(xlist, ylist, P)
plt.show()
