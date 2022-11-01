

## Part 1.2

- proxy config file
 Will have information leading to both of your web servers.
 it will include:
 ```
 - hostname- address of your instance
 - user ubuntu
 - port 22
 - Identity file- this file is the file that has your pem key, such as ceg3120-key.pem 
 - as well as the same thing for the second instance below it
 ```
 - server 1 config file contains:
 ```
 - hostname for server 2
 - user ubuntu
 - identity file
 - with the same contents you will also duplicate but with the proxy hostname instead
 ```
 - server 2 config file contains:
 ```
 - same contents as server one but with server ones hostname instead.
 ```
 
 ## PART 2.2
 
 ```
 Once the config file has been created you are able to use the ssh command followed by eather the adress of the proxy, webserver 1,
 and webserver 2.
 ```
 ## PART 2.3
 
 - setting up HAProxy load balancer:
 ```
 The HAProxy configuration file located in /etc/haproxy/ needs to be modified with the command sudo vim /etc/haproxy/haproxy.cfg 
 ```
 - what configurations were set?
 ```
 frontend haproxy-main
    bind *:80
    option forwardfor
    default_backend apache_webservers

backend apache_webservers
    balance roundrobin
    server webserver-1      10.0.1.05:80 check
    server webserver-2      10.0.1.13:80 check
 ```
 `Use $ sudo systemctl restart haproxy to restart service afetr configuration change`
 
 - resources:
 ```
 https://www.haproxy.com/blog/haproxy-configuration-basics-load-balance-your-servers/
 https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/
 ```
 ## Part 2.4
 - What file(s) were modified & their location
 `for each server, the /etc/hosts and /var/www/html/index.html will need to be changed.`
 - what configurations were set?
 ```
 for the /var/www/html/index.html file these contents were added:
 <html>

<head>
    <title> CEG3120 - IT Design </title>
</head>

<body>
    <H1> Welcome to Server 1! </H1>
    <p> This simple little index file is being hosted on Server 1</p>
</body>

</html>

same thing for webserver 2 besides it will be server 2.
```
- Where site content files were located (and why)?
```
/var/www/html/index.html is the default location
```
- How to restart the service after a configuration change
`sudo systemctl restart apache2`
## PART 2.5
### SCREENSHOTS
![Screenshot 2022-11-01 001608](https://user-images.githubusercontent.com/77698851/199176112-14e2bf6a-7095-4917-979f-0236a3fe60ea.png)
![Screenshot 2022-11-01 001646](https://user-images.githubusercontent.com/77698851/199176150-63456fa7-0400-4b1f-8f1b-feffb3ec9c11.png)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


