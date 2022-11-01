

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
 The HAProxy configuration file located in /etc/haproxy/ needs to be modified with the command `sudo vim /etc/haproxy/haproxy.cfg` 
 ```
 - what configurations were set?
 ```
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


