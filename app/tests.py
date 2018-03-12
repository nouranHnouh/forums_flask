from time import sleep
import models
import stores

"""function create members takes three members as input 
and create them using Member class."""

def create_members():
	member1=models.Member("Karen",19)
	member2=models.Member("Jhon",23)
	member3 =models.Member('Nour', 28)
	print(member1)
	print(member2)
	print(member3) 
	return member1,member2,member3

"""add_members takes two list and use for loop to add members
one by one"""
def add_members(members,member_store):
	for member in members:
		member_store.add(member)
	#print store_members 
	return member_store

#link post to member 
# it takes a list as input 

"""print all members"""
def print_all (instance_store):
	print (instance_store.get_all()) 
	print("="*30)
   
"""get id function takes list and id as input 
it gets the id in the list"""
def get_id(member_store,id): 
	print (member_store.get_by_id(id))
	print("="*30)

"""check if entity exist, it takes two input a list and a string member
check if entity exist in a list"""
def check_entity(member_store,member):
        print (member_store.entity_exist(member))
        print("="*30)

#search member by name
def get_member_name(name):
	memberstore=stores.Memberstore()
	member=memberstore.get_by_name(name)
	for m in member:
		print (m.name) 
	print ("="*30) 

def update_member(member):
	new_member=models.Member(member.name,member.age)
	new_member.id=3 
	#if new_member is not member:
		#print ("new member and member are not the same")
	
	#print(new_member)
	new_member.name="Sally"
	new_member.age=40
	member_store=stores.Memberstore()
	member_store.update(new_member)
	print(member_store.get_by_id(member.id)) 
	print("="*30)




"""delete member or post"""
def delete (all_member,id):
	all_member.delete(id) 
	


	
"""create instances and call functions"""
member_instances=create_members()

#testing members 

member1,member2,member3=member_instances
members_store=stores.Memberstore()
add_members(member_instances,members_store)
print_all(members_store) 
get_id(members_store,1)
get_id(members_store,2)
check_entity(members_store,member1)
print_all(members_store) 

delete(members_store,1)
check_entity(members_store,member1)
print_all(members_store)

get_member_name("Jhon")
update_member(member3)
print_all(members_store)



"""create post and return them"""
def create_post(member):
	post1=models.Post("python list", "python list offers a way to structure data",member[1].id)
	sleep(2)#sleep for 2 second 
	post2=models.Post("writing algorithm", "writing alogarithm is very effective when it comes to analyzing problems",member[2].id)
	sleep(2)
	post3=models.Post("classes in python ", " classes is a template that has information like variables and functions",member[0].id)
	sleep(3)
	post4=models.Post("hello","I love Apple",member[2].id)
	sleep(3)
	post5=models.Post("Engineer ","person trained and skilled in design, construction and use of engineering machines",member[0].id)
	
	print (post1)
	print (post2)
	print (post3)
	print (post4)
	print (post5)
	print("="*30)

	return post1,post2,post3,post4,post5
"""add post to posts list """
def add_posts(posts,post_store):
	for post in posts:
		post_store.add(post)
"""update post"""
def update_post(post):
	new_post=models.Post(post.title,post.content,1)
	#create new post id
	new_post.id=2
	#if new_post is not post:
		#print("post and new_post are not the same")

	new_post.title="Global Warming"
	new_post.content="pollution from factories can contribute to global warming "
	post_store=stores.Poststore()
	post_store.update(new_post)
	print(post_store.get_by_id(post.id))
	print("="*30)


#print member with their corresponding posts 
def get_member_post(member_store,post_store):
	members_with_posts=member_store.get_members_with_posts(post_store.get_all())
	for m in members_with_posts:
		print("{} has posts:".format(m.name))
		for p in m.posts:
			print("\t{}".format(p))
	print ("="*30)
#test get_top_two() method 
def top_two(member_store,post_store):
	top_two_members=member_store.get_top_two(post_store.get_all())
	for member in top_two_members:
		print("{} has posts:".format(member.name))
		for post in member.posts:
			print ("\t{}".format(post))
	print("="*30)

def post_time(post_store):
	posts=post_store.get_post_by_date() 
	print("post sorted by date: ")
	for p in posts:
		print(str(p))





#test post class 
post_instances=create_post(member_instances) 
post1,post2,post3,post4,post5=post_instances
post_store=stores.Poststore() 
add_posts(post_instances,post_store) 
#print_all(post_store) 
#update_post(post2)
#print_all(post_store) 

get_member_post(members_store,post_store)
top_two(members_store,post_store)

#test get post by date
post_time(post_store)









