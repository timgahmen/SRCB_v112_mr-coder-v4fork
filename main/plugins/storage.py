from .. import bot as Drone
from telethon import events, Button
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal, sys, platform, sysconfig
from psutil import disk_usage, cpu_percent, virtual_memory, Process as psprocess

@Drone.on(events.NewMessage(incoming=True, pattern="/storage"))
async def storage(event):
    total, used, free, disk= disk_usage('/')
    total = round(total/1024.0/1024.0/1024.0,1)
    free = round(free/1024.0/1024.0/1024.0,1)
    memory = virtual_memory()
    mem_p = round(memory.percent)
    mem_t = round(memory.total/1024.0/1024.0/1024.0,1)
    mem_a = round(memory.available/1024.0/1024.0/1024.0,1)
    mem_u = round(memory.used/1024.0/1024.0/1024.0,1)
    cpu = str(psutil.cpu_percent(5))
    load1, load5, load10 = psutil.getloadavg()
    cpu_usage = (load10/os.cpu_count()) * 100
    await event.reply(f"**OS:** {platform.system()}\n**Version:** {platform.release()}\n**Arch:** {platform.architecture()}\n**CPU Utilization:** {cpu}%\n**CPU Load Past 10 Min:** {cpu_usage}\n**Total Disk Space:** {total} GB\n**Available Disk Space:** {free} GB\n**Memory Utilization:** {mem_p}%\n**Total Memory:** {mem_t} GB\n**AvailableMemory Free:** {mem_a} GB\n**Memory Utilized:** {mem_u} GB\n")
    return
