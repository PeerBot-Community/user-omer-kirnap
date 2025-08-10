def read_sentences(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()

def change_sentences(sentences):
    return [sentence.strip().upper() for sentence in sentences]

def main():
    sentences = read_sentences('omer.txt')
    modified_sentences = change_sentences(sentences)
    print(modified_sentences)

if __name__ == '__main__':
    main()