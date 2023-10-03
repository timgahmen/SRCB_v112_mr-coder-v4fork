from .. import Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal, sys, platform, sysconfig
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess

@Drone.on(events.NewMessage(incoming=True, pattern="/cpu"))
async def storage(event):
    cpu = str(psutil.cpu_percent(5))
    load1, load5, load10 = psutil.getloadavg()
    cpu_usage = (load10/os.cpu_count()) * 100
    cpu_count = psutil.cpu_count()
    cpu_physical = psutil.cpu_count(logical=False)
    cpu_usable = len(psutil.Process().cpu_affinity())
    await event.reply(f"**OS:** {platform.system()}\nCPU Utilization: {cpu}%\nCPU Load Past 10 Min: {cpu_usage}\nTotal CPU Cores: {cpu_count}\nCPU Physical Cores: {cpu_physical}\nUsable CPU Cores: {cpu_usable}\n\n\n")
    return
  
