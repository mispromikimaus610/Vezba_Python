sentence= "Test sentence to see which word is the longest"
words=sentence.split()
max=0

for i in words:
    if (len(i)>max):
        max=len(i)
        Longest_word=i
        
print(Longest_word)