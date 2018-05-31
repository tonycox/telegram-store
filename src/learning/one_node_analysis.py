import os
import nltk
from gensim.models.doc2vec import Doc2Vec, TaggedBrownCorpus
from nltk.corpus import brown

dir_name = nltk.data.path[-1] + os.path.sep + brown.subdir + os.path.sep + brown.__name__
tagged_docs = TaggedBrownCorpus(dir_name)
model = Doc2Vec(tagged_docs, dm=1, alpha=0.25, vector_size=300, min_count=0, workers=4)

for epoch in range(5):
    if epoch % 2 == 0:
        model.train(tagged_docs, total_examples=model.corpus_count, epochs=model.epochs)
        model.alpha -= 0.002
        model.min_alpha = model.alpha

sent = brown.sents()[0]
print(' '.join(sent))
vector = model.infer_vector(sent)
similar = model.docvecs.most_similar([vector], topn=7)
print(similar)
