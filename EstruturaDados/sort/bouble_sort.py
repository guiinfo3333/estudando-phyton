

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


if __name__ == '__main__':
    alist = []

    for i in range(100000, 0, -1):
        alist.append(i)

    bubbleSort(alist)
    print(alist)