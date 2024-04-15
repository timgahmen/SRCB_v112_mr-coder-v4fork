"""
Plugin for both public & private channels!
"""

import time, os, asyncio
from .. import bot as Drone
from .. import userbot, Bot, AUTH
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_bulk_msg
from main.plugins.helpers import get_link, screenshot

from telethon import events, Button, errors
from telethon.tl.types import DocumentAttributeVideo

from pyrogram import Client 
from pyrogram.errors import FloodWait

from ethon.pyfunc import video_metadata
from ethon.telefunc import force_sub

ft = f"To use this bot you've to join @{fs}."

batch = []

@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/cancel'))
async def cancel(event):
    if not event.sender_id in batch:
        return await event.reply("No batch active.")
    batch.clear()
    await event.reply("Done.")
    
@Drone.on(events.NewMessage(incoming=True, from_users=AUTH, pattern='/batch'))
async def _batch(event):
    if not event.is_private:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft) 
    if s == True:
        await event.reply(r)
        return       
    if event.sender_id in batch:
        return await event.reply("You've already started one batch, wait for it to complete mr owner!")
    async with Drone.conversation(event.chat_id) as conv: 
        if s != True:
            await conv.send_message("Send me the message link you want to start saving from, as a reply to this message.", buttons=Button.force_reply())
            try:
                link = await conv.get_reply()
                try:
                    _link = get_link(link.text)
                except Exception:
                    await conv.send_message("No link found.")
                    return conv.cancel()
            except Exception as e:
                print(e)
                await conv.send_message("Cannot wait more longer for your response!")
                return conv.cancel()
            await conv.send_message("Send me the number of files/range you want to save from the given message, as a reply to this message.", buttons=Button.force_reply())
            try:
                _range = await conv.get_reply()
            except Exception as e:
                print(e)
                await conv.send_message("Cannot wait more longer for your response!")
                return conv.cancel()
            try:
                value = int(_range.text)
                if value > 100000:
                    await conv.send_message("You can only get upto 1,00,000 files in a single batch.")
                    return conv.cancel()
            except ValueError:
                await conv.send_message("Range must be an integer!")
                return conv.cancel()
            batch.append(event.sender_id)
            await run_batch(userbot, Bot, event.sender_id, _link, value) 
            conv.cancel()
            batch.clear()


async def run_batch(userbot, client, sender, link, _range):
    for i in range(_range):
        timer = 60
        if i < 25:
            timer = 10
        if i < 100 and i > 25:
            timer = 10
        if i < 100000 and i > 100:
            timer = 15
        if not 't.me/c/' in link:
            if i < 25:
                timer = 3
            else:
                timer = 5
                
        try: 
            if not sender in batch:
                await client.send_message(sender, "Batch completed.")
                break
        except Exception as e:
            print(e)
            await client.send_message(sender, "Batch completed.")
            break
            
        try:
            # Download the video using get_bulk_msg function
            video_path = await get_bulk_msg(userbot, client, sender, link, i) 
            
            # Compress the downloaded video using ffmpeg
            compressed_video_path = f"{video_path}_compressed.mkv"
            compress_command = f'ffmpeg -hide_banner -loglevel quiet -i \"{video_path}\" -c:v libx265 -preset ultrafast -x265-params "level=6.1:profile=main:high-tier=1:packetizer=hvc1" -crf 25 -vf "scale=854:480" -color_primaries 1 -color_trc 1 -colorspace 1 -pix_fmt yuv420p -color_range 2 -r 30 -c:a libopus -b:a 192k -vbr on -map 0 \"{compressed_video_path}\"'
            subprocess.run(compress_command, shell=True)
            
            # Upload the compressed video
            await client.send_file(sender, compressed_video_path)
            
            # Delete the compressed video file
            os.remove(compressed_video_path)
        except Exception as e:
            print(e)
            await client.send_message(sender, "An error occurred while processing the video.")
            break
            
        # Sleep to avoid Floodwait and protect account
        protection = await client.send_message(sender, f"Sleeping for `{timer}` seconds to avoid Floodwaits and Protect account!")
        await asyncio.sleep(timer)
        await protection.delete()
