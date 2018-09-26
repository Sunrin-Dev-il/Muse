import os
import pytube
import moviepy.editor as mp

def video(v_url):
    try:
        url = "https://www.youtube.com"
        url += v_url

        yt = pytube.YouTube(url)
        vids = yt.streams.filter(progressive=True, file_extension='mp4').first()

        path = video_path()
        vids.download(path)

        video = vids.default_filename
        video_name = video.split(".")[0]

        path = os.path.join(path,video_name)
        if not video_convert(path):
            raise()

        return 1
    except:
        return 0

def video_path():
    path = os.getcwd()
    dir_name = "Music"
    path = os.path.join(path,dir_name)

    if not os.path.isdir(path):
        os.mkdir(path)

    return path

def video_convert(path):
    try:
        clip = mp.VideoFileClip(path+".mp4")
        clip.audio.write_audiofile(path+".mp3")

        clip.close()
        os.remove(path+".mp4")

        return 1

    except:
        return 0

if __name__ == '__main__':
    video("/watch?v=BzYnNdJhZQw")