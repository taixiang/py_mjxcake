#!/usr/bin/python

# -*- coding: utf-8 -*-
import six, os
from zhconv import convert_for_mw
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cakesite.settings")
django.setup()
from poem.models import Poetry,PoetryAuthor

if six.PY2:
    import sys

    reload(sys)
    sys.setdefaultencoding('utf-8')

POETRY_DIRECTORY = './json/'


def trans(name):
    file_path = os.path.join(POETRY_DIRECTORY, name)

    raw = open(file_path, 'r').read()

    content = convert_for_mw(unicode(raw), 'zh-cn')

    output_path = os.path.join('./poetry/', name)

    with open(output_path, 'w') as f:
        f.write(content)


# map(trans, os.listdir(POETRY_DIRECTORY))
def convert(txt):
    return convert_for_mw(txt, 'zh-cn')


def getData():
    poetrys = Poetry.objects.all()[150000:311828]
    for poe in poetrys:
        try:
            title = convert(poe.title)
            content = convert(poe.content)
            author = convert(poe.author)
            poe.title = title
            poe.content = content
            poe.author = author
            print(title)
            print(content)
            print(author)
            poe.save()
        except:
            f = open("./ids", "a")
            f.write(str(poe.id) + "\n")
            f.close()
            pass

    print("====end")


def getData2():
    poetrys = PoetryAuthor.objects.all()[1:12653]
    for poe in poetrys:
        try:
            name = convert(poe.name)
            intro = convert(poe.intro)
            poe.name = name
            poe.intro = intro
            poe.save()
        except:
            f = open("./authors", "a")
            f.write(str(poe.id) + "\n")
            f.close()
            pass

    print("====end")

if __name__ == "__main__":
    getData2()
