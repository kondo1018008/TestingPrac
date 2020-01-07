import math

class procon:
    def Procon(m1, m2):
        g = math.gcd(m1, m2)

        s = {}
        if m1 > m2:
            d = 0
            for i in range(1, m1 + 1):
                if m1 % i == 0 and m2 % i == 0:
                    s[i] = True
                else:
                    s[i] = False
            for i in reversed(range(1, m1 + 1)):
                if d == 1 and s[i] == True:
                    print(i)
                    return i
                    break
                if s[i] == True:
                    d += 1

        else:
            d = 0
            for i in range(1, m2 + 1):
                if m1 % i == 0 and m2 % i == 0:
                    s[i] = True
                else:
                    s[i] = False
            for i in reversed(range(1, m2 + 1)):
                if d == 1 and s[i] == True:
                    print(i)
                    return i
                    break
                if s[i] == True:
                    d += 1
        # print(s)

"""
講義名：ソフトウェア設計論
作成日：2020年1月6日
このプログラムは、二つの数の二番目に大きい公約数を求めるプログラムである。
"""