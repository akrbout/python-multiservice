import random

from fastapi.middleware.cors import CORSMiddleware
from api_models.product import Product

from fastapi import FastAPI, status
from src.routers import auth
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer

from src.storage import engine
from src.storage.crud import BaseCrud
from src.storage.models import User
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI(
    title="Reimport Ecom Service",
    description="Сервис продажи товаров параллельного импорта",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

images = [
    "https://ir.ozone.ru/s3/multimedia-s/wc1000/6858236152.jpg",
    "https://ir.ozone.ru/s3/multimedia-l/wc1000/6847227201.jpg",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
    "https://avatars.mds.yandex.net/get-mpic/4937511/img_id4034618204228796059.jpeg/600x800",
]


@app.on_event("startup")
async def startup():
    await engine.create_db()


# SERVICE AUTH ROUTERS
app.include_router(auth.router)


@app.get("/", include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url="/docs")


@app.get("/healthz", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, int]:
    return {"status": status.HTTP_200_OK}


@app.get("/test_crud")
async def test_crud(session: AsyncSession = Depends(engine.get_async_session)):
    crud = BaseCrud(session)
    users = await crud.get_all(User)
    users = [user._data for user in users]
    return users


@app.get("/products")
def get_products():
    res = []
    for num, image in enumerate(images):
        res.append(
            Product(
                id=num,
                name=image.split("/")[3],
                price=random.randint(300, 1200),
                imageUrl=image,
                description="TESTTESTTESTTEST",
            )
        )
    return {"products": res}


@app.get("/product/1")
def get_product():
    return Product(
        id=1,
        name=images[1].split("/")[3],
        price=random.randint(300, 1200),
        imageUrl=images[1],
        description="TESTTESTTESTTEST",
    )
