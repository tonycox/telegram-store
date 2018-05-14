from sklearn.externals import joblib
from pyspark import SparkContext, SparkConf

appName = 'stream-prediction'
master = 'local[*]'

conf = SparkConf()\
    .setAppName(appName)\
    .setMaster(master)\
    .set('spark.sql.warehouse.dir', 'file:///E:/Work/spark/installtion/spark/spark-warehouse/')
sc = SparkContext(conf=conf)
ssc = _

models = joblib.load('models')
broadcast_models = sc.broadcast(models)

results = {}
for name, clf in models.iteritems():
    results[name] = broadcast_models.predict([cleaned_data])[0]

results.pprint()

ssc.start()
ssc.await..
