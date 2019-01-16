from youtube_dl import YoutubeDL
# 1. Donwload a single youtube video
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=3bJkVSMs4dw"])

# 2. Download multiple youtube videos
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=HXkh7EOqcQ4', 'https://www.youtube.com/watch?v=EFsqoXvpBnQ'])

# 3. Download audio
# option = {
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(option)
# dl.download(['https://www.youtube.com/watch?v=wLu4-sV91D8'])

# 4. Search and then download the first video
# option = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1,
# }
# dl = YoutubeDL(option)
# dl.download(["Phut ban dau - Vu"])

# 5. Sample 5: Search and then download the first audio
# options = {
#     'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads': 1, # Tell downloader to download only the first entry (audio)
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['Noi lam sao het'])