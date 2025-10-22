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

# Challenge Enhancements

**Validate images for each event(you can download these images and assume that the source of truth is local)**

### Questions
- Validate as in the image is the correct image?
- Validate that the image aligns with the correct file path? (i.e Not taking into account the contents of the image itself?)
- Does this mean the approach needed to take of getting the feed data is supposed to be through HTML? The images aren't part of the api call I found to commentary and would require multiple api calls (which is ok but don't know if that's the correct approach)

**Describe how you will automate this to generate an alert indicating the failure (use any tool you are comfortable with)**

Random text

**How to improve the code execution if you need to run the same code against parallel matches running at the same time, let's say 10?**

### Questions

- Is this going to an api call?
- Is this going to be a script thats run 

There's a few ways to go about this

**Approach 1: Brute Force (not ideal)**

```
# provide the urls for each match and file separately (For now this should be hard coded without knowing how this is going to be called, maybe from another system that already has the xml feed and provide the api url)

matches_dict = {
    "match_api_url1": path_to_feed_file.rtf
    "match_api_url2": path_to_feed_file.rtf
    "match_api_url3": path_to_feed_file.rtf
    "match_api_url4": path_to_feed_file.rtf
    "match_api_url5": path_to_feed_file.rtf
    "match_api_url6": path_to_feed_file.rtf
    "match_api_url7": path_to_feed_file.rtf
    "match_api_url8": path_to_feed_file.rtf
    "match_api_url9": path_to_feed_file.rtf
    "match_api_url10": path_to_feed_file.rtf
}

for match_api_url in matches_dict:
    feed_file_path = matches_dict[match_api_url]
    print(FeedComparison(feed_file_path, match_api_url).compare_feed_data())


# Not ideal as it has to wait for each one to finish before doing the second match.
```

**Approach 2: threading**

```
    Updating this method to use threading to do the api calls

    import threading

    def _make_api_call(url):
        return requests.get(url)

    def _fetch_data(self, url: str):
        for match_api_url in matches_dict:
            thread = theading.thread(target=_make_api_call, args=(match_api_url))

        # add some error handling
            - Allow retries?
            - Allow some to fail and continue but log the ones that fails?
```