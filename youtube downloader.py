from pytube import YouTube

try:
	yt = YouTube("https://www.youtube.com/watch?v=VZe5vXH7TcE")
	d_video = yt.streams.get_by_itag(22)
	d_video.download()
except:
	print("Connection Error!")

print('Task Completed!')
