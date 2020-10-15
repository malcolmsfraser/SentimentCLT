#!/usr/bin/env python
import click
import boto3

client = boto3.client('comprehend')

@click.command()
@click.option("--phrase")
def hello(phrase):
    language = client.detect_dominant_language(
    Text=phrase
)
    lang = language['Languages'][0]['LanguageCode']
    response = client.detect_sentiment(
    Text=phrase,
    LanguageCode=lang
)

    if lang in ['de', 'pt', 'en', 'it', 'fr', 'es']:
        wordlist = phrase.split()
        wordlist2 = phrase.split()
        pos = []
        for word in wordlist:
            parts = client.detect_syntax(
            Text=word,
            LanguageCode=lang
        )
            word = wordlist2.pop(0)
            part = parts['SyntaxTokens'][0]["PartOfSpeech"]["Tag"]
            sent = client.detect_sentiment(
                Text=word,
                LanguageCode=lang)['Sentiment']
            pos.append( (word,part,sent))
        click.echo(f"{'#'*80}\nThis phrase has {response['Sentiment']} sentiment!\n{response['SentimentScore']}\n\nThe language code is {lang}\n\nPart of speech and word sentiment:\n{pos}\n{'#'*80}")
    else:
        click.echo(f"{'#'*80}\nThis phrase has {response['Sentiment']} sentiment!\n{response['SentimentScore']}\n\nThe language code is {lang}\n{'#'*80}")


if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    hello()