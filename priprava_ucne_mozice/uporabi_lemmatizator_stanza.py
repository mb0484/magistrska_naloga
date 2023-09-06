from classla import Pipeline

# Initialize the pipeline
nlp = Pipeline('sl')

# Process the text
text = "Martin Božič bo letos magistriral na fakulteti za računalništvo in informatiko univerze v Ljubljani."
doc = nlp(text)
conll_output = doc.to_conll()

print(conll_output)

# Parse the CoNLL-U formatted output
lines = conll_output.strip().split('\n')
word_data = [line.split('\t') for line in lines]

# Loop through each word and check NER tag
for word_info in word_data:
    if len(word_info) >= 9:
        word = word_info[1]
        ner_tag = word_info[9]

        if ner_tag.startswith('NER=B-PER') or ner_tag.startswith('NER=I-PER'):
            print(f"'{word}' is a named entity.")
        else:
            print(f"'{word}' is not a named entity.")