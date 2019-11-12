
# Guided Lab Exercise in using Netcat

For this exercise, I will be connecting to the TCP port 31337. This port number could be anything really; I chose 31337 for no particular reason. To illustrate the relationship between an IP address and a port number, think of how the post office delivers mail to you. If you consider that your street address is analogous to an IP address, a port can be thought of as the name on the envelope. It is up to the sender to identify the specific person that the mail is intended for. If all goes well, the recipient will recognize that the mail is destined for a specific person. Of course, perhaps the sender knows that John, Mary, Jane, and Gregory live at the address, 123 Main Street. At this point, the sender only needs to specify that the letter is intended for Gregory. Regardless of the port you select, once you have your client and listener configured, let's go ahead and get started with the exercise. On the listener machine, we will want to perform the following tasks:

1. Launch a command prompt if your listener operating system is Windows-based as in the preceding example 
(You would open a shell using a terminal on Unix and Linux).

2. Type in the following command:
```
nc –l –p 31337

```
![image](https://user-images.githubusercontent.com/47218880/68681776-9af88e00-0529-11ea-88a2-b6e1da9fa360.png)

In the preceding example, we launched Netcat in listener mode by invoking the –l switch. We specified the utility to listen on the TCP port 31337 by invoking the –p switch. Alternatively, Netcat allows you to concatenate switches as well, so I could have accomplished the same thing by typing nc –lp 31337.

You will notice that the cursor is immediately under the command prompt. Once we begin sending raw packets across, this is where they will appear. At this point, we only have one end of the connection open, so let's establish the other end of the connection now with our client machine.

3. Launch a shell using terminal.
4. In the shell prompt, type the following command:
```
nc 192.168.0.10 31337
```
![image](https://user-images.githubusercontent.com/47218880/68681822-b794c600-0529-11ea-8bab-7b04c90b207d.png)

With our Netcat listener activated on the host 192.168.0.10, we completed the other end of the connection by specifying the host we wanted to connect to, followed by the port number. At this point, we have a fully established and unencrypted socket between the client and listener. We will demonstrate this by typing a message from the client.

5. On the client machine, type message from client to listener and hit Enter. The following screenshot shows what the client sees on the terminal:

![image](https://user-images.githubusercontent.com/47218880/68681858-c8ddd280-0529-11ea-9ce9-ae0544a30d51.png)

6. If you switch to the listener console, you will see that the following screenshot demonstrates what the listener sees:

![image](https://user-images.githubusercontent.com/47218880/68681903-dd21cf80-0529-11ea-91e9-0a583c40cf49.png)

Now, we are simply going to reverse the direction and send communication from the listener to the client.

7. From the listener, type message from listener to client and hit Enter. The following screenshot shows what the listener sees:

![image](https://user-images.githubusercontent.com/47218880/68681940-ef9c0900-0529-11ea-869e-97448263cf3b.png)

8. Switching to the client session, the next screenshot shows what the client sees:

![image](https://user-images.githubusercontent.com/47218880/68681983-004c7f00-052a-11ea-97a1-f059617851c9.png)

After completing the exercise, sending the key combination Ctrl + C on either side will terminate the connection. It is important to note that if you want to re-establish the connection, you will need to launch the listener again when using the –l switch. Netcat can be run with the –L (capital L) switch only on the Windows utility, and when a connection is terminated the listener will remain open.
