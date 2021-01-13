from spacy.lang.pt import Portuguese

nlp = Portuguese()

# Process the text
doc = nlp("Eu gosto de gatos e cachorros.")


for token in doc:
    print(token.text)
