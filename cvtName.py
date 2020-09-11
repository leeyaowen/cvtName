from PIL import Image
from PIL.ExifTags import TAGS
import glob
import os
import timeit


def rename():
    path = input('path=?\n')
    all_file = sorted(glob.glob('%s/*.jpg' % path), key=os.path.getmtime)
    if len(all_file) == 0:
        print('no file!\n')
        return None
    plot = input('plot=?\n')
    i = 0

    start = timeit.default_timer()
    print('please wait...')

    for filename in all_file:
        i = i+1
        metadata = {}
        # noinspection PyBroadException
        try:
            with Image.open(filename) as img:
                info = img._getexif()
            for tag, value in info.items():
                tagname = TAGS.get(tag, tag)
                metadata[tagname] = value
            camtime = metadata['DateTimeOriginal']
            datetime = str('%s-%s-%s-%s' % (camtime[0:4], camtime[5:7], camtime[8:10], camtime[11:13]))

            os.rename(filename, '%s/%s-%s_%s.jpg' % (path, plot, datetime, str(i)))
        except Exception:
            print('error in %s\n' % filename)
            continue

    stop = timeit.default_timer()

    print('Complete!')
    print('time : %s\n' % str(stop-start))


while __name__ == '__main__':
    rename()
