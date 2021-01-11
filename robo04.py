from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='', password='')

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 100)
	session.set_do_like(enabled = True, percentage= 100)
	session.follow_user_followers(['isetups'], amount=3, randomize=False)
	session.follow_user_following(['isetups'], amount=3, randomize=False)
	comentarios = ['Nice shot!', 'Love your posts']
	session.set_do_comment(enabled=True, percentage=95)
	session.set_comments(comentarios, media= 'Photo')
	session.join_pods()