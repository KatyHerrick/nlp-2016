import re
import helper


with open('test_dollar_phone_corpus.txt', 'r') as input_file:
    corpus = input_file.read()

with open('output_dollar.txt', 'w') as output_file:
    corpus = re.sub(r'\$\d+(?:,\d\d\d)*(?:\.\d\d)?', helper.bracket_it, corpus)
    corpus = re.sub(r'(?:\d+(?:,\d\d\d)*(?:\.\d\d)?) *dollars?', helper.bracket_it, corpus)
    corpus = re.sub(r'(?:a|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety) +(?:\b.{0,10}) *dollars?',
        helper.bracket_it, corpus)
    output_file.write(corpus)

with open('dollar.txt', 'w') as output_file:
    # returns expressions starting with a '$' symbol
    pass_1 = re.findall(r'\$\d+(?:,\d\d\d)*(?:\.\d\d)?', corpus)
    # returns expressions with numerical reps followed by 'dollars'
    # e.g. 3000 dollars
    pass_2 = re.findall(r'(?:\d+(?:,\d\d\d)*(?:\.\d\d)?) *dollars?', corpus)
    # returns expressions with no numbers
    # e.g. two hundred thousand dollars
    pass_3 = re.findall(r'(?:a|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety) +(?:\b.{0,10}) *dollars?',
        corpus)
    output_file.write('\n'.join(pass_1)+'\n')
    output_file.write('\n'.join(pass_2)+'\n')
    output_file.write('\n'.join(pass_3)+'\n')

input_file.close()
output_file.close()
