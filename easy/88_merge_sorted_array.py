class MergeSortArray:
    def __init__(self) -> None:
        pass

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        a, b, write_index = m-1, n-1, m + n - 1

        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[write_index] = nums1[a]
                a -= 1
            else:
                nums1[write_index] = nums2[b]
                b -= 1

            write_index -= 1
        
        # remove when submitted
        return nums1



def main():
    solution = MergeSortArray()

    print(solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
    print(solution.merge([4,5,6,0,0,0], 3, [1,2,3], 3))
    print(solution.merge([1], 1, [], 0))
    print(solution.merge([0], 0, [1], 1))

main()