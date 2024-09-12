## OLTP vs. OLAP

DDIA chapter 3

> - OLTP 系统通常面向**最终用户**，这意味着系统可能会收到大量的请求。为了处理负载，应用程序在每个查询中通常只访问少量的记录。应用程序使用某种键来请求记录，存储引擎使用索引来查找所请求的键的数据。**硬盘查找时间往往是这里的瓶颈**。
>- 数据仓库和类似的分析系统会少见一些，因为它们主要由**业务分析人员**使用，而不是最终用户。它们的查询量要比 OLTP 系统少得多，但通常每个查询开销高昂，需要在短时间内扫描数百万条记录。**硬盘带宽往往是瓶颈**，列式存储是针对这种工作负载的日益流行的解决方案。

## Redis

https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/
```
fine-tuned, 256 bytes data SET/GET  200,000 ops/sec
normal, with 60,000 connections      50,000 q/s
normal, with 30,000 connections      60,000 q/s
normal, with    100 connections     120,000 q/s
```

[Redis Explained - by Mahdi Yusuf (architecturenotes.co)](https://architecturenotes.co/p/redis)
![[Pasted image 20240912124312.png]]

[Building a Website to Scale to 100 Million Page Views Per Day and Beyond](https://www.slideshare.net/slideshow/building-a-website-to-scale-to-100-million-page-views-per-day-and-beyond/14760385)
- [On HighScalability](https://highscalability.com/youporn-targeting-200-million-views-a-day-and-beyond/)
- [On Youtube](https://www.youtube.com/watch?v=RlkCdM_f3p4)
![[Pasted image 20240912125330.png]]

## ElasticSearch

[Jepsen: Call me maybe ElasticSearch](https://aphyr.com/posts/317-call-me-maybe-elasticsearch)
> Lucene handles the on-disk storage, indexing, and searching of documents, while ElasticSearch handles document updates, the API, and distribution. Documents are written to collections as free-form JSON; schemas can be overlaid onto collections to specify particular indexing strategies.
![[Pasted image 20240912122805.png]]
注：这里的 CAS 指 Compare-And-Swap。

## ClickHouse
[Fast Open-Source OLAP DBMS. Real-time warehouse.](https://clickhouse.com/)
![[Pasted image 20240911175718.png]]

[Cloudflare 使用 ClickHouse 进行 6 M/s 请求的 HTTP 分析](https://blog.cloudflare.com/http-analytics-for-6m-requests-per-second-using-clickhouse)
![[Pasted image 20240911173926.jpg]]
![[Pasted image 20240911173838.jpg]]

[Cloudflare 如何每秒分析 1M 的 DNS 查询](https://blog.cloudflare.com/how-cloudflare-analyzes-1m-dns-queries-per-second/)
![[Pasted image 20240911174446.png]]

[First ClickHouse research paper: How do you make a modern data analytics database lightning-fast?](https://clickhouse.com/blog/first-clickhouse-research-paper-vldb-lightning-fast-analytics-for-everyone)
![[Pasted image 20240911180046.png]]![[Pasted image 20240911180139.png]]

[https://benchmark.clickhouse.com/](https://benchmark.clickhouse.com/)
![[Pasted image 20240911180620.png]]