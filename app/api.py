from flask import request,jsonify,abort
from app import models
from app import app, member_store, post_store



@app.route("/api/topic/all")
def topic_get_all():
	#convert every objects in the list to dictionary format
	posts = [post.__dict__() for post in post_store.get_all()]
	#use jsonify to convert objects to JSON format
	return jsonify(posts) 
	