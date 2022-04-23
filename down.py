from __future__ import print_function
from progress.bar import Bar

import sys
import time
import requests
import argparse
import datetime

#Convert spent seconds to hours
def sec_to_hours(seconds):
    h=str('{0:.0f}'.format(seconds//3600))
    m=str('{0:.0f}'.format((seconds%3600)//60))
    s=str('{0:.1f}'.format((seconds%3600)%60))
    out="{} hours {} mins {} seconds".format(h, m, s)
    return out

def download(url,printtime=False,chunksize=100):
        
    start = time.time()#Start the timer

    file_url = url #Get the file Direct-Download URL
    filename = file_url.split("/")[-1] #Get The filename to save as

    #Send GET request
    response = requests.get(file_url, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))

    #Download the file in chunks and report it to the user using a progress bar
    with Bar(f'Downloading {filename}', fill='▇',suffix='%(percent)d%% [%(eta_td)s] (%(iter_value)s)') as bar:
          #Write file in binary mode
        with open(filename,"wb") as file:
            #Iterate over the response in data chunks
            for data in response.iter_content(chunk_size=file_size//100):
                file.write(data)   
                bar.next()  #Increase downloading bar 
    
    #If the user wants to show the time it took to download then show it
    if printtime==True: 
        print("Took " + str(sec_to_hours(time.time() - start)) + " to download " + str(filename))

def main() :
    
    parser = argparse.ArgumentParser(description='down.PY - A simple file downloader made with Python')
    parser.add_argument("url", help="Link for the file download(Direct Downloads Only)")
    parser.add_argument("-c","--chunksize", dest="chunksize", help="Define download chunk size(file size divided by value - default=100)", required=False)
    parser.add_argument("-t","--time-taken", dest="printtime", help="Show the time that has taken to download the file(default=true)", required=False , bool=True)
    args = parser.parse_args()
    
    download(args.url,args.printtime,args.chunksize)       


if __name__ == "__main__" :
    main()
