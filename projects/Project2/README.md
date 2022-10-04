Part 1.1

Create A VPC.

how to-
To create VPC, search VPC in search box and click create VPC, made sure to apply a 24-bit subnet, add name in key if not already set.

what is a VPC? 
a Virtual Private Cloud just like a router, is a digital netowrk that can be configured in such a way to communicate to others. 
resembles a traditional network.

![Screenshot 2022-10-03 2126331 1](https://user-images.githubusercontent.com/77698851/193714993-7ac33137-92ab-4139-a44b-4e57bbe2359a.png)


part 1.2.

creating a subnet

how to-
navigate to subnets only from the VPC page on the left scroll down bar. click create subnet and choose VPC that you desire Subnet to be apart of.

What is a Subnet?
A subnet is a range of available IP addresses in your VPC. Can also organize IP's to make the netowrk more efficient. 

![Screenshot 2022-10-03 2143131 2](https://user-images.githubusercontent.com/77698851/193716538-9f48f578-6884-4175-bb34-08b948afb7ec.png)

part 1.3

create an internet gateway

how to- currently on VPC, navigate to left scroll bar and into internet gateways, create one, and on the top right click attack to a VPC.

what is an internet gateway?

A node connects many connections for communicating, also deals with outbound traffic, primarily takes affect when a connection sits between two 
different netowrks.

![Screenshot 2022-10-03 2156081 3](https://user-images.githubusercontent.com/77698851/193717966-863dd728-e888-4883-9067-2e060430ddb9.png)

part 1.4

Create a route table
 how to - 
 
1.click on route tables on the left scroll bar,choose create route table. choose associated VPC. 
2. next, click on tabkle, and on the subnet associatio, explicit subnet asocciations, then choose the subnet that was previously attached to your VPC.
3. Last, click on the route tab on your route table and click edit routes, set destination as 0.0.0.0/0 to send traffic to all destinations
4. set target as internet gateway.

what is a route table?

set of rules that will determine the flow of traffic from the subnet.

![Screenshot 2022-10-03 2210131 4](https://user-images.githubusercontent.com/77698851/193720961-5593642b-23e7-4146-bbff-eb963df1a675.png)
![Screenshot 2022-10-03 2222111 4](https://user-images.githubusercontent.com/77698851/193720978-d4e3d897-b5e1-4fcf-92bd-4e9e0638f172.png)
![Screenshot 2022-10-03 2223141 4](https://user-images.githubusercontent.com/77698851/193720992-b0ce4e59-1c4d-46f0-9ee5-0ec982b792dd.png)

part 1.5
Create a security group

how to?

1.click on security groups on the left hand corner scroll bar.
2.click create security group button on top right.
3.navigate to inbound rules and click on add rule
4.click on SSH(port 22), choose my ip to refer to your computer, which should autofill your IP in ther next column.
5.add rule, SSH, 130.108.0.0/24, so wright state can connect with ip addresses starting with 130.108
6.add rule, SSh, addresses starting with 130.108, which what was our previous VPC we had built to allow all Instances within the VPC.

what is a security group?

Similar to firewall rules, allows for security and manages traffic and who comes in and out of the network via inbound rules and outbound.

**note screenshot does not include added VPC, to attach VPC, click on VPC and attach VPC you want associated.
![Screenshot 2022-10-03 2240131 5](https://user-images.githubusercontent.com/77698851/193723114-de93da8f-151f-4367-bb24-c70d1ed45f3b.png)



