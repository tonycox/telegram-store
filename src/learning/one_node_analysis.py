import os
from gensim.models.doc2vec import Doc2Vec, TaggedBrownCorpus

text_dir = '{}'.format(os.sep).join(['D:', 'projects', 'dataset2014', 'repository_text_2014-06-13'])
meta_dir = '{}'.format(os.sep).join(['D:', 'projects', 'dataset2014', 'repository_metadata_2014-06-13'])


tagged_docs = TaggedBrownCorpus('')


model = Doc2Vec(tagged_docs, dm=0, alpha=0.25, size=100, window=8, min_count=0, workers=4)
for epoch in range(5):
    if epoch % 2 == 0:
        model.train(tagged_docs, total_examples=model.corpus_count)
        model.alpha -= 0.002
        model.min_alpha = model.alpha

# model.docvecs.most_similar_to_given('', [])
print(tagged_docs[0])
model.infer_vector(tagged_docs[0].words)
model.most_similar(u'what', topn=len(model.docvecs))
