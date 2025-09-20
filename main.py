from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from datetime import timedelta
from typing import List
from pydantic import BaseModel

from database import get_db, SessionLocal, engine
from models import Base, User
from schema import UserResponse, Token, UserRegister, UserLogin, UserRoleUpdate
import auth

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Instancia principal de FastAPI
app = FastAPI(title="API con Autenticación Básica")
security = HTTPBearer()



posts = []

class PostCreate(BaseModel):
    title: str
    content: str

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author: str



@app.post("/register", response_model=UserResponse)
def register_user(user_data: UserRegister, db: Session = Depends(get_db)):
    if auth.get_user_by_username(db, user_data.username):
        raise HTTPException(
            status_code=400,
            detail="Username ya está registrado"
        )

    user = auth.create_user(
        db=db,
        username=user_data.username,
        email=user_data.email,
        password=user_data.password
    )

    return UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        is_active=user.is_active,
        role=user.role  
    )


@app.post("/login", response_model=Token)
def login_user(user_data: UserLogin, db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, user_data.username, user_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o password incorrecto",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=30)
    access_token = auth.create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")


@app.get("/users/me", response_model=UserResponse)
def read_users_me(current_user: User = Depends(auth.get_current_user)):
    return UserResponse(
        id=current_user.id,
        username=current_user.username,
        email=current_user.email,
        is_active=current_user.is_active,
        role=current_user.role
    )



@app.get("/public")
def public_endpoint():
    return {
        "message": "Este endpoint es público",
        "status": "no authentication required"
    }


@app.get("/protected")
def protected_endpoint(current_user: User = Depends(auth.get_current_user)):
    return {
        "message": f"Hola {current_user.username}, tienes acceso!",
        "user_id": current_user.id,
        "status": "authenticated"
    }



@app.post("/posts", response_model=PostResponse)
def create_post(
    post_data: PostCreate,
    current_user: User = Depends(auth.get_current_user)
):
    new_post = {
        "id": len(posts) + 1,
        "title": post_data.title,
        "content": post_data.content,
        "author": current_user.username
    }
    posts.append(new_post)
    return PostResponse(**new_post)


@app.get("/posts", response_model=List[PostResponse])
def get_posts():
    return [PostResponse(**post) for post in posts]


@app.get("/posts/my", response_model=List[PostResponse])
def get_my_posts(current_user: User = Depends(auth.get_current_user)):
    my_posts = [post for post in posts if post["author"] == current_user.username]
    return [PostResponse(**post) for post in my_posts]


@app.delete("/posts/{post_id}")
def delete_post(post_id: int, current_user: User = Depends(auth.get_current_user)):
    post = next((p for p in posts if p["id"] == post_id), None)

    if not post:
        raise HTTPException(status_code=404, detail="Post no encontrado")

    if post["author"] != current_user.username:
        raise HTTPException(status_code=403, detail="No tienes permiso para borrar este post")

    posts.remove(post)
    return {"message": "Post eliminado exitosamente"}



@app.post("/create-admin", response_model=UserResponse)
def create_first_admin(user_data: UserRegister, db: Session = Depends(get_db)):

    existing_admin = db.query(User).filter(User.role == "admin").first()

    if existing_admin:
        raise HTTPException(
            status_code=400,
            detail="Ya existe un administrador en el sistema"
        )

    if auth.get_user_by_username(db, user_data.username):
        raise HTTPException(
            status_code=400,
            detail="Username ya está registrado"
        )

    admin_user = auth.create_admin_user(
        db=db,
        username=user_data.username,
        email=user_data.email,
        password=user_data.password
    )

    return UserResponse(
        id=admin_user.id,
        username=admin_user.username,
        email=admin_user.email,
        is_active=admin_user.is_active,
        role=admin_user.role
    )


@app.get("/admin/users", response_model=List[UserResponse])
def list_all_users(
    admin_user: User = Depends(auth.require_admin),
    db: Session = Depends(get_db)
):
    users = auth.get_all_users(db)

    return [UserResponse(
        id=user.id,
        username=user.username,
        email=user.email,
        is_active=user.is_active,
        role=user.role
    ) for user in users]


@app.put("/admin/users/{user_id}/role", response_model=UserResponse)
def update_user_role(
    user_id: int,
    role_data: UserRoleUpdate,
    admin_user: User = Depends(auth.require_admin),
    db: Session = Depends(get_db)
):
    if user_id == admin_user.id:
        raise HTTPException(
            status_code=400,
            detail="No puedes cambiar tu propio rol"
        )

    updated_user = auth.update_user_role(db, user_id, role_data.role)

    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return UserResponse(
        id=updated_user.id,
        username=updated_user.username,
        email=updated_user.email,
        is_active=updated_user.is_active,
        role=updated_user.role
    )
