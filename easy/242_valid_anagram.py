class ValidAnagram:

    def __init__(self):
        pass

    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = dict()

        if len(s) != len(t):
            return False

        i = 0
        while i < len(s):
            if s[i] in anagram_dict:
                anagram_dict[s[i]] = anagram_dict[s[i]] + 1
            else:
                anagram_dict[s[i]] = 1
            i += 1

        j = 0
        while j < len(s):
            if t[j] in anagram_dict:
                anagram_dict[t[j]] = anagram_dict[t[j]] - 1

            j += 1

        for _, value in anagram_dict.items():
            if value > 0:
                return False

        return True
    
    def is_anagram_neetcode_2nd_try(self, s: str, t: str) -> bool:
        have_seen = {}
        
        for char in s:
            if char in have_seen:
                have_seen[char] = have_seen[char] + 1
            else:
                have_seen[char] = 1
                
        
        for char in t:
            if char in have_seen:
                have_seen[char] = have_seen[char] - 1
                if have_seen[char] == 0:
                    del have_seen[char]
            else:
                have_seen[char] = 1
                
        return len(have_seen) == 0
    
solution = ValidAnagram()

print(solution.is_anagram_neetcode_2nd_try("anagram", "nagaram"))


print(sorted([(10, 1), (3, 2), (15, 4), (20, 5)], reverse=True)[:2])