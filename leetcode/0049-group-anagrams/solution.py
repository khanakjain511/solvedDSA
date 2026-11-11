# Runtime: 15 ms
# Memory: 22.7 MB

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            sorted_key = tuple(sorted(s))
            anagram_map[sorted_key].append(s)
            
        return list(anagram_map.values())
