#import flask for webframework
from flask import Flask
from app import stores
from app import dummy_data,models

app = Flask(__name__)
member_store=stores.Memberstore()
post_store=stores.Poststore()
dummy_data.test(member_store,post_store)
from app import views

	
	
