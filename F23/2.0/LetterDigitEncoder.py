def letterDig(in_s):
     out_s = ""
     LETTERS = "aBcDeFgHi"

     for i in in_s:
          if i.isalpha(): # is a letter
               out_s+=str(ord(i))
          else:
               if int(i)==0:
                    out_s+="Z"
               else:
                    out_s+=LETTERS[int(i)-1]

     return out_s

in_s = "2fHj1458oMaa030"
print(letterDig(in_s))