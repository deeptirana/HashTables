class Solution(object):
    def countConsistentStrings(self, allowed, words):
        cnt=0
        a = set(allowed)
        for w in words:
            for c in w:
                if c not in a:
                    cnt+=1
                    break
                
        return len(words)-cnt   
