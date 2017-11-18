from hdfs import *
# 1、创建集群连接
# client = Client('http://node1:50070')

# client = Client("http://node1:50070",root="/",proxy="hadoop",timeout=100,session=False)# error
client = Client("http://node1:50070",root="/",timeout=100,session=False)

# 2、获取路径的具体信息
# print(client.status('/'))

# 3、获取指定路径的子目录信息
# print(client.list('/'))

# 4、创建目录
# client.makedirs('/hello1',permission=777)

# 5、重命名
# client.rename('/hello1','/hello2')

# 6、删除
# client.delete('/hello2',recursive=True)

# 7、上传数据 error
 # client.upload('d://qingshu3.txt','/qingshu3.txt')

# 8、下载
# client.download('/hellohadoop.txt','d://')

# 9、读取文件 error
with client.read('/hellohadoop.text') as reader:
	print(reader.read())