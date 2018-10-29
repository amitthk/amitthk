import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

if __name__ == "__main__":
    if (len(sys.argv) < 5):
        print("insufficient args", sys.stderr)

    if(len(sys.argv)>1 and sys.argv[1] is not None):
        host = sys.argv[1]
    else:
        host = 'localhost'

    if (len(sys.argv)>1 and sys.argv[2] is not None):
        port = sys.argv[2]
    else:
        port = '9092'

    if (len(sys.argv)>2 and sys.argv[3] is not None):
        topic = sys.argv[3]
    else:
        topic = 'twittertopic'

    #if (len(sys.argv)>3 and sys.argv[4] is not None):
     #   tracks = sys.argv[4]

    spark = SparkSession.builder.appName("Tweek consumer").getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")

    tweetsDFRaw = spark.readStream.format("kafka").option("kafka.bootstrap.servers", host+":"+port).option("subscribe", topic).load()

    tweetsDF = tweetsDFRaw.selectExpr("CAST(value AS STRING)")

    query = tweetsDF.writeStream.outputMode("append").format("console").option("truncate", "false").trigger(processingTime="5 seconds").start().awaitTermination()