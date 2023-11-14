def elevationMapping(elevations, N,M):
     Y = 0
     X = 0
     arr = []
     itm = ""
     height = 0

     while len(arr) < M:
          itm = elevations[Y][X]
          
          if itm == "^":
               height+=1
          
          # once ground is reached reset and increment X else keep going down
          if Y == N: 
               Y = 0  
               X+=1
               arr.append(height)
               height = 0
          else:
               Y+=1  

     return arr

in_s = [[" ","^"," "," "," "," "," "," "," "," "],
       ["^","^"," "," "," "," ","^"," "," "," "],
       ["^","^"," "," "," "," ","^"," "," "," "],
       ["^","^","^"," "," "," ","^","^"," "," "],
       ["^","^","^","^"," ","^","^","^","^"," "],
       ["-","-","-","-","-","-","-","-","-","-"]]
  
print(elevationMapping(in_s, 5,10))
