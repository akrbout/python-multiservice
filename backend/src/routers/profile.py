from fastapi import APIRouter
from fastapi import Depends

from src.service.auth import current_active_user
from src.service.profile import ProfileService
from src.storage.models import User
from src.storage import engine

router = APIRouter(prefix="/profile")


@router.get("/avatar")
async def generate_avatar(
    user: User = Depends(current_active_user),
    db_session: engine.AsyncSession = Depends(engine.get_async_session),
):
    profile_service = ProfileService(user, db_session)
    updated_user = await profile_service.generate_profile_avatar()
    return updated_user
