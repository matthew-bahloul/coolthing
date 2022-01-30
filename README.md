This is proof that it is possible to log into a social media site and post a message


example:

# setup
no virtual environment (not recommended)
```
cd path/to/this/repo
pip install -r requirements.txt
```

with virtual environment (recommended)
```
cd path/to/this/repo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

# use
to use this

```
cd path/to/this/repo
python -m main -u <username> -p <password> -m "message 1","message 2", ... "message n"
```
