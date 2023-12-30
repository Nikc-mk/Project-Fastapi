from fastapi import Depends, FastAPI
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserCreate, UserRead

app = FastAPI(title="Trading App", description="", version="1.0.0")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

# роутер для аутентификации
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
# роутер для регистрации
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


# защищенный вход пользователя
@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.email}"


# не защищеный вход пользователья
@app.get("/unprotected-route")
def unprotected_route():
    return "Hello, anonymous"
