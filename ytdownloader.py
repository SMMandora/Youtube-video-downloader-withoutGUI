from pytube import YouTube
 
youtube_video_url = input("Paste the link of the youtube video you want to download : ")
 
try:
    print('............DOWNLOAD OPTIONS............ ')
    print('1.Highest Resolution Available ')
    print('2.Lowest Resolution Available ')

    o = int(input('Enter the option number : '))
    yt_obj = YouTube(youtube_video_url)
 
    filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
    if o == 1:
        filters.get_highest_resolution().download()
        print('Video Downloaded In Highest Resolution ')
    elif o == 2:
        filters.get_lowest_resolution().download()
        print('Video Downloaded In Lowest Resolution ')
    else : 
        print('No such option available')
except Exception as e:
    print(e)
