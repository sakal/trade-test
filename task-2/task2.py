#!/usr/bin/python3

def get_input_values():
    
    N = 0  # count of trading days
    M = 0  # count of lots
    S = 0  # amount of money
    
    in_records = []
    record = None

    N, M, S = [int(x) for x in input().split(" ") if x]

    
