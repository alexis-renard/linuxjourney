import sys
import markdown2
from os import listdir
from os.path import isfile, isdir, join
from bs4 import BeautifulSoup


def HTMLtoXMLparser(html):
    """
    Will parse the received html to a proper and valid XML
    """
    soup = BeautifulSoup(html, features='lxml')
    print(soup.prettify)
    # soup = BeautifulSoup()

def getEnglishLessons(path):
    """
    Will return the needed info about the english lessons
    """
    gettitle = [f for f in listdir(path) if isfile(join(path, f))]
    lessons_directories = [f for f in listdir(path) if isdir(join(path, f))]
    print(lessons_directories)
    for lesson_name in lessons_directories:
        print("New Lesson")
        lessons = [f for f in listdir(path+lesson_name) if isfile(join(path+lesson_name, f))]
        for lesson_part in lessons:
            html = markdown2.markdown_path(path+lesson_name+"/"+lesson_part)
            HTMLtoXMLparser(html)
        print("------")
    return(True)


def main(argv):
    ## Path variables
    based_path="/home/zorro/GI04/TX/TX-linuxjourney/linuxjourney/lessons/locales/"
    english_lessons="en_english/"
    french_lessons="en_french/"

    englishLessons = getEnglishLessons(based_path+english_lessons)


if __name__ == '__main__':
    main(sys.argv[1:])
