import re
import nltk
from nltk import pos_tag


# function for generating pos tags
def generate_tags(text):
    text = re.sub(r'[^\w\s]+', ' ', text)
    text = pos_tag(text.split())
    return text
