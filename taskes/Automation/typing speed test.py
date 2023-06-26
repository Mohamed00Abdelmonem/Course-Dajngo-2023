import time
import re
def check (tests,innputmain):
    right = 0
    for i in range(len(tests)):
        try:
            if tests[i]==innputmain[i]:
                right+=1
        except Exception:
            break
    return right
tests = "hello mohamed abdelmonem."
tests_split = re.split("\s",tests)
print(tests)
t1 = time.time()
inputmain = str(input())
t2 = time.time()
inputmain = re.split("\s",inputmain)
rightwords = check(tests_split,inputmain)
print("this is your typing speed",(rightwords/((t2-t1)/60)))
print("your accuracy was ",rightwords/len(tests_split)*100)