<!-- Hadoop来源：谷歌的三篇论文

大数据的解决方案：Hadoop

### Hadoop的两大核心

1. HDFS
2. MapReduce

### 大数据VS传统数据

![](images/大数据VS传统数据.png)

结构化数据：可存入关系型的数据库中。

### 关系型数据VSHadoop

1. 并行关系数据库
2. MPP or Hadoop

### 谁在使用Hadoop?

阿里、百度、谷歌

### Hadoop版本问题

Hadoop1.2.1

### HDFS结构

![](images/HDFS结构.png)

### HDFS优点

1. 高容错性
2. 适合批量处理
3. 适合大数据处理
4. 可构建在廉价机器上

### HDFS缺点

1. 低延迟数据访问
2. 小文件存取
3. 并发写入、文件随机修改

### HDFS架构

![](images/HDFS架构.png)

1. NameNode负责任务的请求，NameNode把请求转发给各个DataNode
2. HDFS数据存储单元

- 文件被分为固定大小的数据块
- 一个文件的存储方式
- Block大小和副本数通过Client端上传文件时候设置

3. NameNode:接收客户端的读写服务
4. SecondaryNameNode（NN）:帮助NameNode合并edits文件，起到一定的热备份作用

- SNN合并流程
  ![](images/SNN合并流程.png)

5. DataNode（DN）,存储数据

- Black的副本放置策略
  - 第一个副本
  - 第二个副本
  - 第三个副本
  - 更多副本：随机节点

### HDFS读流程

![](images/HDFS读流程.png)

### HDFS写流程
![](images/HDFS写流程.png)

1. HDFS文件权限
2. 安全模式：完成一个初始化的工作 -->[]()

## Hadoop的hdf分布式文件系统

1. 在官网下载Hadoop安装包（hadoop-1.2.1.tar.gz）
2. 解压并配置core_site.xml文件
3. 参考：
- [Hadoop1.2.1详细配置与相关问题讲解](http://m.blog.csdn.net/lht_okk/article/details/77493945)

- [JAVE_HOME is not set](http://blog.csdn.net/sprintfwater/article/details/8791741)

4. 文件拷贝命令：scp -r ./conf/* root@node3:~/hadoop-1.2.1/conf/

5. 格式化namenode:进入bin目录下，执行命令：./hadoop namenode -format，其在相应的目录下生成相应的文件

6. ./start-dfs.sh，启动dfs

7. jps命令查看是否启动了dfs

8. 关闭防火墙：service iptable stop或者systemctl stop firewalld

9. 配置域名解析

10. 在本地通过浏览器访问：http://node1:50070

## Hadoop的mapreduce分布式计算框架（适合于离线计算，strom适合流式计算，实时计算，spark适合在内存中做计算，快速得到计算结果）

### MapReduce设计理念

- 移动计算，而不是移动数据
- 计算框架MR

![](images/MapReduce计算框架.png)

- 其中，split0、split1、split2为一个一个的文件碎片
- 分为四个步骤：
  - 原始数据经过spli后被切换成多个文件片段t、map