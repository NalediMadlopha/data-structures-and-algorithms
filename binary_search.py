import sys


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def get_input():
    input_second = [int(x) for x in sys.stdin.readline().split()]
    input_third = [int(x) for x in sys.stdin.readline().split()]

    return input_second, input_third


def main():
    arr, queries = get_input()

    for x in queries:
        if binary_search(arr, 0, len(arr) - 1, x) != -1:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    main()
