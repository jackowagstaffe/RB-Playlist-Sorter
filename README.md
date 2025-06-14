# Rekordbox Playlist Sorter

## Introduction
I like to sort all of my playlists into key order in ascending 5ths for easier
in key mixing but there is no way to automatically do this in rekordbox.

Rekordbox has the ability to export playlists to a txt file which in practice is 
a tab separated values file and to the m3u8 playlist format. It only has the 
ability to import in the m3u8 format. Annoyingly the txt format contains 
information about track key but the m3u8 format doesn't, so in order to export, 
sort, then re-import the playlist using key information both formats have to be
exported.

This repo contains a simple Python script which takes a file name as an 
argument. It automatically imports both a .txt and .m3u8 file with that name 
from the current directory, sorts it into ascending 5ths key order starting at 
Fm then outputs it to a new file: `{file_name}_sorted.m3u8` which can be 
imported back into rekordbox.

## Process to use the script

To sort a playlist called *My Tracks* you would:

1) Export both .txt and .m3u8 versions of the playlist you want to sort to the same directory as the python script using right-click export on the playlist name
2) Run the script `python3 "My Tracks"`
3) Import the sorted playlist back into rekordbox with File > Import > Import Playlist and selecting My Tracks_sorted.m3u8
