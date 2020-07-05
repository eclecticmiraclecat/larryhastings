# old time radio file

## File name

    RoguesCallery45-10-04016BlondesPreferGentlemen.mp3
    RoguesCallery45-11-08018LitteDropsOfRain.mp3
    RoguesCallery46-06-13051TheCorpseIDidntKill.mp3

## Rename

## hard links
```
$ touch x

$ ls -l x
-rw-rw-r-- 1 exsanetol exsanetol 0 Jul   6 01:31 x
```
> -rw-rw-r-- 1

1 is the number of links

```
$ ln x y

$ ls -l
total 0
-rw-rw-r-- 2 exsanetol exsanetol 0 Jul   6 01:31 x
-rw-rw-r-- 2 exsanetol exsanetol 0 Jul   6 01:31 y
```

> -rw-rw-r-- 2

links has increased to 2

## step 0: hard link backups

```
$ mkdir backup

$ for a in * ; do ln $a backup/$a ; done
```

## step 1: get filenames

```
$ ls *.mp3 > x.py
```

## step 2: turn into big string
### add triple quotes
```py 
files = """
RoguesCallery45-10-04016BlondesPreferGentlemen.mp3
RoguesCallery45-11-08018LitteDropsOfRain.mp3
RoguesCallery46-06-13051TheCorpseIDidntKill.mp3
"""
```

## strip, split

> strip will remove whitespaces (left, right, both)

```py
str.lstrip()
str.rstrip()
str.strip()
```

> split will convert string to lists by separator s or if none given will default to separator by whitespace

```py
str.split([s])
```

## step3: turn into big list
```py
files = """
RoguesCallery45-10-04016BlondesPreferGentlemen.mp3
RoguesCallery45-11-08018LitteDropsOfRain.mp3
RoguesCallery46-06-13051TheCorpseIDidntKill.mp3
""".strip().split('\n')
```

## step4: start dissecting

    RoguesCallery45-10-04016BlondesPreferGentlemen.mp3
            date [      ]
  episode number/ordinal [ ]
                      title [                    ]     

### the fields so far
```py
for file in files:
    date = "19" + file[13:21]
    ordinal = file[22:24]
    title = file[24:]
```

## remove .mp3 from title
```py
title = BlondesPreferGentlemen.mp3
```

## partition, rpartition

> before, sep, after

```py
str.partition(sep)
str.rpartition(sep)
```

### the elegance of partition
```py
before, sep, after = s.partition(anything)

# always True
assert before + sep + after == s
```

### partition examples
```py
>>> 'breakafterthe firstspace'.partition(' ')
('breakafterthe', ' ', 'firstspace')
>>> 
>>> 'break after the dot'.partition('.')
('break after the dot', '', '')
>>> 
>>> 'BlondesPreferGentlemen.mp3'.rpartition('.mp3')
('BlondesPreferGentlemen', '.mp3', '')
>>> 
>>> 'BlondesPreferGentlemen.mp3'.rpartition('.mp3')[0]
'BlondesPreferGentlemen'
```

## tip: test as you go along
```py
for file in files:
    date = "19" + file[13:21]
    ordinal = file[22:24]
    title = file[24:].rpartition(".mp3")[0]
    print(date, ordinal, title)
```

```
$ python x.py 
('1945-10-04', '16', 'BlondesPreferGentlemen')
('1945-11-08', '18', 'LitteDropsOfRain')
('1946-06-13', '51', 'The Corpse I Didnt Kill')
```

## add spaces to title
look for capital letters and add space in front

```py
for file in files:
    date = "19" + file[13:21]
    ordinal = file[22:24]
    title = list(file[24:].rpartition(".mp3")[0])

    for i, s in enumerate(title):
        if s.isupper():
            title[i] = ' ' + s
    
    title = "".join(title).strip()
```

## list comprehension method
```py
for file in files:
    date = "19" + file[13:21]
    ordinal = file[22:24]
    title = list(file[24:].rpartition(".mp3")[0])
    title = [(' ' + s) if s.isupper() else s for s in title]
    title = "".join(title).strip()
```

## new results
```
$ python x.py 
('1945-10-04', '16', 'Blondes Prefer Gentlemen')
('1945-11-08', '18', 'Litte Drops Of Rain')
('1946-06-13', '51', 'The Corpse I Didnt Kill')
```

### fix Didnt to Didn't

## str.replace
```py
str.replace(old, new)
```

## exception list
```py
for orig, new in (
    ("Amystery", "A Mystery"),
    ("Theres", "There's"),
    ("Didnt", "Didn't"),
    ("Playhouse137", "Playhouse 137),
    ):
    title = title.replace(orig, new)
```

```
$ python x.py 
('1945-10-04', '16', 'Blondes Prefer Gentlemen')
('1945-11-08', '18', 'Litte Drops Of Rain')
('1946-06-13', '51', "The Corpse I Didn't Kill")
```

## step 5: finish
```py
result = (f"Rogue's Gallery - " +
    f"{ordinal} - {date} - {title}.mp3")
os.rename(file, result)

shutil.move()
```

```
$ python3 x.py 
Rogue's Gallery - 16 - 1945-10-04 - Blondes Prefer Gentlemen.mp3
Rogue's Gallery - 18 - 1945-11-08 - Litte Drops Of Rain.mp3
Rogue's Gallery - 51 - 1946-06-13 - The Corpse I Didn't Kill.mp3
```


