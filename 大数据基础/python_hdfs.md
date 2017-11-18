### Python操作HDFS分布式文件系统

#### 1：安装

​      由于我的是windows环境（linux其实也一样），只要有pip或者setup_install安装起来都是很方便的

```
     pip install hdfs
```

#### 2：Client——创建集群连接

```
from hdfs import *
client = Client("http://127.0.0.1:50070")
```

​       其他参数说明：

​       class`hdfs.client.``Client`(**url****, ****root=None****, ****proxy=None****, ****timeout=None****, ****session=None**)

​                    url：ip：端口

​                    root：制定的hdfs根目录

​                    proxy：制定登陆的用户身份

​                    timeout：设置的超时时间

​                    seesion：requests.Session instance, used to emit all requests.（不是太懂，应该四用户发出请求）

​       这里我们着重看一下proxy这个，首先我们指定root用户连接

```
>>> client = Client("http://127.0.0.1:50070",root="/",timeout=100,session=False)
>>> client.list("/")
[u'hbase']
```

​       看起来一切正常的样子，接下来我们指定一个别的用户，比如说gamer再看

```
>>> client = Client("http://127.0.0.1:50070",root="/",proxy="gamer",timeout=100,session=False)
>>> client.list("/")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/hdfs/client.py", line 893, in list
    statuses = self._list_status(hdfs_path).json()['FileStatuses']['FileStatus']
  File "/usr/local/lib/python2.7/dist-packages/hdfs/client.py", line 92, in api_handler
    **self.kwargs
  File "/usr/local/lib/python2.7/dist-packages/hdfs/client.py", line 181, in _request
    return _on_error(response)
  File "/usr/local/lib/python2.7/dist-packages/hdfs/client.py", line 44, in _on_error
    raise HdfsError(message)
hdfs.util.HdfsError: Failed to obtain user group information: org.apache.hadoop.security.authorize.AuthorizationException: User: dr.who is not allowed to impersonate gamer
```

​       这时候就抛出异常了

# 3：dir——查看支持的方法

```
>>> dir(client)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
'__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__registry__',
 '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_append', '_create', '_delete',
 '_get_content_summary', '_get_file_checksum', '_get_file_status', '_get_home_directory', '_list_status', '_mkdirs', '_open',
 '_proxy', '_rename', '_request', '_session', '_set_owner', '_set_permission', '_set_replication', '_set_times', '_timeout', 
'checksum', 'content', 'delete', 'download', 'from_options', 'list', 'makedirs', 'parts', 'read', 'rename', 'resolve', 'root',
 'set_owner', 'set_permission', 'set_replication', 'set_times', 'status', 'upload',
 'url', 'walk', 'write']
```

# 4：status——获取路径的具体信息

```
>>> client.status("/")
{'accessTime': 0, 'pathSuffix': '', 'group': 'supergroup', 'type': 'DIRECTORY', 'owner': 'root', 'childrenNum': 4, 'blockSize': 0,
 'fileId': 16385, 'length': 0, 'replication': 0, 'storagePolicy': 0, 'modificationTime': 1473023149031, 'permission': '777'}
```

​      其他参数：`status`(**hdfs_path****, ****strict=True**)

​               hdfs_path：就是hdfs路径

​               strict：设置为True时，如果hdfs_path路径不存在就会抛出异常，如果设置为False，如果路径为不存在，则返回None

```
>>> client = Client("http://127.0.0.1:50070",root="/",timeout=100,session=False)
>>> client.status("/gamer",strict=True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python2.7/dist-packages/hdfs/client.py", line 277, in status
    res = self._get_file_status(hdfs_path, strict=strict)
  File "/usr/local/lib/python2.7/dist-packages/hdfs/client.py", line 92, in api_handler
    **self.kwargs
  File "/usr/local/lib/python2.7/dist-packages/hdfs/client.py", line 181, in _request
    return _on_error(response)
  File "/usr/local/lib/python2.7/dist-packages/hdfs/client.py", line 44, in _on_error
    raise HdfsError(message)
hdfs.util.HdfsError: File does not exist: /gamer
>>> client.status("/gamer",strict=False)
>>>
```

​      从例子中可以看出，当设置为false时，路径不存在，什么也不输出

# 5：list——获取指定路径的子目录信息

```
>>> client.list("/")
['file', 'gyt', 'hbase', 'tmp']
```

​     其他参数：`list`(**hdfs_path****, ****status=False****)**

​              status：为True时，也返回子目录的状态信息，默认为Flase

```
>>> client.list("/")
[u'hbase']
>>> client.list("/",status=False)
[u'hbase']
>>> client.list("/",status=True)
[(u'hbase', {u'group': u'supergroup', u'permission': u'755', u'blockSize': 0, u'accessTime': 0, u'pathSuffix': u'hbase', u'modificationTime': 1472986624167, u'replication': 0, u'length': 0, u'childrenNum': 7, u'owner': u'root', u'storagePolicy': 0, u'type': u'DIRECTORY', u'fileId': 16386})]
>>> 
```

# 6：makedirs——创建目录

```
>>> client.makedirs("/test")
>>> client.list("/")
['file', 'gyt', 'hbase', 'test', 'tmp']
>>> client.status("/test")
{'accessTime': 0, 'pathSuffix': '', 'group': 'supergroup', 'type': 'DIRECTORY', 'owner': 'dr.who', 'childrenNum': 0, 'blockSize': 0,
 'fileId': 16493, 'length': 0, 'replication': 0, 'storagePolicy': 0, 'modificationTime': 1473096896947, 'permission': '755'}
```

