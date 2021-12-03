# down.py
A simple File Downloader program/library made with Python.

## Dependencies 
### Python Deps.
+ Python 3.9.7+
+ Python PIP
### Python Modules 
+ Progress - https://pypi.org/project/progress/
+ Requests - https://pypi.org/project/requests/
+ Argparse - https://pypi.org/project/argparse/
+ System   - Included with Python
+ Time     - Included with Python

## Usage 
For normal usage
```` 
python3 down.py <HTTP Direct Download>
````

For using it in scripts as a library
````
import down

down.download("<HTTP Direct Download>",False) #The first is the download link and the second option is 
                                              #if you want to show the time after the download is compleate
````
It will download the file where the script is executed.
