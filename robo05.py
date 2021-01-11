from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='', password='')

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 100)
	session.set_do_like(enabled = True, percentage= 100)
	# session.follow_likers(['isetups'], photos_grab_amount= 1, follow_likers_per_photo = 2, randomize = True, sleep_delay = 600, interact = True)
	session.follow_commenters(['isetups'], amount=2, daysold=100, max_pic= 1, sleep_delay=600, interact=True)
	comentarios = ['Top de mais!', 'Gata','Perfeito(a)!', 'Love your posts','Nice shot!', 'Love your posts','Nice shot!', 'Love your posts','Nice shot!', 'Love your posts','Nice shot!', 'Love your posts']
	session.set_do_comment(enabled=True, percentage=95)
	session.set_comments(comentarios, media= 'Photo')
	session.join_pods()