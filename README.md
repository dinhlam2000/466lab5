# CSC466-Lab-5


## set up
```bash
virtualenv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

#textVectorizer.py
```bash
python textVectorizer.py [directory name] [stop words directory name]
[directory name] = directory of the Documents
[stop words] = directory of the stop words list

OUTPUT: 
[directory name]_tf_idf.csv_[stop words directory].csv -> first column is the document name and the rest is tf_idf computations of all words
[directory name]_words_[stop words directory].csv -> all words that map to tf_idf out file

```
