from DataStore import DataStore

if __name__ == "__main__":
    d1 = DataStore("d1","aaaa")
    d1['a']=10
    d1['b']=20

    ld1 = DataStore("d1","aaaa")
    ld1['a']=10
    ld1['b']=20
    print(ld1['a'])

    for key in ld1:
        print(key, ld1[key])