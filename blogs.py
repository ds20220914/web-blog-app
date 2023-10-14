from db import db
from sqlalchemy import text


def find_all_blogs(community):
    query = text("SELECT blog_name,id FROM Blogs WHERE community=:community")
    right_blogs = db.session.execute(query,{"community":community})
    blogs=right_blogs.fetchall()
    return blogs

def find_userid_by_name(name):
    query = text("SELECT id FROM users WHERE username=:name")
    right_id = db.session.execute(query,{"name":name})
    id=right_id.fetchall()
    return id[0]

def create_blog(topic,content,writer,community):
    sql =text( "INSERT INTO Blogs (blog_name, content,time,user_id,community) VALUES (:topic, :content,NOW(),:writer,:community)")
    result = db.session.execute(sql, {"topic":topic,"content":content,"writer":writer,"community":community})
    db.session.commit()


def find_text(community,id ):
    query = text("SELECT content FROM Blogs WHERE id=:id AND community=:community")
    right_blogs = db.session.execute(query,{"id":id,"community":community})
    blog=right_blogs.fetchone()
    return blog

def find_all_blogs_byname(name,community):
    query = text("SELECT blog_name,id FROM Blogs WHERE Blog_name=:Blog_name AND community=:community")
    right_blogs = db.session.execute(query,{"Blog_name":name, "community":community})
    blogs=right_blogs.fetchall()
    return blogs

def add_comment(id,content):
    query = text(" INSERT INTO Comments (Blog_id,content) VALUES (:id , :content)")
    right_blogs = db.session.execute(query,{"id":id, "content":content})
    db.session.commit()

def find_comments(id):
    query = text(" SELECT content FROM Comments WHERE Blog_id=:id ")
    right_comments = db.session.execute(query,{"id":id})
    comments=right_comments.fetchall()
    return comments

def all_my_blogs(username):
    list=[]
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
        list.append([])
    if len(blogs1)!=0:
        list.append(blogs1)
    if len(blogs2)==0:
        list.append([])
    if len(blogs2)!=0:
        list.append(blogs2)
    if len(blogs3)==0:
        list.append([])
    if len(blogs3)!=0:
        list.append(blogs3)
    if len(blogs4)==0:
        list.append([])
    if len(blogs4)!=0:
        list.append(blogs4)
    return list
def delete_blog(id):
    for i in id:
        query = text(" DELETE FROM Blogs WHERE id=:i ")
        delete = db.session.execute(query,{"i":i})
        db.session.commit()


