# coding: utf-8


from fastapi import FastAPI

from app.routes import rpn_router

app = FastAPI()
app.include_router(rpn_router, prefix='/api/v1/rpn')