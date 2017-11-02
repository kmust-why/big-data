import hdfs
client = hdfs.Client("http://192.168.194.128:9000")
print(client.list("/",status=False))
