class Solution:
    
    def reverseWord_manual(self, word):
        res = ''
        left, rigth = 0, 0
        
        while rigth < len(word):
            if word[rigth] != ' ':
                rigth += 1
            else:
                res += word[left:rigth+1][::-1]
                rigth += 1
                left = rigth
            
        #print("string antes da ultima palavra-----",res)
        res += ' '
        res += word[left:rigth + 2][::-1]               
        #print("string depois da ultima palavra-----",res)
        res_trim = res[1:]
        
        return res_trim, len(res_trim)


palavra_invertida, quant = Solution.reverseWord_manual("arvalap oremun mu ed")
print(f"Palavra invertida = {palavra_invertida}\nLetas = {quant}")