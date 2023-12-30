from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from src.auth.base_config import auth_backend
from src.auth.manager import get_user_manager
from src.auth.models import User
from src.auth.schemas import UserCreate, UserRead
from src.operations.router import router as router_operation

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

app.include_router(router_operation)
