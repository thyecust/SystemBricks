## Nginx

[WordPress.com Serves 70,000 req/sec and over 15 Gbit/sec of Traffic using NGINX](https://highscalability.com/wordpresscom-serves-70000-reqsec-and-over-15-gbitsec-of-traf/)
> WordPress.com is serving about 70,000 req/sec and over 15 Gbit/sec of traffic from its NGINX powered load balancers at peak, with plenty of room to grow. Hardware configuration is Dual Xeon 5620 4 core CPUs with hyper-threading, 8-12GB of RAM, running Debian Linux 6.0.

[Testing the Performance of NGINX](https://blog.nginx.org/blog/testing-the-performance-of-nginx-and-nginx-plus-web-servers)
![[Pasted image 20240911192713.png]]

## Load Balancer

[Load Balancing (samwho.dev)](https://samwho.dev/load-balancing/)
![[Pasted image 20240911234402.png]]

[Let's Create a Simple Load Balancer With Go - kasvith.me](https://kasvith.me/posts/lets-create-a-simple-lb-go/)
```go
func lb(w http.ResponseWriter, r *http.Request) {
	attempts := GetAttemptsFromContext(r)
	if attempts > 3 {
		log.Printf("%s(%s) Max attempts reached, terminating\n", r.RemoteAddr, r.URL.Path)
		http.Error(w, "Service not available", http.StatusServiceUnavailable)
		return
	}

	peer := serverPool.GetNextPeer()
	if peer != nil {
		peer.ReverseProxy.ServeHTTP(w, r)
		return
	}
	http.Error(w, "Service not available", http.StatusServiceUnavailable)
}
```

## Self-hosting

[我希望我的 Web 服务器位于我房间的角落 (interconnected.org)](https://interconnected.org/home/2022/10/10/servers)
- [on Hacker News](https://news.ycombinator.com/item?id=33165836)

[我在单个服务器上自托管数十个 Web 应用程序 + 服务的设置 - Casey Primozic 的主页](https://cprimozic.net/blog/my-selfhosted-websites-architecture/)
- [on Hacker News](https://news.ycombinator.com/item?id=29746223)
