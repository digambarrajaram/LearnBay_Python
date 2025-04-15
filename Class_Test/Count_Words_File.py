import os

def count_words_in_file(file):
    try:
        os.path.exists(file)
        word_count = 0
        with open(file,'r') as fp:
            str1 = fp.readlines()
            for i in range(len(str1)):
                iterator_count = str(str1[i].strip())
                word_count = word_count + len(iterator_count.split(' '))
        fp.close()
        return f"The total words in the {file} are {word_count}"
    except FileNotFoundError:
        print(f"Error : {file} not found")
    

print(count_words_in_file("file.txt"))
print('=======================================')
print(count_words_in_file("file1.txt"))