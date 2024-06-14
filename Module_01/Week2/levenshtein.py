def levenshtein(src, tar):
    del_cost = 1
    ins_cost = 1

    def sub_cost(src_idx, tar_idx):
        cost = 1
        if src[src_idx-1] == tar[tar_idx-1]:
            cost = 0
        return cost

    # Step 1
    len_src = len(src) + 1
    len_tar = len(tar) + 1
    D = [[]*len_tar]*len_src

    # Step 2
    D[0] = [i for i in range(len_tar)]
    for i in range(1, len_src):
        D[i] = [i] + [0] * (len_tar-1)

    # Step 3
    for i in range(1, len_src):
        for j in range(1, len_tar):
            tar_del = D[i-1][j] + del_cost
            src_ins = D[i][j-1] + ins_cost
            sub = D[i-1][j-1] + sub_cost(i, j)
            D[i][j] = min(tar_del, src_ins, sub)

    return D[len_src-1][len_tar-1]


print(levenshtein('yu', 'you'))
print(levenshtein('I', 'you'))
print(levenshtein('love', 'you'))
