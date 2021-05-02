def intersect(nums1, nums2):
    n1_d = {}
    n2_d = {}

    for num in nums1:
        n1_d[num] = n1_d.get(num, 0) + 1

    for num in nums2:
        n2_d[num] = n2_d.get(num, 0) + 1

    common_values = []

    for k, v in n1_d.items():
        common_values += min(v, n2_d.get(k, 0)) * [k]

    return common_values

print(intersect([1,2,2,1], [2,2]))
