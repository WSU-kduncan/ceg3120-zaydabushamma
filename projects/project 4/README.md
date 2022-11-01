

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
 - server 2 config filw contains:
 ```
 - same contents as server one but with server ones hostname instead.
 ```
 


