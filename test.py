def min_mul():
    num_list = map(int, raw_input().split())
    a_bit = int(raw_input())
    b_bit = int(raw_input())

    use_list = []
    total_bit = a_bit + b_bit
    for i in range(10):
        total_bit -= num_list[i]
        if total_bit <= 0:
            use_list.append(num_list[i] + total_bit)
            break
        use_list.append(num_list[i])

    nums = []
    for i in range(len(use_list)):
        for j in range(use_list[i]):
            nums.append(i)

    all_comb = permute(nums)
    min_result = 2**32-1

    for num_l in all_comb:
        a_num = 0
        for i in range(a_bit):
            a_num = a_num * 10 + num_l[i]
        assert len(num_l) == a_bit + b_bit
        b_num = 0
        for i in range(a_bit, a_bit + b_bit):
            b_num = b_num * 10 + num_l[i]
        result = a_num * b_num
        if result < min_result:
            min_result = result
        if min_result == 0:
            break

    return min_result


def permute(nums):
    res = [[]]

    for num in nums:
        new_res = []
        for i in range(len(res)):
            prev = res[i]
            prev.append(num)
            for j in range(len(prev)):
                prev[j], prev[-1] = prev[-1], prev[j]
                new_res.append(prev[:])
                prev[j], prev[-1] = prev[-1], prev[j]
        res = new_res
    return res

print min_mul()