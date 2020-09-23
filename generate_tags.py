import re
import nltk
from nltk import pos_tag


def generate_tags(text):
    text = pos_tag(text.split())
    return text