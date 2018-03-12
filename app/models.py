
import datetime
class Member():
	
	""" this class has the following members attributes:
	name of the member and age of the member
	list posts to save members posts
	and id of the member"""
	def __init__(self,name,age):
		self.name=name
		self.age=age 
		#list of the post 
		self.posts=[]
		self.id=0
	def __str__(self):
		return 'Name:{}\nAge: {}'.format(self.name,self.age)
	def __repr__(self):
		return "<name:%s age %s>"%(self.name,self.age)
		
class Post():
	"""class post will show the posts that members create
	it has the following attributes:
	date: show date of post
	title of the post 
	content of the post 
	member_id:to get the post by id of member
	and an id of the post"""
	def __init__(self,title,content,member_id=0):

		self.title=title
		self.content=content
		self.member_id=member_id
		self.id=0
		self.date=datetime.datetime.now() 

	def __str__(self):
		return 'Title: {} \nContent: {}'.format(self.title, self.content)
	def __repr__(self):
		return "<title:%s content %s>"%(self.title,self.content)	


		

