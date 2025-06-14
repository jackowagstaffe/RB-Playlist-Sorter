import sys
import csv
import m3u8
from pprint import pprint

# We need to get the key information from RB playlists in order to sort them
# and output them in a format which can be imported back into RB
#
# The RB txt output includes key information but cannot be imported
# The RB m3u8 format can be imported but does not include key information
#
# We need to export to TXT, parse this, then export to m3u8 for importing back into RBi

key_order = [
    'Fm',
    'Ab',
    'Cm',
    'Eb',
    'Gm',
    'Bb',
    'Dm',
    'F',
    'Am',
    'C',
    'Em',
    'G',
    'Bm',
    'D',
    'F#m',
    'A',
    'Dbm',
    'E',
    'Abm',
    'B',
    'Ebm',
    'F#',
    'Bbm',
    'Db',
]

file_name = sys.argv[1]

## Parse the txt output file
tracks = []
with open('./' + file_name + '.txt', encoding='utf-16-le') as tsv:
    for line in csv.DictReader(tsv, delimiter='\t'):
        tracks.append(line)

## Parse the m3u8 file and add the data to the existing tracks list
m3_playlist = m3u8.load('./' + file_name + '.m3u8')
for segment in m3_playlist.segments:
    title = segment.title
    file = segment.uri

    for i, track in enumerate(tracks):
        if title == track['Artist'] + ' - ' + track['Track Title']:
            track['Full Title'] = title
            track['File'] = file

## Sort the tracks as desired
sorted_tracks = sorted(tracks, key=lambda t: key_order.index(t["Key"]))

## Export an m3u8 file which can be imported back into Rekordbox
with open(file_name + '_sorted.m3u8', 'w+') as output:
    output.write('#EXTM3U\n')

    for track in sorted_tracks:
        output.write(track["Full Title"] + '\n')
        output.write(track["File"] + '\n')

