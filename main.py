from fastapi import FastAPI , Depends , HTTPException , Query
from sqlalchemy.orm import Session
from database import engine , sessionLocal
import models , schemas
from auth import create_token , verify_token 


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = sessionLocal()
    try:
        yield db 
    finally :
        db.close()



@app.get("/home")
def get_api():
    return {
        "message" : "blog api  started"
    }

@app.post("/login")
def login_api():
    return {
        "access_token" : create_token({"user" : 'bitun'}),
        "token_type" :"bearer"
    }

@app.post("/blogs" , response_model=schemas.BlogResponse)

def create_blog(blog: schemas.BlogCreate , db: Session = Depends(get_db) , user = Depends(verify_token)):

    new_blog = models.Blog(title=blog.title , content = blog.content)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

@app.get("/blogs")
def get_blogs(
    page : int = 1,
    limit : int = 5,
    search : str = Query(default=""),
    db: Session = Depends (get_db)
):
    
    query = db.query(models.Blog)

    if search : 
        query = query.filter(
            models.Blog.title.ilike(f"%{search}%")
        )


    total = query.count()
    start = (page - 1) * limit
    blogs = query.offset(start).limit(limit).all()

    return {
        "page" : page,  
        "limit" : limit,
        "total" : total,
        "data" : blogs
    }
        

@app.get("/blogs/{id}" , response_model=schemas.BlogResponse)
def get_blogs(id: int , db: Session = Depends(get_db) , user = Depends(verify_token)):
    one_get = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not one_get :
        raise HTTPException(
            status_code=404,
            detail="blog not found"

         )


    return one_get

@app.put("/updte/{id}" , response_model=schemas.BlogResponse)
def update_blogs(id : int , Blog : schemas.BlogCreate , db : Session = Depends(get_db)):
    update_blogs = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not update_blogs:
        raise HTTPException(
            status_code=404,
            detail="blog not found"
        )
    update_blogs.title = Blog.title
    update_blogs.content = Blog.content

    db.commit()
    db.refresh(update_blogs)



    return update_blogs

@app.delete("/blogs/{id}")
def delete_blogs(id : int , db: Session = Depends(get_db)):
    delete_blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not delete_blog:
        raise HTTPException(
            status_code=404,
            detail="blog not found"
        )
    db.delete(delete_blog)
    db.commit()

    return {
        "message" : "blog deleted sucessfully"
    }


