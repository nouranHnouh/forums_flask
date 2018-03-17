from app import models
members_data=[models.Member("Nancy",20),
              models.Member("Narmdha",27),
              models.Member("Mark",33),
              models.Member("George",40)]
post_data=[models.Post("python","python is an interpreted high-level programming language",members_data[0].id),
           models.Post("Telecommunication network","is electronic system of switches and nodes, that aalows for data transfer and exchange between multiple users",members_data[3].id),
           models.Post("Artificial intelligence","is intellegence demonstrated by machine such as self-driving cars ",members_data[0].id),
		   models.Post("what is HTML?","HTML is standard markup language for creating web pages",members_data[1].id),
		   models.Post("Electrical Engineering","is the field that deals with study and application of electricity and electronics",members_data[2].id),
		   models.Post("circuit components","Resistors, Capacitors, and inductors are examples of circuit components",members_data[1].id),
		   models.Post("circuit simulation","matlab can be used to simulate circuits",members_data[2].id)] 
def test(member_store,post_store):
	for member in members_data:
		member_store.add(member)
	for post in post_data:
		post_store.add(post)


