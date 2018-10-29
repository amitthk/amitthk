from pyspark.sql.types import *
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
import time, datetime


if __name__ == "__main__":
    sparkSession = SparkSession.builder.master('local').appName('SparkLogAppendMode').getOrCreate()

    sparkSession.sparkContext.setLogLevel('ERROR')

    schema = StructType([StructField("P", StringType(), True),
                         StructField("S", StringType(), True),
                         StructField("UID", StringType(), True),
                         StructField("PID", StringType(), True),
                         StructField("PPID", StringType(), True),
                         StructField("C", StringType(), True),
                         StructField("PRI", StringType(), True),
                         StructField("NI", StringType(), True),
                         StructField("ADDR", StringType(), True),
                         StructField("SZ", StringType(), True),
                         StructField("WCHAN", StringType(), True),
                         StructField("STIME", StringType(), True),
                         StructField("TTY", StringType(), True),
                         StructField("TIME", StringType(), True),
                         StructField("CMD", StringType(), True)])

    fileStreamDf = sparkSession.readStream.option("header","true")\
        .option("delimiter"," ").schema(schema).csv("D:\\Amit\\projects\\amitthk\\bitbucket\\pysparktest\\docker\\all_logs")

    def add_timestamp():
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        return timestamp

    print(" ")
    print("Stream ready?")
    print(fileStreamDf.isStreaming)

    print(" ")
    print("Schema: ")
    print(fileStreamDf.printSchema)

    add_timestamp_udf = udf(add_timestamp, StringType())

    tsFileStream = fileStreamDf.withColumn("timestamp", add_timestamp_udf())

    trimmedDF = fileStreamDf.select(fileStreamDf.TIME, fileStreamDf.CMD, "timestamp")

    query = trimmedDF.writeStream.outputMode("append").format("console").option("truncate", "false").option("numRows", 30).start().awaitTermination()