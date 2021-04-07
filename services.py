import json
import urllib.request
import string
import random
import time

# start_time = time.time()


def generateRandomYoutudeURL(API_KEY, amountofvideos = 1):
    randomVideo = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,amountofvideos,randomVideo)
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))

    bdYoutubeVideos = ['https://www.youtube.com/watch?v=' for i in range(0, amountofvideos)]

    i = 0
    for data in results['items']:
        videoId = (data['id']['videoId'])
        bdYoutubeVideos[i] += videoId
        i += 1
    return bdYoutubeVideos


def generateRandomHabrURL():
    return 0




# print(generateRandomYoutudeURL())



# print("--- %s seconds ---" % (time.time() - start_time))
