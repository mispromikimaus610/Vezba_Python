string="hello world hello test test world hi hello"
print(string)
words=string.split()
word_count={}

for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)