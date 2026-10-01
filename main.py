from fastapi import FastAPI , Depends , HTTPException , Query
from database import engine , SessionLocal
import models , schemas
from sqlalchemy.orm import Session 
from auth import create_token , verify_token



models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()




#home
app = FastAPI()
@app.get("/")
def get_home():
    return {
        "message" : "blog api started"
    }

#login API 
@app.post("/login")
def get_login():
    return {
        "access_token" : create_token({"user" : "admin"}),
        "token_type" : "bearer"

    }







#create blog(protected)
@app.post("/blog", response_model=schemas.BlogResponse )
def create_blog(blog: schemas.BlogCreate , db: Session = Depends(get_db),user= Depends(verify_token)):
    new_blog = models.Blog(
        title = blog.title,
        content = blog.content
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@app.get("/blogs")
def get_blogs(
        page: int = 1,
        limit : int = 5,
        search: str = Query(default=""),
        db : Session = Depends(get_db)
    ):

    
    query = db.query(models.Blog)

    if search :
        query = query.filter(
            models.Blog.title.ilike(f"%{search}%")
        )

    total = query.count()
    start = (page -1) * limit 
    blogs = query.offset(start).limit(limit).all()

    return {
        "page" : page,
        "limit" : limit,
        "total" : total,
        "data" : blogs

     }




#find one blogs(protected)
@app.get("/blogs/{id}" , response_model=schemas.BlogResponse )
def get_one(id: int ,db:Session = Depends(get_db) , user = Depends(verify_token)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog :
        raise HTTPException(
            status_code=404,
            detail="blog not found"
        )

    return blog

#update blogs
@app.put("/blogs/{id}", response_model=schemas.BlogResponse)
def update_blog(id: int , blog: schemas.BlogCreate , db: Session = Depends(get_db)):
    new_blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not new_blog :
        raise HTTPException(
            status_code=404,
            detail="queary not upgraded"
        )

    new_blog.title = blog.title 
    new_blog.content = blog.content

    db.commit()

    return new_blog


#delete blogs
@app.delete("/blogs/{id}")
def get_delete(id : int , db : Session = Depends(get_db)):
    deletes = db.query(models.Blog).filter (models.Blog.id == id).first()

    if not deletes : 
        raise HTTPException(
            status_code=404,
            detail="error not found"
        )

    db.delete(deletes)
    db.commit()

    return {
        "message" : "Blog deleted sucessfully"
    }



