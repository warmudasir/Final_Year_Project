import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

file_path = 'recommend/data/input/data.csv'
encoding = detect_encoding(file_path)
print(f'The file is encoded in {encoding}')
