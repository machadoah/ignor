from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Templates(BaseModel):
    templates: list[str]


class Template(BaseModel):
    template: str
