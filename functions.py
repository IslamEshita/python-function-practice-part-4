def max_num(num1, num2, num3):
    if num1 > num2:
        return max(num1, num3)
    else:
        return max(num2, num3)
    

print(max_num(8, 7, 9))



def mult_list(l):
    result = 1
    for item in l:
        result = result * item
    
    return result

print(mult_list([1, 2, 3, 4]))




def rev_string(s):
    length = len(s)
    if length == 0 or length == 1:
        return s
    else:
       return rev_string(s[1:]) + s[0]
    
print(rev_string('hello world'))



def num_within(num, range_low, range_high):
    if num < range_low or num > range_high:
        return False
    else:
        return True

print(num_within(4, 1, 3))






def pascal(n):
    def sum_in_list(l):
        sums = []
        i = 0
        while(i < len(l) - 1):
            item1 = l[i]
            item2 = l[i + 1]
            sum = item1 + item2
            sums.append(sum)
            i = i + 1

        return sums

    all_rows = []
    if n == 1:
        all_rows.append([1])
    elif n == 2:
        all_rows.append([1])
        all_rows.append([1, 1])
    else:
        all_rows.append([1])
        all_rows.append([1, 1])
        for i in range(2, n+1):
            l_prev = all_rows[i - 1]
            sums = sum_in_list(l_prev)
            row = []
            row.append(1)
            for item in sums:
                row.append(item)
            row.append(1)
            all_rows.append(row)

    for row in all_rows:
        print(row)
    print("'''")

pascal(1)
pascal(2)
pascal(10)

