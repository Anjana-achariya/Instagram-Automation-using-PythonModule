import instagrapi
from instagrapi import Client
import random
username, password= "user.namenew2023","forsecurity"
client= Client()
client.login(username,password)

hashtag="cats"
comments=["Awesome","cute","nice"]
medias=client.hashtag_medias_recent(hashtag,20)
for i,media in enumerate(medias):
	client.media_like(media.id)
	print(f"liked post number {i+1} of hashtag{hashtag}")
	if i%5==0:
		client.user_follow(media.user.pk)
		print(f"Followed user{ media.user.username}")
		client.media_comment(media.id,"Awesome post")
		comment=random.choice(comments)
		print(f"Commented {comment} under post number {i+1}")