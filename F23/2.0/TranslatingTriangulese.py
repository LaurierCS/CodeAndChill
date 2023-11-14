def tri(in_s): 
     out_s = ""
     count = 0

     for lttr in in_s:
          if lttr.isalpha():
               for j in range(count+1):
                    if count==0:
                         out_s+=lttr.upper()
                    else:
                         out_s+=lttr
               count+=1
               out_s+="\n"
          elif lttr.isspace(): count = 0

     return out_s

in_s = "Hello, how are you?"
print(tri(in_s))