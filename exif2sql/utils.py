import pandas as pd
import exifread
import os

from datetime import datetime
from pathlib import Path
from typing import List
from multiprocessing import Pool
from clean import clean_all

picture_globs = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']


def get_extension(filename):
    filename, file_extension = os.path.splitext(filename)
    return file_extension.lower()


def get_pictures(directory: Path):
    pics = []
    for glob in picture_globs:
        pics.extend(directory.rglob(glob))
    return pics


def get_exif(path: Path):
    # try:
    # noinspection PyTypeChecker
    with open(path, 'rb') as f:
        return path, exifread.process_file(f)
    # except:
    #     return


def multiprocess_extract_exif(fnames: List[Path], processes=5):
    with Pool(processes) as pool:
        return pool.map(get_exif, fnames)


def parse_date(exif_info):
    if not exif_info:
        return
    date = exif_info.get('Image DateTime')
    if not date:
        return
    try:
        return datetime.strptime(str(date.values), '%Y:%m:%d %H:%M:%S')
    except ValueError:
        return

def get_panda_dataframe(folder_names):
    pics_filenames = []
    for folder in folder_names:
        abs_path = Path(folder).resolve()
        pics_filenames.extend(get_pictures(abs_path))

    cleaned_data = clean_all(multiprocess_extract_exif(pics_filenames))

    return pd.DataFrame(cleaned_data)

