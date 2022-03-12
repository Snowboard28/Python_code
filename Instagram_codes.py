import dbm
import os
/* import psutil
from string import Template


def string_formatting():
    str_0 = "Python"
    str_1 = "Genius"

    single_old_style = "Hello %s" % str_1
    multi_old_style = "%s_%s" % (str_0, str_1)
    map_old_style = "%(first)s_%(second)s" % {"first": str_0, "second": str_1}
    
    print(single_old_style)
    print(multi_old_style)
    print(map_old_style)

    f_string_format = f"This number will be formatted: {100000:,}"
    print(f_string_format)
    

def cpu_info():
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
          


def data_tellen():
    data = [
        [3,4,5,6,], [8,9,0,1],[4], [9,4,3,2,1], [5,5,6,7], [2,5]]
    print (sum(data,[]).count(5))
    
def Quantity():
    title = 'Quantity'
    val1 = 100
    val2 = 2456
    val3 = 25
    width = len(title)
    print(title)
    print(str(val1).rjust(width))
    print(str(val2).rjust(width))
    print(str(val3).rjust(width))
    
def database_x():
    with dbm.open('db.db', 'c') as db:
                  db["key1"] = 'Value A01'
                  db["key2"] = 'Value B03'

    with dbm.open('db.db', 'c') as db:
                  print(db["key1"])
                  print(db["key2"])
    
def listdir():
    print(os.path)
    print(os.curdir)

    for name in os.listdir('.'):
        print(name)
        
def string_templates():
    t = Template('Hello, $name!')
    print(t.substitute(name='Arie'))
    print(t.substitute(name='Willem'))
                       
def parse_url():
    import urllib.parse

    url = 'https://ex.com:80/path/to?a=b#x'
    parsed = urllib.parse.urlparse(url)
    print (' Scheme: ', parsed.scheme)
    print (' Host: ', parsed.hostname)
    print (' Port: ', parsed.port)
    print (' Path: ', parsed.path)
    print (' Query: ', parsed.query)
    print (' Fragment', parsed.fragment)
    
def reverse_string():
    data = [3, 5, 8, 9, 10, 13, 21, 211]
    print(data)
    for i in range(len(data) // 2):
        data[i], data[-1 -i] = data[-1 -i], data[i]
    print(data)
    data.reverse()
    print(data)
    
        
