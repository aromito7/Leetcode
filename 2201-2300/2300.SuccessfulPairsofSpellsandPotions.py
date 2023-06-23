class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted([(potion + success - 1)//potion for potion in potions])
        
        output = []
        length = len(potions)
        #print(potions)
        for spell in spells:
            #print(spell)
            start = 0
            end = length - 1
            middle = (end + start)//2

            if spell >= potions[end]:
                output.append(length)
                continue
            elif spell < potions[0]:
                output.append(0)
                continue
            elif length == 2:
                output.append(1)

            while start < middle < end:
                #print(start, middle, end)
                if spell >= potions[middle]:
                    if spell < potions[middle + 1]:
                        output.append(middle + 1)
                        break
                    else:
                        start = middle
                        middle = (end + start)//2
                elif spell < potions[middle]:
                    if spell >= potions[middle - 1]:
                        output.append(middle)
                        break
                    else:
                        end = middle
                        middle = (end + start)//2

        
        return output
             
