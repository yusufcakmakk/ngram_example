import json
import re
import utils


__clean_html_regex = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
__clean_punctuation_regex = re.compile('•+|�+|½+|+|+|\^+|≥+|□+|+|+|​+|“+|”+|\'+|"+|!+|‘+|’+|#+|\*+|·+|§+|è+|=+')
__clean_punctuation_ws_regex = re.compile('\(+|\)+|-+|\.+|–+|\,+|\?+|!+|/+|%+|:+|₺+|;+|&+|_+')
__remove_html_table_regex = re.compile(r'<table(.*?)</table>')
__remove_html_bold_regex = re.compile(r'<b>(.*?)</b>')

deascify_map = {"Ç":"C","Ş":"S","İ":"I","Ğ":"G","Ü":"U","Ö":"O",
                "ç":"c","ş":"s","ı":"i","ğ":"g","ü":"u","ö":"o",
                "â":"a","û":"u"}


def clean_html(raw_html):
    cleantext = re.sub(__clean_html_regex, ' ', str(raw_html))
    return cleantext


def clean_punctuation(raw_text):
    cleantext = re.sub(__clean_punctuation_regex, '', str(raw_text))
    cleantext = re.sub(__clean_punctuation_ws_regex, ' ', cleantext)
    return cleantext

def remove_text_between_tag(raw_text):
    cleantext = re.sub(__remove_html_table_regex, ' ', raw_text)
    return cleantext

def clean_whitespace_newline(raw_text):
    return ' '.join(raw_text.split())

def __clean_numbers(raw_text):
    return (' '.join([re.sub(r'\d+', '<number>', token) for token in raw_text.split()])).strip()

def apply_preprocess(string:str, remove_numbers:bool=False, lower_case:bool=True, deascify:bool=True)->str:
    # new_string = clean_html(string)
    new_string = clean_punctuation(string)
    new_string = clean_whitespace_newline(new_string)
    if remove_numbers:
        new_string = __clean_numbers(new_string)
    if lower_case:
        new_string = utils.unicode_tr(new_string).lower()

    if deascify:
        deascified = ""
        for char in new_string:
            if char in deascify_map:
                deascified += deascify_map[char]
            else:
                deascified += char
        new_string = deascified
    
    return new_string
