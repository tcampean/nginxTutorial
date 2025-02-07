# nginxTutorial

## What is a load balancer?
A load balancer is a hardware/software that acts as a reverse proxy and distributes network or application traffic across a number of servers. Load balancers are used to increase the capacity (concurrent users) and reliability of applications. They improve the overall performance of applications by decreasing the burden on servers associated with managing and maintaining application and network sessions.

## Choosing a Load Balancing Method
NGINX Open Source supports four load balancing methods, and NGINX Plus adds two more methods:

## 1- Round Robin:
Requests are distributed evenly across the servers, with server weights taken into consideration. This method is used by default (there is no directive for enabling it):

```
upstream backend {
   # no load balancing method is specified for Round Robin
   server app1;
   server app2;
}
```

## 2- Least Connections:
A request is sent to the server with the least number of active connections:

```
upstream backend {
    least_conn;
    server app1;
    server app2.com;
}
```

## 3- IP Hash: 
The server to which a request is sent is determined from the client IP address. In this case, either the first three octets of the IPv4 address or the whole IPv6 address are used to calculate the hash value. The method guarantees that requests from the same address get to the same server unless it is not available.

```
upstream backend {
    ip_hash;
    server app1;
    server app2;
}
```

## 4- Generic Hash:
The server to which a request is sent is determined from a user-defined key which can be a text string, variable, or combination. For example, the key may be a paired source IP address and port, or a URI as in this example:

```
upstream backend {
    hash $request_uri consistent;
    server app1;
    server app2;
}
```

## Make Server Down

If one of the servers needs to be temporarily removed from the load balancing rotation, it can be marked with the down parameter in order to preserve the current hashing of client IP addresses.

```
upstream backend {
    server app1;
    server app2;
    server app3 down;
}
```

## Configure as server backup

The app3 is marked as a backup server and does not receive requests unless both of the other servers are unavailable.

```
upstream backend {
    server app1;
    server app2;
    server app3 backup;
}
```

## Nginx configuration

This configuration can be found in `docker-compose.yml` and it reflects how the services look and on what port nginx listens.

```
services:
  app1:
    build: ./app1
  app2:
    build: ./app2
  app3:
    build: ./app3
  
  nginx:
    build: ./nginx 
    ports:
    - "80:80"
    depends_on:
      - app1
      - app2
      - app3
```

## Run the example

Intialize the containers by executing `docker-compose up -d` inside the `nginx-docker-load-balancer` folder.

Test it by going to localhost:80 in your browser