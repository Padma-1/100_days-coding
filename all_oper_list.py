if __name__ == '__main__':
    N = int(input())
    list1 = []
    for i in range(N):
        x = input().split(" ")
        command  = x[0]
        if command == "insert":
            list1.insert(int(x[1]),int(x[2]))
        elif command == "print":
            print(list1)
        elif command == "remove":
            list1.remove(int(x[1]))
        elif command == "append":
            list1.append(int(x[1]))
        elif command == "sort":
            list1.sort()
        elif command == "pop":
            
                list1.pop()
        elif command == "reverse":
            list1.reverse()
        
