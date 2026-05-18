import csv

import numpy as np


def WynnEpsilon(sn, k):
    n = 2 * k + 1
    e = np.zeros((n+1, n+1))

    for i in range(1, n+1):
        e[i, 1] = sn[i-1]

    for i in range(3, n+2):
        for j in range(3, i+1):
            e[i-1, j-1] = e[i-2, j-3] + 1/(e[i-1, j-2] - e[i-2, j-2])

    ek = e[:, 1:n + 1:2]
    return ek

# --------------------------------------------------
def main():

    n  = np.logspace(0,8,9,base=2).astype(int)
    pn = n*np.sin(np.pi/n)

    pw = np.zeros(4)
    for i in range(1,5):
        en = WynnEpsilon(pn,i)
        pw[i-1] = en[-1, -1]

    print ("{:<5} {:<20} {:<20}".format('n','Pi-n','Pi-Wynn'))
    for k in range(n.size):
        if (k%2 == 0 and k>0):
            i = int(k/2)
            print("{:<5} {:.15f}    {:.15f}".format(n[k], pn[k], pw[i-1]))
        else:
            print ("{:<5} {:.15f}".format(n[k], pn[k]))

    with open('pi_approximation.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # 写入表头
        writer.writerow(['n', 'Pi-n', 'Pi-Wynn'])
        # 写入数据
        for k in range(n.size):
            if k % 2 == 0 and k > 0:
                idx = int(k / 2) - 1
                if idx < len(pw):
                    writer.writerow([n[k], pn[k], pw[idx]])
                else:
                    writer.writerow([n[k], pn[k], ''])
            else:
                writer.writerow([n[k], pn[k], ''])
    print("✅ 数据已写入 pi_approximation.csv\n")

# --------------------------------------------------
if __name__ == '__main__':
    main()