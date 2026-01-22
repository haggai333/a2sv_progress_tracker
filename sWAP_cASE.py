def swap_case(s):
    a=''
    for i in s:
        if i.isupper():
            a+=i.lower()
            continue
        if i.islower():
            a+=i.upper()
            continue
        a+=i
    return a
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)