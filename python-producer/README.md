to create this docker image go to terminal:
$ cd kafka-spark-streaming-docker

First make sure that all previous docker images and containers are deleted just to be sure.
Then:

$ docker build python-producer -t python-producer

 Then after the image is created:

$ docker-compose up

For some reason the python producer stops after a minute, so wait until the console is idle, then start the producer container again

Then use this command:

$ sudo chmod 777 jars_dir && \
docker exec -it spark \
spark-submit \
--packages "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0" \
--master "spark://172.18.0.10:7077" \
--class Streaming \
--conf spark.jars.ivy=/opt/bitnami/spark/ivy \
ivy/spark-streaming-with-kafka_2.12-1.0.jar


Also the message still includes the unnecessary "H" in the beginning and is converted to bytes, have to work on making it cleaner.