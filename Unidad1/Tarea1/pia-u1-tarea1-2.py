import re

words_list = ["hello", "world", "house", "car", "python"]

print("Input list: " + str(words_list))

def get_dictionary(wordsList, filePath):
    wordsDictionary = {}
    
    wordsList.sort()
    
    with open(filePath, 'r', encoding='utf-8') as f:
        content = f.read().lower()

    file_content_formatted = re.sub(r'[^\w\s]', '', content)

    for word in wordsList:
        wordsDictionary[word] = file_content_formatted.count(word)

    return wordsDictionary
    
print("Final dictionary: " + str(get_dictionary(words_list, 'textFile.txt')))
