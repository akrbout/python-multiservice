from src.settings import avatar_generator_settings
from aiohttp import ClientSession
from src.storage.models import User
from src.storage.crud import BaseCrud, AsyncSession


class ProfileService:
    _avatar_service_api: str
    _user: User
    _crud: BaseCrud

    def __init__(self, user: User, db_session: AsyncSession):
        """
        Profile Service class

        :param session: Aiohttp ClientSession obj
        """
        self._avatar_service_api = f"{avatar_generator_settings.service_address}/avatar"
        self._user = user
        self._crud = BaseCrud(db_session)

    async def update_profile(self) -> None:
        await self._crud.update(new_obj=self._user)

    async def generate_profile_avatar(self) -> User:
        req_data = {"nickname": self._user.username, "image_upscale_size": avatar_generator_settings.image_size}
        async with ClientSession() as session:
            async with session.post(self._avatar_service_api, json=req_data) as response:
                if response.status != 200:
                    return None
                avatar_base64 = await response.json()
                new_avatar = avatar_base64["image_base64"]
            self._user.photo_base64 = new_avatar
            await self.update_profile()
            return self._user

    async def change_profile_info(self):
        pass
