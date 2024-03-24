#coding:utf-8
import json
import re
import sys

def to_json():
    with open('language.i18n') as i18n:
        i18nline=i18n.readlines()
        nuew={}
        k=0
        nuew[k]=[]
        for i in i18nline:
            if ("v:" not in i) and (i!='\n'):
                i=re.sub('(k:")|("\n)','',i)
                nuew[k].append(i)
            if i=='\n':
                k+=1
                nuew[k]=[]
    with open('language_en.json',mode='+w') as i18n:
        skillline=json.dumps(nuew)
        i18n.write(skillline)

to_json()
