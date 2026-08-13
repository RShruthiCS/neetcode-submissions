class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_strs = {}
        for char in strs:
            char_sort = "".join(sorted(char))
            if char_sort in grp_strs:
                grp_strs[char_sort].append(char)
            else: 
                grp_strs[char_sort] = [char]
        return list(grp_strs.values())