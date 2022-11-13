def __mod_twse__():
    structure = {
        "LoadBanner":{
            "way1":"banner",
            "way2":"files\\banner"
        },
        "Language":"ENG"
    }
    try:
        with open(r'files\config\user.json', 'w') as file_json:
            file_json.write(structure)
    except FileNotFoundError:
        with open(r'config\user.json', 'w') as file_json:
            file_json.write(structure)
