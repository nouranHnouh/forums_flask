
import itertools 
class Basestore():
	def __init__(self,data_provider,last_id):
		self._data_provider=data_provider
		self._last_id=last_id 

	#get_all method returns members and posts
	def get_all(self):
		#get all the members
		#print (Memberstore.members)
		return self._data_provider
   
    #add members and posts to lists
	def add(self,item):
		#add the members and their id to the list 
		item.id=self._last_id
		#append item to list
		self._data_provider.append(item)
		self._last_id+=1 

	"""method that return member and post id """
	def get_by_id(self,id):
		all_members=self.get_all()
		result=None
		for member in all_members:
			if member.id==id:
				result=member 
				break 
		return result 

	 #update method, updtaes member and post data
	def update(self,item):
		result=item
		all_members=self.get_all()
		for m,current_member in enumerate(all_members):
			if item.id==current_member.id: 
				all_members[m]=item  
				break
		return result 


	"""method check if member exist in the list"""
	def entity_exist(self,item):
		result = True 
		if self.get_by_id(item.id) is None:
			result = False
		return result

	#delete methods deltes member or post 
	#that member creates using member id
	def delete(self,id):
		all_members=self.get_all()
		id_member=self.get_by_id(id)
		all_members.remove(id_member)

class Memberstore(Basestore):
	#store members
	members=[]
	last_id=1
	def __init__(self):
		super().__init__(Memberstore.members,Memberstore.last_id)
	"""get member by name,and return it """
	def get_by_name(self,name):
		all_members=self.get_all()
		for member in all_members: 
			if member.name==name:
				yield member 
    
    #get_members_with_post method returns the member with their corresponding post
	def get_members_with_posts(self,all_posts):
		all_members=self.get_all()
		for member,post in itertools.product(all_members,all_posts):
			if member.id==post.member_id:
				member.posts.append(post)
		for member in all_members:
			yield member 
	
	#get top 2 people who wrote more posts 
	def get_top_two(self,posts):
		#create list
		storted_members=list(self.get_members_with_posts(posts))
		#sort list, from members with most written posts
		storted_members.sort(key=lambda member:len(member.posts),reverse=True)
		yield storted_members[0]
		yield storted_members[1]

class Poststore(Basestore):
	"""class poststore has store the members posts in posts list"""
	posts=[] 
	last_id=1 # get post by id 

	def __init__(self):
		super().__init__(Poststore.posts,Poststore.last_id)

	"""sort posts by date"""
	def get_post_by_date(self):
		all_posts=list(self.get_all())
		all_posts.sort(key=lambda post: post.date,reverse=True)
		return all_posts

		

   















