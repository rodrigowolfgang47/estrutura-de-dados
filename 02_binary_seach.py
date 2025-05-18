from typing import List

class Solution(object):
    def containsNearbyDuplicate(self, nums: List[int] , k:int) -> bool:
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #abs(i - j) <= k
        #nums[i] == nums[j]
        nums = self._list_treatment(nums)
        k = int(k)
        visto_por_ultimo = {}
        
        for i, num in enumerate(nums):
            if num in visto_por_ultimo and abs(i - visto_por_ultimo[num]) <= k:
                return True
            visto_por_ultimo[num] = i
        return False
            
    def _list_treatment(self, s_lista:str) -> List[int]:
        """This function transform a string list from input in interger list"""
        int_list = self._remove_char(s_lista)
        int_list = [int(n) for n in int_list]
        return int_list

    def _remove_char(self, int_list:str):
        int_list = int_list.replace("[", "").replace("]", "")
        if "," in int_list:
            int_list = int_list.split(sep=",")
        else:
            int_list = int_list.split()
        
        return int_list

################################ call program ################################

nums    = input("Int list:")
k       = input("Max next value in list:")

has_next_duplicate = Solution()
validation = has_next_duplicate.containsNearbyDuplicate(nums, k)
print(validation)