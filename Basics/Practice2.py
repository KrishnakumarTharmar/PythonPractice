def average(array):
    # your code goes here
    my_array=set(array)
    avg=sum(my_array)/len(my_array)
    return avg
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
