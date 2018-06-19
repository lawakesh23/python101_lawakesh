def python101_range(start, stop="NOT_GIVEN", step=1):
    
    if stop == "NOT_GIVEN":
        stop=start
        start=0
    while start < stop:
        yield start
        start+=step

for i in python101_range(1,10,2):
print(i)
