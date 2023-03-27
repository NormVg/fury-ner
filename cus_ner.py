import spacy

nlp_ner = spacy.load("model-best")
text = "play big scratch music"
doc = nlp_ner(text)
for ent in doc.ents:
    print(ent.text,ent.label_)