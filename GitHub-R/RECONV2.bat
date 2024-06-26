:Recon-v2
cls
@echo off
title Recon v2
color 09
chcp 65001 > nul
type ReCon.txt
type Rec-Cmds.txt

set /p Opt=
if %Opt% == IpSn goto IpSna

if %Opt% == RmIp goto RemoteId
 
if %Opt% == GenNit goto NitroGeN
 
if %Opt% == SlfIp goto SelfIp

if %Opt% == RecMen goto Recon-v2
pause 

:SelfIp
arp -a >> Rec-logged.txt 
pause 
echo Current ids will be logged in Rec-logged.txt 
pause 
goto Recon-v2

:IpSna
echo arp -a>> Open-me.bat
cls

echo File created Name Open-me.bat
goto Recon-v2

