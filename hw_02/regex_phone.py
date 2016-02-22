import re
import helper

with open('test_dollar_phone_corpus.txt', 'r') as input_file:
    corpus = input_file.read()

with open('output_phone.txt', 'w') as output_file:
    corpus = re.sub(r'\(\d\d\d\)\s\d{3}[-.]\d{4}', helper.bracket_it, corpus)
    output_file.write(corpus)

with open('phone.txt', 'w') as output_file:
    pass_1 = re.findall(r'\(\d\d\d\)\s\d{3}[-.]\s?\d{4}', corpus)
    output_file.write('\n'.join(pass_1))

input_file.close()
output_file.close()