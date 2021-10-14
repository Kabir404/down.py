import sys
import time
import requests
import argparse

from progress.bar import Bar

parser = argparse.ArgumentParser(description='down.PY - A simple file downloader made with Python')
parser.add_argument("url", help="Link for the file download(Direct Downloads Only)")
args = parser.parse_args()

def main() :
  start = time.time()

  file_url = args.url

  filename = file_url.split("/")[-1]

  #send get request
  response = requests.get(file_url, stream=True)

  file_size = int(response.headers.get("Content-Length", 0))

  with Bar(f'Downloading {filename}', fill='▇',suffix='%(percent)d%% %(eta)ds') as bar:
      #write file in binary mode
      with open(filename,"wb") as file:
          #iterate over the response in data chunks
          for data in response.iter_content(chunk_size=file_size//100):
              file.write(data)   
              bar.next()  #increase downloading bar 
            
  print("Took " + str('{0:.2f}'.format(time.time() - start)) + " Seconds to download " + str(filename))


if __name__ == "__main__" :
  main()