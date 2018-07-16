# cc.py
Simple multi threaded tool to extract domain related data from commoncrawl.org

**Usage**
```
ccp.py [-h] -d domain -o path [-t THREADS] [-f index1] [-f index2]

necessary arguments:
  -d, --domain   The domain you want to search for in CC data.
  -o, --outfile  The path and filename where you want the results to be saved to.

optional arguments:
  -h, --help     Show help message and exit
  -f, --filter   Use only indices which contain this string
  -t, --threads  Threads for requests
```

**Examples**

Search for github.com and save to /home/folder/cc/data.txt
```
python3 ccp.py -d github.com -o /home/folder/cc/data.txt
```

Search for github.com in indices which contain "CC-MAIN-2017-09", save to data.txt
```
python3 ccp.py -d github.com -o ./data.txt -f CC-MAIN-2017-09
```

Search for github.com in indices which contain "2013" and "2014", save to data.txt
```
python3 ccp.py -d github.com -o ./data.txt -f 2014 -f 2013
```

Search for github.com using 10 threads, save to data.txt
```
python3 ccp.py -d github.com -o ./data.txt -t 10
```

**grep tips**

I am no grep expert but I know how to extract data, if you have better solutions for my existing commands OR additional ideas what to search for: __PR__

1. Find entries which end with popular file extension indicating dynamic pages etc:
```
grep -i -E '\.(php|asp|dev|jsp|wsdl|xml|cgi|json|html)$' /home/folder/cc/data.txt
```

2. Find interesting files like backups, archives, log files...
```
grep -i -E '\.(zip|rar|tar|bkp|sql|zip|bz2|gz|txt|bak|conf|log|error|debug|yml|lock|template|tpl)$' /home/folder/cc/data.txt
```

3. Find entries which contain popular strings like "admin" etc:
```
grep -i -E '(admin|account|debug|control|config|upload|system|secret|environment|dashboard)$' /home/folder/cc/data.txt
```

4. Find files which begin with "." (htaccess, ...):
```
grep -i -E '\/\.' /home/folder/cc/data.txt
```

5. Find obvious backup files:
```
grep -i -E '(\.bkp|\.bak|backup|\.dump|\.sql)' /home/folder/cc/data.txt
```

6. Extract subdomains:
```
sed -e 's|^[^/]*//||' -e 's|^www\.||' -e 's|/.*$||' /home/folder/cc/data.txt | grep -v ":" | grep -v "@" | grep -v "?" | grep -v "/" | sort -u
```

7. Find urls with parameters in it:
```
grep -i -E '(\?|\&)(.*?)=((.*?)|)' /home/folder/cc/data.txt | sort -u
```

**Dependencies**
* python3
* requests
* argparse
* json

**Information**

This project was initially forked from [cc.py](https://github.com/si9int/cc.py) but since I refactored it completely and si9int took another path I decided to create a stand alone project.