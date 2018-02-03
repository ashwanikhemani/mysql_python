# -*- coding: utf-8 -*-
"""
Script in Python that goes over user database and creates users on Intercom

"""
import MySQLdb
from intercom.client import Client

#intialize values to connect to the database 
hostname="host"
username="db_user"
password="pwd"
database_name="db_name"

#Create mysqldb connection 
myConn = MySQLdb.connect(host=hostname,user=username,passwd=password,db=database_name)
cur=myConn.cursor();

# Configuration of client
# Valid token to be given for authorization 
intercom = Client(personal_access_token='access_token')

#Fetch list of users from DB and create them on intercom 
cur.execute("select * from user")
for id,user_name,user_email in cur.fetchall():
    print "id:",id,"user name:",user_name,"user email:",user_email
    user = intercom.users.create(user_id=id,email=user_email, name=user_name)

# List Users
for user in intercom.users.all():
    print user
    
# Create or Update User  
user = intercom.users.create(user_id=id,email=user_email, name=user_name)
user = intercom.users.create(used_id=id, email='new_email@new.com')

# delete a user
user = intercom.users.find(user_id=id)
deleted_user = intercom.users.delete(user)

# Submit job to create users 
intercom.users.submit_bulk_job(create_items=[{'user_id': 10, 'email': 'a@new.com'}, {'user_id': 11, 'email': 'b@new.com'}])

# Submit job to delete users
intercom.users.submit_bulk_job(delete_items=[{'user_id': 10, 'email': 'a@new.com'}, {'user_id': 11, 'email': 'b@new.com'}])

