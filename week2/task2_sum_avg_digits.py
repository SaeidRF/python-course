s1 = "S2A4E9I2D"
total = 0
count = 0
for x in s1:
    if x.isdigit():
        total+= int(x)
        count +=1
print("sum:", total)
print("count:", count)
if count > 0:
    average = total / count
    print("average:", average)
else:
    print("no digits found")

