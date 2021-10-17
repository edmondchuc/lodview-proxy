from fastapi import APIRouter

from lodview_proxy.routes.api_v1 import endpoints

router = APIRouter()
router.include_router(endpoints.lodview.router)
