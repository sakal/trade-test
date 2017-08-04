#!/usr/bin/python3

def get_input_values():
    N = 0
    parts = []
    N = int(input())
    for i in range(N):
        x = float(input())
        parts.append(x)

    return N, parts

def calculate(n, parts):
    total = sum(parts)
    result = [k for k in map(lambda x: "{:.3f}".format( ( 100.0 / ( total / x ) ) * 0.01 ), parts)]
    return result

def main():
    N, parts = get_input_values()
    result = calculate(N, parts)
    print()
    for item in result:
        print(item)

if '__main__' == __name__:
    main()

