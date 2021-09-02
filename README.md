# discord-channel-jumper

## What is it
I wanted to switch channels in discord with a simple command.
So what this does: 
```
main.py CHANNEL_NAME
```
Switches to discord window
presses ctrl+k  - _discord quick switcher_

then enters name from arugment and presses enter and your on that channel


## Use case
I have a raspberry pi connect to a monitor with discord open all the time.
Now I'm able to make aliases in powershell eg. "cs" 

which translates into: 
```
ssh raspberry_pi@IP /PATH/TO/FILE cs
```
and boom I'm on the cs channel.


## requirements
Needs:

Python and wmctrl

 **wmctrl** 
:
```
sudo apt install wmctrl
```