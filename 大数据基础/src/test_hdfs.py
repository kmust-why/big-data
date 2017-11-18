import hdfs
# 创建一个客户端
client = hdfs.Client('http://node1:50070',root="/",timeout=100,session=False)
#print(client.list('/',status=False))

#print(client.status(hdfs_path="/opt/hadoop1.2/mapred/system",strict=False))

#print(client.content("/hello.txt"))

# print(dir(client))
# print(client.list('/'))
print(client.status("/"))
print(client.list('/'))
