def solve(s):
    result = ""
    new = s.split(" ")
    for i in new:
        result +=" "+i.capitalize()
        
    return result[1:] 
    
print(solve("hello     mohamed"))



       
       
         