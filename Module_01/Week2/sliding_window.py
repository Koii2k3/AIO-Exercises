def sliding_window(num_list, k):
    for i in range(len(num_list)-k+1):
        for j in num_list[i:i+k]:
            print(j, end=' ')
        print(f'--> {max(num_list[i:i+k])}')
    

num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
sliding_window(num_list, k)
