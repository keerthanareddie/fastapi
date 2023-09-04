from .. import models, schemas, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional
from sqlalchemy import func


router = APIRouter(
    prefix="/posts"
)







@router.get("/", response_model=List[schemas.Postvote])
def get_posts(db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user), Limit: int = 10, skip: int =0, search: Optional[str] = ""):
    # cursor.execute("""SELECT * FROM post""")
    # data = cursor.fetchall()
    # data = db.query(models.Post).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()
    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()  
    print(data)
    #return data
    return results
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(postdata: schemas.PostCreate, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # print(postdata)
    # keer = postdata.dict()
    # keer['id'] = randrange(0, 1000000)
    # postlist.append(keer)
    #return{"new_post": f"title is {payload['title']} content: {payload['content']}"}
    # cursor.execute("""INSERT INTO POST (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
    # (postdata.title,postdata.content,postdata.published))
    # keer = cursor.fetchone()
    # conn.commit()
    #print(**postdata.dict())
    # keer = models.Post(**postdata.dict())
    # db.add(keer)
    # db.commit()
    # db.refresh(keer)
    #keer = models.Post(title=postdata.title, content= postdata.content, published=postdata.published)
    print(current_user.email)
    keer = models.Post(owner_id=current_user.id, **postdata.dict())
    db.add(keer)
    db.commit()
    db.refresh(keer)
    return  keer

@router.get("/{id}", response_model=schemas.Postvote)
def get_post_id(id: int, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # print(type(id))
    # cursor.execute(""" SELECT * FROM POST WHERE id = %s """, (str(id)))
    # data = cursor.fetchone()
    # data = db.query(models.Post).filter(models.Post.id == id).first()
    data = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    #data = find_post(id)
    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
        detail=f"post with {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"post with {id} was not found"}
    # if data.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized to perform this action")
   
    
    # print(data)
    # print(type(data))
    return  data

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" DELETE FROM POST WHERE id = %s RETURNING * """, (str(id)))
    # data = cursor.fetchone()
    # conn.commit()
    # data = find_index(id)
    data = db.query(models.Post).filter(models.Post.id == id)
    keerreddy = data.first()
    if data.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with {id} doesnt exist")
    
    # if keerreddy.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized to perform this action")
   
    data.delete(synchronize_session=False)
    db.commit()
    #postlist.pop(data)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user : int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" UPDATE POST SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content,post.published, str(id)))
    # data = cursor.fetchone()
    # conn.commit()
    #data = find_index(id)
    data = db.query(models.Post).filter(models.Post.id == id)
    keer = data.first()
    if keer == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with {id} doesnt exist")
    # if keer.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="not authorized to perform this action")
    data.update(post.dict(), synchronize_session=False)
    db.commit()
    # post_dict = post.dict()
    # print(post_dict)
    # post_dict['id'] =id
    # print(id)
    # postlist[data] = post_dict
    return data.first()

