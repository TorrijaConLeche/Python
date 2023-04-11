# Upgrade: Include search feature (with pytube)
# Upgrade: Download playlist option
from pytube import YouTube
import re
import time

# Inicialize the var asking for the URL
yt = YouTube(
    input("Welcome, input the URL of the video you want to download: \n"))

# Ask for download video or audio
extension = input("Input file type (video / audio)\n").lower()


if extension == "video":
    opt = input("Do you want to download with specific resolution? (Y / N)\n")
    if opt.lower() == "y":
        resolution = input(
            "Input resolution (include the letter 'p') (144p / 240p / 360p / 480p / 720p / 1080p )\n")

        streams = yt.streams.filter(only_video=True, res=resolution)
        if not streams:
            print("Sorry, the resolution you asked for isn't available")
            exit()
    else:
        streams = yt.streams.filter(only_video=True)

    for s in streams:
        test = str(s)
        test = re.findall(r'\w+', test)
        print("Option: ", test[2])
        print("------------------")
        print("Extension:    ", test[5])
        print("Resolution:   ", test[7])
        print("FPS:          ", test[9])
        print("")


elif extension == "audio":
    streams = yt.streams.filter(only_audio=True)
    for s in streams:
        test = str(s)
        test = re.findall(r'\w+', test)

        print("Option: ", test[2])
        print("------------------")
        print("Extension:    ", test[5])
        print("Bitrate:   ", test[7])
        print("")

    if not streams:
        print("Sorry, the resolution you asked for isn't available")
        exit()
else:
    print("Please enter a valid file type (audio / video)")
    exit()

tag = input("Input the option number that you want: ")
stream = yt.streams.get_by_itag(tag)
try:
    stream.download()
    print("\nDownloading...", yt.title)
    time.sleep(1.5)
    print("\nDownload completed")
except:
    print("Input a valid number please")
