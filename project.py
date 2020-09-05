words=["Hello","world","!"]
print(words[0])
print(words[1])
print(words[2])
print(words)

m=[
    [1,2,3],
    [4,5,6]
    ]
print(m[1][2])
str="Hello word!"
print(str[6])    

nums=[7,7,7,7,7]
nums[2]=5
print(nums)

print(nums+[4,5,6])
print(nums*3)

print("Hello"in words)
print("world" in words)
print("?" in words)

print(not "hey" in words)
print(not "!" in words)

words.append("hey!")
print(words)

print(len(words))

index=1
words.insert(index,"hey")
print(words)

print(words.index("Hello"))