if __name__ == '__main__':
    list=[]
    N = int(input())
    for i in range(N):
        y=input()
        if "insert" in y:
            yy=y.split()
            list.insert(int(yy[-2]),int(yy[-1]))
        if "remove" in y:
            yy=y.split()
            list.remove(int(yy[-1]))
        if "append" in y:
            yy=y.split()
            list.append(int(yy[-1]))
        if "print" in y:
            print(list)
        if "sort" in y:
            list.sort()
        if "reverse" in y:
            list.reverse()
        if "pop" in y:
            list.pop()
