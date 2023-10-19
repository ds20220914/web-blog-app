"Here are all the functions that handle the tables in database "
from sqlalchemy import text
from db import db



def find_all_blogs(community):
    """find all blogs by given community name"""
    query = text("SELECT blog_name,id FROM Blogs WHERE community=:community")
    right_blogs = db.session.execute(query,{"community":community})
    blogs=right_blogs.fetchall()
    return blogs

def find_userid_by_name(name):
    """find the user's id by given name"""
    query = text("SELECT id FROM users WHERE username=:name")
    right_id = db.session.execute(query,{"name":name})
    id1=right_id.fetchall()
    return id1[0]

def create_blog(topic,content,writer,community):
    """create a blog using given information of the topic,content,
       the writer name and community of the blog."""
    sql =text( "INSERT INTO Blogs (blog_name, content,time,user_id,community) VALUES"
                "(:topic, :content,NOW(),:writer,:community)")
    db.session.execute(sql,
       {"topic":topic,"content":content,"writer":writer,"community":community})
    db.session.commit()


def find_text(community,blog_id ):
    """find the content text of a blog using given community name and the blog's
       id"""
    query = text("SELECT content FROM Blogs WHERE id=:id AND community=:community")
    right_blogs = db.session.execute(query,{"id":blog_id,"community":community})
    blog=right_blogs.fetchone()
    return blog

def find_all_blogs_byname(name,community):
    """find all the blogs that has the same name in one community"""
    query = text("SELECT blog_name,id FROM Blogs"
                 " WHERE Blog_name=:Blog_name AND community=:community")
    right_blogs = db.session.execute(query,{"Blog_name":name, "community":community})
    blogs=right_blogs.fetchall()
    return blogs

def add_comment(id1,content):
    """add a comment to the blog"""
    query = text(" INSERT INTO Comments (Blog_id,content) VALUES (:id , :content)")
    db.session.execute(query,{"id":id1, "content":content})
    db.session.commit()

def find_comments(blog_id):
    """ find all the comments of a blog"""
    query = text(" SELECT content FROM Comments WHERE Blog_id=:id ")
    right_comments = db.session.execute(query,{"id":blog_id})
    comments=right_comments.fetchall()
    return comments

def all_my_blogs(username):
    """ find all the blogs that user has posted"""
    list1=[]
    query1 = text("SELECT * FROM Blogs WHERE user_id=:writer AND community=:school")
    right_blogs1 = db.session.execute(query1,{"writer":username,"school":"school"})
    query2 = text("SELECT * FROM Blogs WHERE user_id=:writer AND community=:life")
    right_blogs2 = db.session.execute(query2,{"writer":username,"life":"life"})
    query3 = text("SELECT * FROM Blogs WHERE user_id=:writer AND community=:sport")
    right_blogs3 = db.session.execute(query3,{"writer":username,"sport":"sport"})
    query4 = text("SELECT * FROM Blogs WHERE user_id=:writer AND community=:game")
    right_blogs4 = db.session.execute(query4,{"writer":username,"game":"game"})
    blogs1=right_blogs1.fetchall()
    blogs2=right_blogs2.fetchall()
    blogs3=right_blogs3.fetchall()
    blogs4=right_blogs4.fetchall()
    if len(blogs1)==0:
        list1.append([])
    if len(blogs1)!=0:
        list1.append(blogs1)
    if len(blogs2)==0:
        list1.append([])
    if len(blogs2)!=0:
        list1.append(blogs2)
    if len(blogs3)==0:
        list1.append([])
    if len(blogs3)!=0:
        list1.append(blogs3)
    if len(blogs4)==0:
        list1.append([])
    if len(blogs4)!=0:
        list1.append(blogs4)
    return list
def delete_blog(id1):
    """ delete one single blog using given blog's id"""
    for i in id1:
        query = text(" DELETE FROM Blogs WHERE id=:i ")
        db.session.execute(query,{"i":i})
        db.session.commit()

def find_all_all_blogs():
    """find all the blogs that in the app and divide into
       different groups according to their community"""
    list1=[]
    query1 = text("SELECT * FROM Blogs WHERE community=:school")
    right_blogs1 = db.session.execute(query1,{"school":"school"})
    query2 = text("SELECT * FROM Blogs WHERE community=:life")
    right_blogs2 = db.session.execute(query2,{"life":"life"})
    query3 = text("SELECT * FROM Blogs WHERE community=:sport")
    right_blogs3 = db.session.execute(query3,{"sport":"sport"})
    query4 = text("SELECT * FROM Blogs WHERE community=:game")
    right_blogs4 = db.session.execute(query4,{"game":"game"})
    blogs1=right_blogs1.fetchall()
    blogs2=right_blogs2.fetchall()
    blogs3=right_blogs3.fetchall()
    blogs4=right_blogs4.fetchall()
    list1.append(blogs1)
    list1.append(blogs2)
    list1.append(blogs3)
    list1.append(blogs4)
    return list
def check_if_admin(user_id):
    """check if this user is admin"""
    query=text("SELECT id FROM Admin WHERE admin_id=:id ")
    admin=db.session.execute(query,{"id":user_id[0]})
    admin_id=admin.fetchall()
    return admin_id

def recently_added_blog(user):
    """find the user's latest added blog"""
    query1=text("SELECT MAX(id) FROM Blogs WHERE user_id=:id ")
    right_blogs1 = db.session.execute(query1,{"id":user})
    id1=right_blogs1.fetchone()
    return id1

def add_blog_password(blogid,password):
    """add a private password to one single blog"""
    query1 = text("INSERT INTO Private_blogs (private_blog_id,password) VALUES (:id,:password) ")
    db.session.execute(query1,{"id":blogid, "password":password})
    db.session.commit()

def check_if_blog_password(blog_id):
    """check if a blog is private and has password"""
    query1 = text("SELECT password FROM Private_blogs WHERE private_blog_id=:id ")
    right_blogs1 = db.session.execute(query1,{"id":blog_id})
    password=right_blogs1.fetchone()
    return password

def find_writer_name(blogid):
    """ find the name of blog writer"""
    query1 = text("SELECT U.username FROM Blogs B LEFT JOIN Users U"
                   " ON B.user_id=U.id WHERE B.id=:id")
    right_name = db.session.execute(query1,{"id":blogid})
    name=right_name.fetchone()
    return name
