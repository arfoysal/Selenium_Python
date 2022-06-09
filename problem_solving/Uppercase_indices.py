test_str = "I am Foysal and Love Automation"

print("The original string is : " + test_str)
res = []
for idx in range(len(test_str)):
    if test_str[idx].isupper():
        res.append(idx)

print(res)