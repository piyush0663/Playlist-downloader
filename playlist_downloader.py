from pytube import Playlist

py=Playlist("https://www.youtube.com/playlist?list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz")

print(f'downloading:{py.title}')

for video in py.videos:
    video.streams.first().download()

print('complete')
