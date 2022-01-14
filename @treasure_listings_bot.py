import requests
import json
import tweepy
import time

#auth header from discord channel
headers = {
    'authorization': '',
}

#add account specific keys
consumer_key = ''
consumer_secret_key = ''
access_token = ''
access_token_secret = ''

#authenticating to access the twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    try:
        r = requests.get(
        'https://discord.com/api/channels/910004403849793546/messages', headers=headers)

        jsonn = json.loads(r.text)
        
        embeded_title = jsonn[0]['embeds'][0]['title']
        

        embeded_name = jsonn[0]['embeds'][0]['fields'][0]['value'].replace(
            ')', '').replace('(', '')
        embeded_collection = jsonn[0]['embeds'][0]['fields'][1]['value'].replace(
            ')', '').replace('(', '')
        embeded_price = jsonn[0]['embeds'][0]['fields'][2]['value']
        embeded_quantity = jsonn[0]['embeds'][0]['fields'][3]['value']
        embeded_buyer = jsonn[0]['embeds'][0]['fields'][4]['value']
        embeded_footer = jsonn[0]['embeds'][0]['footer']['text']
        embeded_img = jsonn[0]['embeds'][0]['thumbnail']['url']
        filename = 'image_name.jpg'
        txt_log = 'log.txt'
        img_data = requests.get(embeded_img).content
    
    
        t = open('log.txt', 'r')
        t_contents = t.read()
        print(t_contents)

        tweet_text = f'Item Listed: \n{embeded_name} \n Collection: \n {embeded_collection} \n Listing Price: {embeded_price} \n Quantity: \n {embeded_quantity} \n Time: \n {embeded_buyer}'

        if embeded_name != t_contents:
            with open(filename, 'wb') as handler:
                handler.write(img_data)
            with open(txt_log, 'w') as handler:
                handler.write(embeded_name)

            api.update_status_with_media(filename=filename, status=tweet_text)
            print(tweet_text)
        else:
            pass

        time.sleep(300)
    except:
        print('error')
        
