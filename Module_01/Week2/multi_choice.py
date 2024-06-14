def max_kernel(num_list, k):
    res = []
    for i in range(len(num_list)-k+1):
        res.append(max(num_list[i:i+k]))
    return res


assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))
# 1A
####################################################################


def character_count(word):
    return {char: word.count(char) for char in list(word)}


assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))
# 2A
####################################################################


def count_word(file_path):
    with open(file_path) as f:
        string = f.read()
    string = string.lower().split()
    return {word: string.count(word) for word in string}


file_path = './P1_data.txt'
result = count_word(file_path)
assert result['who'] == 3
print(result['man'])
# 3C
####################################################################


def levenshtein_distance(src, tar):
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

    return float(D[len_src-1][len_tar-1])


assert levenshtein_distance("hi", "hello") == 4
print(levenshtein_distance("hola", "hello"))
# 4C
####################################################################


def check_the_number(n):
    list_of_numbers = []
    results = ""
    for i in range(1, 5):
        list_of_numbers.append(i)
    if n in list_of_numbers:
        results = "True"
    if n not in list_of_numbers:
        results = "False"
    return results


N = 7
assert check_the_number(N) == "False"
N = 2
results = check_the_number(N)
print(results)
# 5A
####################################################################


def my_function(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


my_list = [5, 2, 5, 0, 1]
max = 1
min = 0
assert my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
my_list = [10, 2, 5, 0, 1]
max = 2
min = 1
print(my_function(max=max, min=min, data=my_list))
# 6C
####################################################################


def my_function(x, y):
    x.extend(y)
    return x


list_num1 = ['a', 2, 5]
list_num2 = [1, 1]
list_num3 = [0, 0]
assert my_function(list_num1, my_function(list_num2, list_num3)) == [
    'a', 2, 5, 1, 1, 0, 0]

list_num1 = [1, 2]
list_num2 = [3, 4]
list_num3 = [0, 0]

print(my_function(list_num1, my_function(list_num2, list_num3)))
# 7A
####################################################################


def my_function(n):
    min_num = n[0]
    for i in n:
        if i < min_num:
            min_num = i
    return min_num


my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100
my_list = [1, 2, 3, -1]
print(my_function(my_list))
# 8C
####################################################################


def my_function(n):
    max_num = n[0]
    for i in n:
        if i > max_num:
            max_num = i
    return max_num


my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001
my_list = [1, 9, 9, 0]
print(my_function(my_list))
# 9D
####################################################################


def my_function(integers, number=1):
    return any([True if num == number else False for num in integers])


my_list = [1, 3, 9, 4]
assert my_function(my_list, -1) == False
my_list = [1, 2, 3, 4]
print(my_function(my_list, 2))
# 10C
####################################################################


def my_function(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var/len(list_nums)


assert my_function([4, 6, 8]) == 6
print(my_function())
# 11A
####################################################################


def my_function(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


assert my_function([3, 9, 4, 5]) == [3, 9]
print(my_function([1, 2, 3, 5, 6]))
# 12A
####################################################################


def my_function(y):
    var = 1
    while (y > 1):
        var *= y
        y -= 1
    return var


assert my_function(8) == 40320
print(my_function(4))
# 13C
####################################################################


def my_function(x):
    return x[::-1]


x = 'I can do it'
assert my_function(x) == "ti od nac I"
x = 'apricot'
print(my_function(x))
# 14B
####################################################################


def function_helper(x):
    return 'T' if x > 0 else 'N'


def my_function(data):
    res = [function_helper(x) for x in data]
    return res


data = [10, 0, -10, -1]
assert my_function(data) == ['T', 'N', 'N', 'N']

data = [2, 3, 5, -1]
print(my_function(data))
# 15C
####################################################################


def function_helper(x, data):
    for i in data:
        if x == i:
            return 0
    return 1


def my_function(data):
    res = []
    for i in data:
        if function_helper(i, res):
            res.append(i)

    return res


lst = [10, 10, 9, 7, 7]
assert my_function(lst) == [10, 9, 7]

lst = [9, 9, 8, 1, 1]
print(my_function(lst))
# 16A
