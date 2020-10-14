from resources import strings_en
from resources import strings_ko

ko = strings_ko
en = strings_en


def getStrings(lan: str):
    if lan == "ko":
        return ko
    else:
        return en
