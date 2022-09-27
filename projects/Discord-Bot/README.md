
Part 1- SETUP
*how to use OAuth2 to add/authenticate your Bot with your server-  OAuth2 is a protocol for dealing with authorization, where a service can grant a client application
limited access based on the application’s credentials and allowed scopes.

Navigate to developer portal , OAuth2, URL generator. Check Bot then administrator, copy Url and paste it in search bar to authorize. Head back to your server and bot should have joined.

*Dependencies: Packages needed to run code were sudo apt install python3-pip, pip3 install -U python-dotenv, 
	pip3 install -U discord.py==1.7.3, sudo apt install python3-pip, and pip3 install -U discord.py==2.0.1. 
  
*How to generate an API token- head to the Discord Developer Portal and create a new application, agree to terms, and add bot.
click reset token on bot tab and make sure to copy right after as you will not be able to after.

*Place token into your.env file and will be placed into a variable DISCORD_TOKEN.
you will also have a variable called DISCORD_GUILD which you will store the name of your server to deploy the bot.
 for now in the folder .env place the contents DISCORD_TOKEN="with your token".
 
 Part2- Usage
*To use: output the word "quotes" to display motivational quotes-
'The road to success and the road to failure are almost exactly the same.',
'Success is peace of mind, which is a direct result of self-satisfaction in knowing you made the effort to become the best of which you are capable.',
'I never dreamed about success. I worked for it.',
'You learn more from failure than from success. Don’t let it stop you. Failure builds character.',

part 3- Research
*One way to allow an active bot on at all times is to keep another system on all the time or maybe even a virtual machine might work. 
After looking up more solutions one that may work is having a sceduled task on a pc or a computer such as a cron job but I do not know if it is still active when a pc is 
turned off :( 
the only possible solution for a system to be off would be a cloud system or virtual machine, if your someone that always has their computers on then that will also work.
hello

