class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        array = list(t)
        start_index = 0
        end_index = len(array)
        try:
            for i in s:
                start_index = array.index(i, start_index) + 1
                print(start_index)
        except ValueError:
            return False
        return True
        

            
