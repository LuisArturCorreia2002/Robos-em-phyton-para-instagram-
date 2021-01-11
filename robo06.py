from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='', password='')

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 100)
	session.set_do_like(enabled = True, percentage= 100)
	session.unfollow_users(amount=2, nonFollowers=True, style="FIFO", unfollow_after=3*60, sleep_delay=450)
	comentarios = ['Nice shot!', 'Love your posts','Nice shot!', 'Love your posts','Nice shot!', 'Love your posts','Nice shot!', 'Love your posts','Nice shot!', 'Love your posts','Nice shot!', 'Love your posts']
	session.set_do_comment(enabled=True, percentage=95)
	session.set_comments(comentarios, media= 'Photo')
	session.join_pods()