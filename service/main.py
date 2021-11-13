from fastapi import FastAPI
from service.api.api import router as api_router
import os

os.environ["encryption_key"] = "@NcRfUjXnZr4u7x!A%D*G-KaPdSgVkYp"
os.environ["encryption_iv"] = "pIbTlr3fyPHnxosRA3Ethg=="


app = FastAPI(
    title="encrypt-fastapi",
)

app.include_router(api_router)


@app.get("/ping", summary="Check that the service is operational")
def pong():
    """
    Sanity check - this will let the user know that the service is operational.

    It is also used as part of the HEALTHCHECK. Docker uses curl to check that the API service is still running, by exercising this endpoint.

    """
    return {"ping": "pong!"}
