import re
import os
import pickle

def censor_text(text):
    profane_words = ['bad', 'offensive', 'inappropriate']  # Replace with your own list of profane words
    
    # Load the machine learning model
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'rf_model.pkl')
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Compile a regular expression pattern to match any profane word
    pattern = re.compile(r'\b({})\b'.format('|'.join(profane_words)), re.IGNORECASE)

    # Replace profane words with asterisks
    censored_text = pattern.sub('*'*len(text), text)

    return censored_text
