import os
import wget
import constants

#url = "https://instagram.fsaw2-2.fna.fbcdn.net/v/t50.2886-16/121626566_769569767232426_7898949840618761369_n.mp4?_nc_ht=instagram.fsaw2-2.fna.fbcdn.net&_nc_cat=106&_nc_ohc=esmcRlRHnmcAX_jIEZa&oe=5FF1BFCD&oh=75731340e14432609683054471e24d60"


def download_file(url, file_name):
    path_to_save = os.path.join(
        constants.download_dir, file_name) + constants.video_extension
    wget.download(url, path_to_save)

    return path_to_save
