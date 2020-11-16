# containerized-sentiment-analysis-CLT

## Contents
This container contains a command-line tool takes a string phrase, and performs sentiment analysis on it.
    Returns overall phrase sentiment
    Returns language
    Returns part of speech and relative sentiment for each word

## Run it yourself
***Okay...so this doesnt actually run because I removed my AWS keys when making this code public

```bash
docker pull malcolmsfraser/sentimentclt:latest
docker run -it malcolmsfraser/sentimentclt
python sentiment.py --phrase " **text here** "
```
