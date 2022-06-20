class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mas = digits[::-1]
        for i in range(len(mas)):
            if mas[i] == 9:
                mas[i] = 0
                if i == len(mas) - 1:
                    mas.append(1)
            else:
                mas[i] += 1
                break
        return mas[::-1]
            
        