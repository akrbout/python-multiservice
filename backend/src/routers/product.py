from fastapi import APIRouter
from fastapi import Depends

from src.api_models import service
from src.storage.models import Product

router = APIRouter(prefix="/product")
