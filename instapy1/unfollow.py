import instabot 
from instabot import Bot 
from time import sleep
from random import randint
import my_config 

bot = Bot()

bot.login(username = my_config.USERNAME,password =my_config.PASSWORD)

non_followers = set(bot.following) - set(bot.followers)

for non_follower in non_followers:
    try:
        bot.unfollow(non_follower)
        sleep(randint(6,12))
    except Exception as e:
        print(e)
        sleep(randint(30,300))