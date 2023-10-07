class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
      g.sort()
      s.sort()
      fg=fs=0
      while fg<len(g) and fs<len(s):
        if s[fs]>=g[fg]:
          fg+=1
        fs+=1
      return fg
