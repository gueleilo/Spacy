import spacy
from spacy.matcher import Matcher

nlp = spacy.load("pt_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "eu baixei Fortnite no meu laptop e não pude abrir o jogo de jeito nenhum. Ajuda?"
    "então, quando eu estava baixando Minecraft, eu consegui a versão Windows onde"
    "está a pasta .zip e usei o programa padrão pra abrir..."
    "É necessário baixar Winzip?"
)

# Write a pattern that matches a form of "download" plus proper noun
pattern = [{"LEMMA": "baixar"}, {"POS": "PROPN"}]

# Add the pattern to the matcher and apply the matcher to the doc
matcher.add("BAIXAR_COISAS_PADRAO", None, pattern)
matches = matcher(doc)
print("Total de matches encontrados:", len(matches))

# Iterate over the matches and print the span text
for match_id, start, end in matches:
    print("Match encontrado:", doc[start:end].text)
