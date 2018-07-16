# cc.py
Simple multi threaded tool to extract domain related data from commoncrawl.org

**Usage**
```
ccp.py [-h] -d domain -o path [-t THREADS] [-i index1] [-i index2]

necessary arguments:
  -d, --domain   The domain you want to search for in CC data.
  -o, --outfile  The path and filename where you want the results to be saved to.

optional arguments:
  -h, --help     Show help message and exit
  -i, --index    Use only this specified index
  -t, --threads  Threads for requests
```

**Examples**

Search for github.com and save to /home/folder/cc/data.txt
```
python3 ccp.py -d github.com -o /home/folder/cc/data.txt
```

Search for github.com in index "CC-MAIN-2017-09", save to data.txt
```
python3 ccp.py -d github.com -o ./data.txt -i CC-MAIN-2017-09
```

Search for github.com in index "CC-MAIN-2017-09" & "CC-MAIN-2017-04", save to data.txt
```
python3 ccp.py -d github.com -o ./data.txt -i CC-MAIN-2017-09 -i CC-MAIN-2017-04
```

Search for github.com using 10 threads, save to data.txt
```
python3 ccp.py -d github.com -o ./data.txt -t 10
```

**Dependencies**
* python3
* requests
* argparse
* json

**Information**

This project was initially forked from [cc.py](https://github.com/si9int/cc.py) but since I refactored it completely and si9int took another path I decided to create a stand alone project.