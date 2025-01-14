# CREATED BY MYSELF WITH ALL EMOTIONS
import asyncio
import socket
import speedtest
from .. import bot as Drone
from telethon import events, Button
from telethon.tl import functions, types
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import psutil, os, signal
from time import time
from datetime import datetime as dt
from psutil import (boot_time, cpu_count, cpu_percent, disk_usage,
                    net_io_counters, swap_memory, virtual_memory)
from main.utils import TimeFormatter, humanbytes, botStartTime

SIZE_UNITS = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#
@Drone.on(events.NewMessage(incoming=True, pattern="/status"))
async def show_status(event):
    currentTime = TimeFormatter(time() - botStartTime)
    osUptime = TimeFormatter(time() - boot_time())
    total, used, free, disk = disk_usage('/')
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    sent = humanbytes(net_io_counters().bytes_sent)
    recv = humanbytes(net_io_counters().bytes_recv)
    cpuUsage = cpu_percent(interval=0.5)
    p_core = cpu_count(logical=False)
    t_core = cpu_count(logical=True)
    swap = swap_memory()
    swap_p = swap.percent
    stt = dt.now()
    ed = dt.now()
    ms = (ed - stt).microseconds / 1000
    p = f"{ms}ms"
    memory = virtual_memory()
    mem_t = humanbytes(memory.total)
    mem_a = humanbytes(memory.available)
    mem_u = humanbytes(memory.used)
    await event.reply(f"""`
Bot Uptime: {currentTime}
OS: {osUptime}
Ping: {p}
UL: {sent} | DL: {recv}
-------------------------
Total Disk: {total}
Used: {used}
Free: {free}
-------------------------
CPU: {cpuUsage}%
Utilized: {swap_p}%
Total Cores: {t_core}
Physical Core: {p_core}
------------------------- 
Total RAM: {mem_t}
Free RAM: {mem_a}
Used: {mem_u}`""")
    return 
#----------------------------------------------------------------------------------------------------------------------------------------------------------------#


@Drone.on(events.NewMessage(incoming=True, pattern="/ping"))
async def test(event):
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        server_name = st.results.server['host']
        server_country = st.results.server['country']
        server_latency = st.results.ping
        download_speed = round(st.download() / 10**6, 2)  # convert to Mbps and limit to 2 decimal points
        upload_speed = round(st.upload() / 10**6, 2)  # convert to Mbps and limit to 2 decimal points
        client_ip = st.results.client['ip']
        isp = st.results.client['isp']
        sponsor = st.results.server['sponsor']

        result = f"Server: {server_name}, \n" \
                 f"Country: {server_country}, \n" \
                 f"Download Speed: {download_speed} Mbit/s, \n" \
                 f"Upload Speed: {upload_speed} Mbit/s, \n" \
                 f"Ping: {server_latency} ms, \n" \
                 f"ISP: {isp}, \n" \
                 f"Sponsor: {sponsor}, \n" \
                 f"Client IP: {client_ip}"
        await event.reply(f"**{result}**")
    except speedtest.SpeedtestException as e:
        await event.reply(f"**Error: {e}**")


@Drone.on(events.NewMessage(incoming=True, pattern="/cpu"))
async def storage(event):
    cpu = psutil.cpu_percent()
    load1, load5, load15 = psutil.getloadavg()
    cpu_usage1 = round((load1/os.cpu_count()) * 100,2)
    cpu_usage5 = round((load5/os.cpu_count()) * 100,2)
    cpu_usage15 = round((load15/os.cpu_count()) * 100,2)
    cpu_total = psutil.cpu_count()
    cpu_physical = psutil.cpu_count(logical=False)
    cpu_usable = len(psutil.Process().cpu_affinity())
    freq = psutil.cpu_freq()
    cpu_cur = round(freq.current,2)
    cpu_max = freq.max
    cpu_min = freq.min
    await event.reply(f"`CPU Utilization: {cpu}%\nTotal CPU Cores: {cpu_total}\nUsable CPU Cores: {cpu_usable}\nPhysical CPU Cores: {cpu_physical}\n---------------------------------\nCPU Frequency :-\nCurrent: {cpu_cur} mhz\nMAX: {cpu_max} mhz\nMIN: {cpu_min} mhz\n---------------------------------\nLoad Past 1 Min: {cpu_usage1} %\nLoad Past 5 Min: {cpu_usage5} %\nLoad Past 15 Min: {cpu_usage15} %\n`")
    return

@Drone.on(events.NewMessage(incoming=True, pattern="/storage"))
async def storage(event):
    disk= psutil.disk_usage('/')
    d_p = disk.percent    
    d_t = format(disk.total/1024.0/1024.0/1024.0,".2f")
    d_u = format(disk.used/1024.0/1024.0/1024.0,".2f")
    d_f = format(disk.free/1024.0/1024.0/1024.0,".2f")
    memory = psutil.virtual_memory()
    swap = psutil.swap_memory()
    mem_p = memory.percent
    mem_t = format(memory.total/1024.0/1024.0/1024.0,".2f")
    mem_a = format(memory.available/1024.0/1024.0/1024.0,".2f")
    mem_f = format(memory.free/1024.0/1024.0/1024.0,".2f")
    mem_u = format(memory.used/1024.0/1024.0/1024.0,".2f")
    await event.reply(f"`Total Disk Space: {d_t} GB\nAvailable Disk Space: {d_f} GB\nUsed Disk Space: {d_u} GB\nUsed Disk Percentage: {d_p}%\n---------------------------------\nTotal RAM: {mem_t} GB\nAvailable RAM: {mem_a} GB\nFree RAM: {mem_f} GB\nRAM Utilized: {mem_u} GB\nRAM Utilized Percentage: {mem_p}%`")
    return

@Drone.on(events.NewMessage(incoming=True, pattern="/clear"))
async def clear(event):
    try:
        zylern = "rm -rf downloads"
        fetch = await asyncrunapp(
            zylern,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())
        await event.reply("**" + result + "**")
    except FileNotFoundError:
        await event.reply("**Error Occurred **")

@Drone.on(events.NewMessage(incoming=True, pattern="/info"))
async def quick_info(event):
    cpu = str(psutil.cpu_percent()) + '%'
    memory = psutil.virtual_memory()
    available = round(memory.available/1024.0/1024.0/1024.0,2)
    total = round(memory.total/1024.0/1024.0/1024.0,2)
    mem_info = str(available) + ' / ' + str(total) + ' (' + str(memory.percent) + '%)'
    disk = psutil.disk_usage('/')
    free = round(disk.free/1024.0/1024.0/1024.0,2)
    total = round(disk.total/1024.0/1024.0/1024.0,2)
    disk_info = str(free) + ' / ' + str(total) + ' (' + str(disk.percent) + '%)'
    await event.reply(f"`CPU: {cpu}\nDisk: {disk_info}\nMemory: {mem_info}`")
    return

@Drone.on(events.NewMessage(incoming=True, pattern="/memory"))
async def space(event):
    try:
        zylern = "df -H"
        fetch = await asyncrunapp(
            zylern,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())
        await event.reply("**" + result + "**")
    except FileNotFoundError:
        await event.reply("**Install speedtest-cli**")

@Drone.on(events.NewMessage(incoming=True, pattern="/sysinfo"))
async def sysinfo(event):
    try:
        zylern = "neofetch --stdout"
        fetch = await asyncrunapp(
            zylern,
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await fetch.communicate()
        result = str(stdout.decode().strip()) \
            + str(stderr.decode().strip())
        await event.reply("**" + result + "**")
    except FileNotFoundError:
        await event.reply("**Install neofetch ~using source code or apt**")
      
