#!/usr/bin/env bash

import os

import cloudscraper
import m3u8
from bs4 import BeautifulSoup

live_events = "https://futbollibre.net/en-vivo/liga-profesional-argentina/"
scraper = cloudscraper.CloudScraper()
soup = BeautifulSoup(scraper.get(live_events).text, "html.parser")

streams = []
for link in soup.find_all("a"):
    urls = [l for l in link.get("href").split() if l.endswith("m3u8")]
    streams = streams + urls

playlist = m3u8.M3U8()
for i, l in enumerate(streams):
    playlist.add_playlist(f"#EXTINF:0,Canal {i+1}")
    playlist.add_playlist(l)

os.makedirs("_build", exist_ok=True)
playlist.dump("_build/live.m3u")
