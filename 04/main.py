import math
def distance(p1, p2):
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]
    c = math.sqrt((a**2 + b**2))
    return c

# def get_movie_info():
#     #csatlalkozunk egy adatb-hoz
#     return("Total Recall", 1990, 7.5)


def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print("a ket pont kozotti tavolsag: {0:.3f}".format(distance(p1, p2)))

    #title, year, score = get_movie_info()

    #x, y = y x (elemcsere egyszerre)
if __name__ == '__main__':
    main()
