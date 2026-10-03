def uniformArray(nums1: list[int]) -> bool:
    nums1.sort()
    m = nums1[0]
    typ = None
    if m%2 == 0:
        typ = "even"
    else:
        typ = "odd"

    if typ == "odd":
        return True
    else:
        for i in nums1[1:]:
            if i%2 != 0:
                return False
            else:
                pass
        return True