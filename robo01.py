from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='', password='')

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 100)
	session.set_do_like(enabled = True, percentage= 100)

	session.like_by_tags([''], amount=5)

	comentarios = ['salve !', 'deixa o like']
	session.set_do_comment(enabled=True, percentage=95)
	session.set_comments(comentarios, media= 'Photo')
	session.join_pods()