from __future__ import print_function
from progress.bar import Bar

import sys
import time
import requests
import argparse
import datetime


def sec_to_hours(seconds):
    h=str('{0:.0f}'.format(seconds//3600))
    m=str('{0:.0f}'.format((seconds%3600)//60))
    s=str('{0:.1f}'.format((seconds%3600)%60))
    out="{} hours {} mins {} seconds".format(h, m, s)
    return out

def download(url,printtime):
    start = time.time()

    file_url = url

    filename = file_url.split("/")[-1]

    #send get request
    response = requests.get(file_url, stream=True)

    file_size = int(response.headers.get("Content-Length", 0))

    with Bar(f'Downloading {filename}', fill='▇',suffix='%(percent)d%% [%(eta_td)s] (%(iter_value)s)') as bar:
          #write file in binary mode
        with open(filename,"wb") as file:
            #iterate over the response in data chunks
            for data in response.iter_content(chunk_size=file_size//100):
                file.write(data)   
                bar.next()  #increase downloading bar 
    if printtime==True: 
        print("Took " + str(sec_to_hours(time.time() - start)) + " to download " + str(filename))

def main() :
    parser = argparse.ArgumentParser(description='down.PY - A simple file downloader made with Python')
    parser.add_argument("url", help="Link for the file download(Direct Downloads Only)")
    args = parser.parse_args()
    
    download(args.url,True)       


if __name__ == "__main__" :
    main()
