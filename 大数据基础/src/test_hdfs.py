import hdfs
# 创建一个客户端
client = hdfs.Client('http://192.168.194.128:50070',root="/",timeout=100,session=False)
#print(client.list('/',status=False))

#print(client.status(hdfs_path="/opt/hadoop1.2/mapred/system",strict=False))

#print(client.content("/hello.txt"))

# print(dir(client))
# print(client.list('/'))
client.status("/")