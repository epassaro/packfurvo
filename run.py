#!/usr/bin/env bash

import os

import m3u8
import requests
from bs4 import BeautifulSoup

channel_url = "https://futbollibre.net/en-vivo/liga-profesional-argentina/"
request = requests.get(channel_url)
soup = BeautifulSoup(request.text, "html.parser")

streams = []
for link in soup.find_all("a"):
    urls = [l for l in link.get("href").split() if l.endswith("m3u8")]
    streams = streams + urls

playlist = m3u8.M3U8()
_ = [playlist.add_playlist(l) for l in streams]

os.makedirs("_build", exist_ok=True)
playlist.dump("_build/live.m3u")
