"""модуль считывания страницы веб-сайта или локального файла в переменную"""

import urllib.request
import urllib.error
import urllib.parse



def get_page (address):
    """функция получения содержимого страницы веб-сайта"""
    try:
        web = urllib.request.urlopen(address)
        content = str(web.read())

        return content
    #в случае ЛЮБОЙ ошибки (на данном этапе)
    except:
        return False

def get_file (path):
    """функция получения содержимого локального файла"""
    try:
        with open (path) as f:
            content = f.read()
        
        return content
    except:
        return False

