# use PYTHON 3
#Script to download from web,
#No proxy handling

import urllib.request
import shutil


# Download the file from `url` and save it locally under `file_name`:
for i in range(1,6):
  url = 'http://ces.iisc.ernet.in/phylo_workshop/phylo_2014/Day{0}.zip'.format(i)
  filename = '/home/littleboy/temp/phylo_2014_Day{0}.zip'.format(i)
  print (filename)
  with urllib.request.urlopen(url) as response, open(filename, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

