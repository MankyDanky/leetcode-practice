class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        l = []

        self.generate_happy_strings(n, "", l)

        if k > len(l):
            return ""
        
        return l[k-1]
    
    def generate_happy_strings(self, n, current_string, happy_strings):
        if len(current_string) == n:
            happy_strings.append(current_string)
            return

        for curr in ['a', 'b', 'c']:
            if len(current_string) > 0 and current_string[-1] == curr:
                continue
            
            self.generate_happy_strings(n, current_string + curr, happy_strings)
        