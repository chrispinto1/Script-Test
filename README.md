# System Requirements:

- python 3 (not tested with python 2)


# Steps to run script:

- ```python3 -m venv .env``` or ```python -m venv .env```

- ```source .env/bin/activate```
- ```pip install -r requirements.txt```

This python script accepts an optional command line argument, by default it's set to False. This argument determines whether you want a full report on unmatched events instead of only checking for matches (small added feature). By default it only checks if there are any matches and returns True or False if so
- ```python3 feed_comparison.py``` or ```python3 feed_comparison.py False``` or ```python feed_comparison.py True```


# Output

| script argument | output                                                             |
|:-----------------:|------------------------------------------------------------------|
|True             | **Any unmatched**: The following events are not included in<br>the XML feed: comma_separate_list of unmatched<br>event ids<br><br>**All matched**: All the events are included in the xml feed|
|      No Argument or False      | **If any matched**: True<br><br>**if no matches**: False                    |