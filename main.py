# python3

def parallel_processing(n, m, data):
    output = []
    threads = [[0, ] for i in range(n)]

    for i in range(m):
        time = data[i]
        next_thread = min(threads)
        output.append((next_thread[1], next_thread[0]))
        next_thread[0] += time

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    result = parallel_processing(n,m,data)
    
    for i, j in result:
        print(str(i) + " " + str(j))


if __name__ == "__main__":
    main()
