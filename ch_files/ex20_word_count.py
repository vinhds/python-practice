def wordcount(filename):
    '''Takes a filename as input and print four lines of output:
    1 - Number of characters (including whitespace)
    2 - Number of words (separated by whitespace)
    3 - Number of lines
    4 - Number of unique words (case sensitive)'''
    with open(filename) as f:
        content = f.read()
        num_chars = len(content)
        content_lines = content.split('\n')
        num_lines = len(content_lines) - 1
        # content_lines_2 = [line for line in content_lines if line != '']
        # content_words = [lines.split(' ') for lines in content_lines_2]
        # content_words_2 = [word for word_list in content_words for word in word_list]
        # num_words = len(content_words_2)
        # num_unq_words = len(set(content_words_2))
        content_words = content.split()
        num_words = len(content_words)
        num_unq_words = len(set(content_words))
    print(f"The file {filename} contains {num_chars} characters.")
    print(f"The file {filename} contains {num_lines} lines.")
    print(f"The file {filename} contains {num_words} words and {num_unq_words} different words.")
if __name__ == "__main__":
    wordcount('wcfile.txt')