​       其他参数：`makedirs`(**hdfs_path****, ****permission=None**)

​                permission：设置权限

```
>>> client.makedirs("/test",permission=777)
>>> client.status("/test")
{u'group': u'supergroup', u'permission': u'777', u'blockSize': 0, u'accessTime': 0, u'pathSuffix': u'', u'modificationTime': 1473175557340, u'replication': 0, u'length': 0, u'childrenNum': 0, u'owner': u'dr.who', u'storagePolicy': 0, u'type': u'DIRECTORY', u'fileId': 16437}
```

​       可以看出该文件夹的权限是777

# 7：rename—重命名

```
>>> client.rename("/test","/new_name")
>>> client.list("/")
['file', 'gyt', 'hbase', 'new_name', 'tmp']
```

​       格式说明：`rename`(**hdfs_path****, local****_path）**

# 8：delete—删除

```
>>> client.list("/")
['file', 'gyt', 'hbase', 'new_name', 'tmp']
>>> client.delete("/new_name")
True
>>> client.list("/")
['file', 'gyt', 'hbase', 'tmp']
```

​      其他参数：`delete`(**hdfs_path****, ****recursive=False**)

​               recursive：删除文件和其子目录，设置为False如果不存在，则会抛出异常，默认为False

```
>>> client.delete("/test",recursive=True)
True
>>> client.delete("/test",recursive=True)
False
>>> client.delete("/test")
False
```

# 9：upload——上传数据

===================================分割线===================================================================

为什么这里需要分割线？因为在做web平台可视化操作hdfs的时候遇到了问题！错误如下：

```
requests.exceptions.ConnectionError: HTTPConnectionPool(host='slaver1', port=50075): Max retries exceeded with url:
 /webhdfs/v1/thinkgamer/name.txt?op=OPEN&namenoderpcaddress=master&offset=0 (Caused by NewConnectionError
('<requests.packages.urllib3.connection.HTTPConnection object at 0x00000000043A3FD0>: Failed to establish a new connection:
 [Errno 11004] getaddrinfo failed',))
```

对错误的理解：看其大意是Http连接太多，没有及时关闭，导致错误 （PS：网上对hdfs操作的资料比较少，大部分都只停留在基础语法层面，但对于错误的记录及解决办法少之又少）

解决办法：暂无

由于我是在windows上操作集群的，而我的集群是在服务器上部署的，所以我考虑是否在服务器上尝试下载和上传数据，果断ok

```
>>> client.list("/")
[u'hbase', u'test']
>>> client.upload("/test","/opt/bigdata/hadoop/NOTICE.txt")
'/test/NOTICE.txt'
>>> client.list("/")
[u'hbase', u'test']
>>> client.list("/test")
[u'NOTICE.txt']
```

​       其他参数：

```
upload
```

(

**hdfs_path**

**, **

**local_path**

**, **

**overwrite=False**

**, **

**n_threads=1**

**, **

**temp_dir=None**

**, **

**                                 chunk_size=65536****,****progress=None****, ****cleanup=True****, *****\*kwargs**)

​               overwrite：是否是覆盖性上传文件

​               n_threads：启动的线程数目

​               temp_dir：当overwrite=true时，远程文件一旦存在，则会在上传完之后进行交换

​               chunk_size：文件上传的大小区间

​               progress：回调函数来跟踪进度，为每一chunk_size字节。它将传递两个参数，文件上传的路径和传输的字节数。一旦完成，-1将作为第二个参数

​               cleanup：如果在上传任何文件时发生错误，则删除该文件

# 10：download——下载

```
>>> client.download("/test/NOTICE.txt","/home")
'/home/NOTICE.txt'
>>> import os
>>> os.system("ls /home")
lost+found  NOTICE.txt	thinkgamer
0
>>> 
```

​      其他参数：

```
download
```

(

**hdfs_path**

**, **

**local_path**

**, **

**overwrite=False**

**, **

**n_threads=1**

**, **

**temp_dir=None**

**, **

***\*kwargs**

)

​              参考上传 upload

# 11：read——读取文件

​    同样在windows客户端上执行依旧报错，在hadoop的节点服务器上执行

```

```

```
>>> with client.read("/test/NOTICE.txt") as reader:
...     print reader.read()
... 
This product includes software developed by The Apache Software
Foundation (http://www.apache.org/).

>>>
```

​     其他参数：

```
read
```

(

***args**

**, **

***\*kwds**

)

​              hdfs_path：hdfs路径

​              offset：设置开始的字节位置

​              length：读取的长度（字节为单位）

​              buffer_size：用于传输数据的字节的缓冲区的大小。默认值设置在HDFS配置。

​              encoding：制定编码

​              chunk_size：如果设置为正数，上下文管理器将返回一个发生器产生的每一chunk_size字节而不是一个类似文件的对象

​              delimiter：如果设置，上下文管理器将返回一个发生器产生每次遇到分隔符。此参数要求指定的编码。

​              progress：回调函数来跟踪进度，为每一chunk_size字节（不可用，如果块大小不是指定）。它将传递两个参数，文件上传的路径和传输的字节数。称为一次与- 1作为第二个参数。

附：在对文件操作时，可能会提示错误

```
hdfs.util.HdfsError: Permission denied: user=dr.who, access=WRITE, inode="/test":root:supergroup:drwxr-xr-x
```

​        解决办法是：在配置文件hdfs-site.xml中加入

```
<property>
  <name>dfs.permissions</name>
  <value>false</value>
</property>
```

​        重启集群即可

基本常用的功能也就这些了，如果需要一些特殊的功能，可以自己执行help(client.method)进行查看