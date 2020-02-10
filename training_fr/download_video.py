from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=1R_oXwwQxW0")
yt = yt.streams.get_by_itag(133).download("videos")