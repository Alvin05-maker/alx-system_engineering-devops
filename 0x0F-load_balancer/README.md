# Load balancer
> Load balancer will distribute the work-load of your system to multiple individual systems, or group of systems to to reduce the amount of load on an individual system, which in turn increases the reliability, efficiency and availability of your enterprise application or websites.

In this project, I've implemented a load balancing solution using `HAProxy` to efficiently distribute incoming traffic across two servers. The chosen load-balancing method is `round-robin`. Additionally, I've enhanced the setup by introducing a custom HTTP header: `X-Served-By` to both servers, facilitating the identification of the traffic source.

Adhering to best practices, I've developed bash scripts and puppet manifests to streamline automation and configuration processes.


![ad](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png)


## Example

```bash
alvin05$ curl -sIL alvin05.tech
HTTP/2 200 
server: nginx/1.18.0 (Ubuntu)
date: Fri, 15 Dec 2023 20:50:42 GMT
content-type: text/html
content-length: 13
last-modified: Tue, 05 Dec 2023 05:22:52 GMT
etag: "656eb3ac-d"
x-served-by: 138525-web-01
accept-ranges: bytes


alvin05$ curl -sIL alvin05.tech
HTTP/2 200 
server: nginx/1.18.0 (Ubuntu)
date: Fri, 23 Aug 2024 20:50:54 GMT
content-type: text/html
content-length: 13
last-modified: Sat, 09 Dec 2023 14:33:15 GMT
etag: "65747aab-d"
x-served-by: 138525-web-02
accept-ranges: bytes
```


## Automation scriptis
- `0-custom_http_response_header`: Configures Nginx so that its HTTP response contains a custom header: `X-Served-By: $hostname`

- `1-install_load_balancer` - Configures `HAproxy` so that it send traffic to web-01 and web-02 using round-robin algorithm

- `2-puppet_custom_http_response_header.pp` - Puppet manifest that adds a custom http header
