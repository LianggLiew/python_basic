s1 = input('请输入一个字符串：')
s2 = input('请输入一个字符串：')


def find_lcs(s1, s2):
    m = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]
    mmax = 0
    p =0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                m[i+1][j +1]=m[j][i]+1
                if m[i+1][j+1] > mmax:
                    mmax = m[i+1][j+1]
                    p = i + 1
    print(f'公子串长度：{mmax}，公子串为:{s1[p-mmax:p]}.')

find_lcs(s1, s2)
