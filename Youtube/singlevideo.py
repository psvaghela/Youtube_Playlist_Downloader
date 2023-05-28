from pytube import YouTube
yt = YouTube("https://youtu.be/rAVnE7hswl8",use_oauth=True, allow_oauth_cache=True)
#yt = yt.get('mp4', '720p')
yt = yt.streams.get_highest_resolution()
yt.download('F:\\binod\\')