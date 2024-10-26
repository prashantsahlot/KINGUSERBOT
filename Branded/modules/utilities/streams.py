import asyncio, os, yt_dlp

from . import queues
from ..clients.clients import call
from ...console import USERBOT_PICTURE

from asyncio.queues import QueueEmpty
from pytgcalls.types import MediaStream
from pytgcalls.types import AudioQuality, VideoQuality
from youtubesearchpython.__future__ import VideosSearch

# Path to the cookies file
COOKIES_FILE = "https://github.com/prashantsahlot/KINGUSERBOT/raw/main/cookes.txt"

async def get_result(query: str):
    results = VideosSearch(query, limit=1)
    for result in (await results.next())["result"]:
        url = result["link"]
        try:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        except:
            thumbnail = USERBOT_PICTURE
        
    return url, thumbnail


async def download_with_cookies(url: str, download_path: str):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": download_path,
        "cookiefile": COOKIES_FILE  # Reference the cookies file here
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        ydl.download([url])
    
    return info.get("url")


async def run_stream(link, type):
    if type == "Audio":
        stream = MediaStream(
            media_path=link,
            video_flags=MediaStream.Flags.IGNORE,
            audio_parameters=AudioQuality.STUDIO,
        )

    elif type == "Video":
        stream = MediaStream(
            media_path=link,
            audio_parameters=AudioQuality.STUDIO,
            video_parameters=VideoQuality.HD_720p,
        )

    return stream


async def close_stream(chat_id):
    try:
        await queues.clear(chat_id)
    except QueueEmpty:
        pass
    try:
        return await call.leave_call(chat_id)
    except:
        pass


