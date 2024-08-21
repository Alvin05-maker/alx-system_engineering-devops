# Web stack debugging #4

<div align=center>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWk-dJOMGyOSA3mVPR0AIP-6u_afmu6crxdEwPjGCeYHmfeWY8RwHGDGzIIPqi7jr_7tU&usqp=CAU"/>
</div>

## Problem 01
In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends!

```bash
root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   0.353 seconds
Complete requests:      2000
Failed requests:        943
   (Connect: 0, Receive: 0, Length: 943, Exceptions: 0)
Non-2xx responses:      1057
Total transferred:      1196526 bytes
HTML transferred:       789573 bytes
Requests per second:    5664.01 [#/sec] (mean)
Time per request:       17.655 [ms] (mean)
Time per request:       0.177 [ms] (mean, across all concurrent requests)
Transfer rate:          3309.15 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.1      0       8
Processing:     2   17   3.8     17      24
Waiting:        2   17   3.8     17      24
Total:          9   17   3.3     17      24

Percentage of the requests served within a certain time (ms)
  50%     17
  66%     19
  75%     20
  80%     20
  90%     21
  95%     23
  98%     23
  99%     23
 100%     24 (longest request)
```

## Solution
After intensive debugging, I found out my nginx server couldn't handle thousands of request at a time, when I look at error log file, it was obvious most of the request were failing on error `(24) Too many open files ...`. Fixing this required modifying the `/etc/default/nginx` configuration file, and increasing the `ULIMIT` variable from `15` to `9999`


## Problem 02
Trying to login as `holberton` user in my linux machine wasn't possible as I was having a `Too many open file ...` error

```bash
root@079b7269ec1b:~# su - holberton
-su: /etc/profile: Too many open files
-su: /home/holberton/.bash_profile: Too many open files
-su-4.3$ head /etc/passwd
-su: start_pipeline: pgrp pipe: Too many open files
.
.
.
```

## Solution
To fix this, I had to modify the `/etc/security/limits.conf` file and adjust the `hard nofile` variable of the holberton user from `5` to `2000`

`PS` - For the two solution, a puppet manifest was created to make future fix as fast as possible and automated