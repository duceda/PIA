import re

words_list = ["hello", "world", "house", "car", "python"]

print("Input list: " + str(words_list))

words_list.sort()

print("Sorted list: " + str(words_list))

def content_file_format(contentFile):
    no_punctuation = re.sub(r'[^\w\s]', '', contentFile)
    return no_punctuation

with open('textFile.txt', 'r', encoding='utf-8') as f:
    content = f.read().lower()

fileContentFormatted = content_file_format(content)
print("File content Formatted: " + fileContentFormatted)

wordsDictionary = {}

for word in words_list:
    wordsDictionary[word] = fileContentFormatted.count(word)
    
print("Final dictionary: " + str(wordsDictionary))
