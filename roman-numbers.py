class Solution:
    def romanToInt(self, s: str) -> int:
        roman={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        previous = 0
        numRoman = 0


        for item in s:
            num=item.replace(item,str(roman[item]))
            current=int(num)

            print(previous,current)

            if(previous >= current or previous == 0):
             numRoman += current
             previous = current
             

            if(current > previous):
             thisNum = current - (previous * 2)
             numRoman += thisNum  
             previous = current     
        
        


        return numRoman

Solution.romanToInt("III","III")