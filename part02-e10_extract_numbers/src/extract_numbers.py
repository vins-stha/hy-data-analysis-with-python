#!/usr/bin/env python3

def extract_numbers(s):
    #print(s.split())
    #words =[x.split() for x in s]
    items = s.split()
    nums = []

    for item in items:
        try:
            nums.append(int(item))
        except ValueError:
            try:
                nums.append(float(item))
            except ValueError:
                continue


    return nums

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
