class TwoSum:
    def __init__(self) -> None:
        pass

    # time complexity
    # because two nested loop that need to iterate all the element each time index in the first loop changed ---> O(n^2)
    def two_sum_brute_force(self, target: int, items: list[int]) -> list[int]:
        result = []
        for idx, i_value in enumerate(items):
            for jdx, j_value in enumerate(items[idx + 1:], idx + 1):
                if i_value + j_value == target:
                    result = [idx, jdx]
                    break
        return result

    # time complexity is O(n) because we only iterate array only once per element
    def two_sum_optimize(self, target: int, items: list[int]) -> list[int]:
        pass_dict = {}
        result = []
        for idx, i_value in enumerate(items):
            if target - i_value in pass_dict:
                result = [pass_dict[target - i_value], idx]
                break
            pass_dict[i_value] = idx
        return result

    def two_sum_two_pointer(self, target: int, items: list[int]) -> list[int]:
        sorted_items = sorted(items, key=None, reverse=False)
        f_pointer = 0
        s_pointer = len(items) - 1
        result = []
        while f_pointer != s_pointer:
            sum = sorted_items[f_pointer] + sorted_items[s_pointer]
            if sum == target:
                result = [f_pointer, s_pointer]
                break
            elif sum > target:
                s_pointer -= 1
                continue
            else:
                f_pointer += 1
                continue
        return result



def main():
    two_sum = TwoSum()
    print(two_sum.two_sum_brute_force(4, [1, 2, 3, 4]))
    print(two_sum.two_sum_optimize(4, [1, 2, 3, 4]))
    print(two_sum.two_sum_two_pointer(6, [3, 2, 4]))

main()