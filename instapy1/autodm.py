from instabot import Bot
 
bot = Bot()
bot.login(username="user.namenew2023",
          password="forsecurity")
message = "check my profile for new updates"
list_of_userid = ["ardentarts", "anjana.ramachandran.12"]
bot.send_messages(message, list_of_userid)