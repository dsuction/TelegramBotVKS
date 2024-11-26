from bs4 import BeautifulSoup
import requests


def find_data_materials(class_school, subject):
    data = {}
    m = requests.get("https://schoolhm.ru/", verify=False)
    soup = BeautifulSoup(m.text, "lxml")
    bank = soup.find_all("li")

    for object in bank:
        if class_school in object.text and "ЮФМЛ" in object.text:
            path = object.find("a").attrs["href"]
            bank_tasks = requests.get(path, verify=False)
            pile = filter(lambda s: s != "\n",
                          BeautifulSoup(bank_tasks.text, "lxml").find("div", class_="entry-content").contents)
            soup1 = BeautifulSoup(bank_tasks.text, "lxml")

            titles = soup1.css.select("h6")
            contents = soup1.css.select("p")
            for content in pile:
                if content in titles:
                    if "год" in content.text:
                        year = content.text
                        data[year] = []
                        flag = True
                        count_index = -1
                    else:
                        flag = False
                        title = content.text
                        data[year].append({title: []})
                        count_index += 1
                elif content in contents:
                    try:
                        if flag:
                            data[year].append((content.text, content.a.attrs['href']))
                            count_index += 1
                        else:
                            data[year][count_index][title].append((content.text, content.a.attrs['href']))
                    except:
                        pass

    if subject == 'all':
        return data['2023-2024 учебный год']
    else:
        for element in data['2023-2024 учебный год']:
            if type(element) is dict:
                for key in element.keys():
                    if key.lower() == subject.lower():
                        return element[key]
