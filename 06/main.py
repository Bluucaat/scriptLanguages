def main():
    h = sorted({5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5})


    a = ["alma", "banan", "citrom"]

    d = {"a": "alpha", "b": "beta", "g": "gamma", "d": "delta"}
    print(d.get('x', "NOT FOUND"))

    for k in d:
        print(k + " --> " + d[k])

    for k in sorted(d):
        print(k + " --> " + d[k])

    for k, v in d.items():
        print(k, v)

    del d["k" , ""]
    
    



if __name__ == '__main__':
    main()