# IM

## 简述
一个用python开发的IM<br>

### 实验目的
1 主要是尝试操控redis和mysql,python 较 c++配置环境简单很多就是采用了Python <br>
2 采用UDP通信<br>

### 思路
#### 客户端
1 发出后，数据库会回信，判断成功与否，和错误代码。 <br>

### 服务端
1 服务端每个Worker server 采用单线程，受Nginx 启发，采用一个分发任务进程做负载均衡。<br>
2 将在线的人的地址放入redis中,并设置过期时间，采用SETNX 做分布式锁。 <br>
