import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

if __name__ == '__main__':
    if len(sys.argv) !=3:
        print('insufficient params')
        #exit(-1)
    if(len(sys.argv) > 1 and sys.argv[1] is not None):
        host = sys.argv[1]
    else:
        host = 'localhost'

    if(len(sys.argv) > 1 and sys.argv[2] is not None):
        port = int(sys.argv[2])
    else:
        port = 8099

    spark = SparkSession.builder.appName("Spark Stream 1").getOrCreate()
    spark.sparkContext.setLogLevel('ERROR')

    lines = spark.readStream.format('socket').option('host',host).option('port', port).load()

    words = lines.select(explode(split(lines.value, ' ')).alias('word'))
    wordCounts = words.groupBy('word').count()

    query = wordCounts.writeStream.outputMode('complete').format('console').start()

    query.awaitTermination()
