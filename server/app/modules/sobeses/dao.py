# from typing import List
from app.dao.base import BaseDAO

from .models import SobesModel

class SobesDAO(BaseDAO):
    model = SobesModel
