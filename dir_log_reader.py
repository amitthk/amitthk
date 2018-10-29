from pyspark.sql.types import *
from pyspark.sql import SparkSession


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

    print(" ")
    print("Stream ready?")
    print(fileStreamDf.isStreaming)

    print(" ")
    print("Schema: ")
    print(fileStreamDf.printSchema)

    trimmedDF = fileStreamDf.select(fileStreamDf.TIME, fileStreamDf.CMD)

    query = trimmedDF.writeStream.outputMode("append").format("console").option("truncate", "false").option("numRows", 30).start().awaitTermination()