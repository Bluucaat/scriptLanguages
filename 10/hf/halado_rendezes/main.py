
def my_func1(t):
    return t[-1]

def my_func2(user: str) -> int:
 return int(user.split(":")[0])

def main():
    data = [
        (1, 'Albany', 'NY', 162692),
        (121, 'Wyoming', 'NY', 8722),
        (3, 'Allegany', 'NY', 11982),
        (123, 'Yates', 'NY', 5094)
    ]
    result = sorted(data, key=my_func1)
    result2 = sorted(data, key=lambda t: t[-1])
    print(result2)


    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User5']


    result3 = sorted(users, key=my_func2, reverse=True)
    result4 = sorted(users, key=lambda user: int(user.split(":")[0]), reverse=True)
    print(result4)

    matrix = [ [2, 6], [1, 3], [5, 4] ]

    sorted_matrix = sorted(matrix, key=lambda x: x[1])

    print(sorted_matrix)




if __name__ == '__main__':
    main()