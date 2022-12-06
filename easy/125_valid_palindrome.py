import re

class ValidPalindrom:
    def __init__(self) -> None:
        pass

    def isPalindrome(self, s: str) -> bool:
        if(len(s) <= 1):
            return True

        without_ws = re.sub(r"(\s+|_)", "",re.sub(r"[^\w+]", "", s.lower()))
        print(without_ws)

        s_len = len(without_ws)

        i = 0
        j = 0
        if s_len % 2 == 0:
            j = int(s_len / 2)
            i = int(s_len / 2) - 1
        else:
            j = int(s_len / 2) + 1
            i = int(s_len / 2) - 1

        while i >= 0:
            if without_ws[i] != without_ws[j]:
                return False
            i -= 1
            j += 1

        return True


def main() -> None:
    solution = ValidPalindrom()

    print(solution.isPalindrome("A man, a plan, a canal: Panama"))
    print(solution.isPalindrome("race a car"))
    print(solution.isPalindrome(""))
    print(solution.isPalindrome(" "))
    print(solution.isPalindrome("ab_a"))
    print(solution.isPalindrome("ab-a"))

main()