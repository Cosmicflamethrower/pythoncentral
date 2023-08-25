import json


def expgain(content, ID):
    exp_gain = 0
    print(content, flush=True)
    for i in content:
        exp_gain += 1
    folder_path = "E:\\Data\\DeathMetal64\\user_data"
    file_path = folder_path + '\\' + str(ID) + '.json'
    with open(file_path, 'rt') as file:
        data = json.load(file)
        level = int(data["level"])
        exp = int(data["experience"])
        exp_new = exp + exp_gain
        exp = exp_new
        exp_needed = round((level ** 1.5) + 25)
        while exp >= exp_needed:
            print('{} {}'.format(level, exp), flush=True)
            level += 1
            exp -= exp_needed
            print('{} {}'.format(level, exp), flush=True)
        exp_data = {
            "level": level,
            "experience": exp
        }
        exp_dta = json.dumps(exp_data)
        print(exp_data, flush=True)
    with open(file_path, 'wt+') as file:
        file.write(exp_dta)
