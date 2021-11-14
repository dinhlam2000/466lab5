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

output: tf_idf.csv -> first column is the document name and the rest is tf_idf computations of all words
        words.csv -> all words that map to tf_idf

```
