
def pathway(in_s):
     arr = []

     Y = 0
     X = in_s[0].index("S")

     # the abs(Y-9) is used so that the recorded Y value matches the diagram
     arr.append((X,abs(Y-9)))

     Y = 1 # will always be directly beneath start

     itm = in_s[Y][X]
     #print('"'+itm+'"')
     arr.append((X,abs(Y-9)))
    
     while itm!="E":
          
          b = True
          
          # check left
          if X-1 > -1 and b: # make sure you're not at the very left
               if in_s[Y][X-1]!="X" and (X-1,abs(Y-9)) not in arr:
                    #print('"'+in_s[Y][X-1]+'"')
                    X-=1
                    b = False
          
          # check right
          if X+1 < 10 and b: # make sure you're not at the very right
               if in_s[Y][X+1]!="X" and (X+1,abs(Y-9)) not in arr:
                    #print('"'+in_s[Y][X+1]+'"')
                    X+=1
                    b = False
          
          # check down
          if Y+1 < 10 and b: # make sure you're not at the very bottom
               if in_s[Y+1][X]!="X"  and (X,abs(Y-8)) not in arr:
                    #print('"'+in_s[Y+1][X]+'"')
                    Y+=1
                    b = False
          
          # check up
          if Y-1 > -1 and b: # make sure you're not at the very top
               if in_s[Y-1][X]!="X"  and (X,abs(Y-10)) not in arr:
                    #print('"'+in_s[Y-1][X]+'"')
                    Y-=1
                    b = False
          
          arr.append((X,abs(Y-9)))
          itm = in_s[Y][X]

     return arr

in_s = [["X","X","X","S","X","X","X","X","X","X"],
        ["X","X","X"," ","X","X","X","X","X","X"],
        ["X","X","X"," "," ","X"," "," "," ","X"],
        ["X","X","X","X"," "," "," ","X"," ","X"],
        ["X","X","X","X","X","X","X","X"," ","X"],
        ["X","X","X","X","X"," "," "," "," ","X"],
        ["X","X","X","X"," "," ","X","X","X","X"],
        ["X","X","X","X"," ","X","X","X","X","X"],
        ["X","X","X","X"," ","X","X","X","X","X"],
        ["X","X","X","X","E","X","X","X","X","X"]]

print(pathway(in_s))