# cc.py
Extracting URLs of a specific target based on the results of "commoncrawl.org"

**Usage**
```
cc.py [-h] -d domain -o path [-i index1] [-i index2]

positional arguments:
  -d, --domain   The domain you want to search for in CC data.
  -o, --outfile  The path and filename where you want the results to be saved to.

optional arguments:
  -h, --help     Show help message and exit
  -i, --index    Use only this specified index
```

**Examples**
```
python3 cc.py -d github.com -o /home/folder/cc/data.txt
cat /home/folder/cc/data.txt | grep user
```

```
python3 cc.py -d github.com -o ./data.txt -i CC-MAIN-2017-09
cat ./data.txt | grep user
```

```
python3 cc.py -d github.com -o ./data.txt -i CC-MAIN-2017-09 -i CC-MAIN-2017-04
cat ./data.txt | grep user
```

**Dependencies**
* python3
* requests
* argparse
* json

**Information**

This project was initially forked from [cc.py](https://github.com/si9int/cc.py) but since I refactored it completely and si9int took another path I decided to create a stand alone project.