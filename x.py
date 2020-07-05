files = """
RoguesCallery45-10-04016BlondesPreferGentlemen.mp3
RoguesCallery45-11-08018LitteDropsOfRain.mp3
RoguesCallery46-06-13051TheCorpseIDidntKill.mp3
""".strip().split('\n')

for file in files:
    date = "19" + file[13:21]
    ordinal = file[22:24]
    title = list(file[24:].rpartition(".mp3")[0])

    for i, s in enumerate(title):
        if s.isupper():
            title[i] = ' ' + s

    # Comprehension method
    # title = [(' ' + s) if s.isupper() else s for s in title]

    title = "".join(title).strip()

    for orig, new in (
        ("Amystery", "A Mystery"),
        ("Theres", "There's"),
        ("Didnt", "Didn't"),
        ("Playhouse137", "Playhouse 137"),
        ):
        title = title.replace(orig, new)

    result = (f"Rogue's Gallery - " + f"{ordinal} - {date} - {title}.mp3")
    # os.rename(file, result)

    print(result)

