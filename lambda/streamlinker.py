import json

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'modules'))
import streamlink as sl



def stream_to_url(url, quality='best'):
    streams = sl.streams(url)
    if streams:
        return streams[quality].to_url()
    else:
        return ("No steams were available")

 
def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,GET'


        },
        'body': stream_to_url("https://www.twitch.tv/virtulabs")
    }