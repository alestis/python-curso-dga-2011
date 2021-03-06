# -*- coding: utf-8 -*-

__all__ = ['Translator']

import urllib
import simplejson as json
#import json

def call(appId, url, params):
        """Calls the given url with the params urlencoded
        """
        params['appId'] = appId
        response = urllib.urlopen(
            "%s?%s" % (url, urllib.urlencode(params))).read()
        rv =  json.loads(response.decode("UTF-8-sig"))

        if isinstance(rv, basestring) and \
                rv.startswith("ArgumentOutOfRangeException"):
            raise ArgumentOutOfRangeException(rv)

        if isinstance(rv, basestring) and \
                rv.startswith("TranslateApiException"):
            raise TranslateApiException(rv)

        return rv

def translate(appId, text, to_lang, from_lang=None, 
            content_type='text/plain', category='general'):
        params = {
            'text': text.encode('utf8'),
            'to': to_lang,
            'contentType': content_type,
            'category': category,
            }
        if from_lang is not None:
            params['from'] = from_lang
        return call(appId,
            "http://api.microsofttranslator.com/V2/Ajax.svc/Translate",
            params)


def main():
	API_KEY = "FAAB868F7EA0F933924B8A1D9879DFD5895EF14A"
	result = translate(API_KEY,"Hola Mundo","en","es")

	print result


if __name__ == "__main__":
    main()
