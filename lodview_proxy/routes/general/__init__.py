from fastapi import FastAPI, APIRouter

router = APIRouter()


@router.get('/', include_in_schema=False)
def root():
    """Redirect root route to /docs."""
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url='/docs')
