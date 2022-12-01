class LongerCommonPrefix:
    def __init__(self) -> None:
        pass

    def longer_common_prefix_brute_force(self, strs: list[str]) -> str:
        shortest_str = sorted(strs, key=len)[0]
        common_prefix = ""
        
        for i_value in shortest_str:
            prefix = common_prefix + i_value
            contain_common_prefix = True
            for jdx, j_value in enumerate(strs):
                if j_value.startswith(prefix) == False:
                    contain_common_prefix = False
                    break
            if contain_common_prefix == True:
                common_prefix = prefix
            elif contain_common_prefix == False:
                break
        return common_prefix

def main():
    solution = LongerCommonPrefix()
    print(solution.longer_common_prefix_brute_force(["flower","flow","flight"]))
    print(solution.longer_common_prefix_brute_force(["dog","racecar","car"]))

main()