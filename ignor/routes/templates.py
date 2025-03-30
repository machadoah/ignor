import os

from fastapi import APIRouter

from ignor.schemas import Template, Templates
from ignor.settings import Settings

router = APIRouter(
    prefix='/api/templates',
    tags=['templates'],
)


@router.get('/list', response_model=Templates)
def list_templates():
    """
    List all templates
    """

    templates = [file for file in os.listdir(Settings().TEMPLATES_PATH)]

    return {'templates': templates}


@router.get('/verify/{template_name}', response_model=Templates)
def verify_template(template_name: str) -> Templates:
    """
    Verify if a template exists

    Verifica se um template existe, retornando somente o nome do template

    exemplo: /api/templates/verify/script

    tera o retorno:

    {
        "templates": ["JavaScript", "TypeScript", "CljoreScript"]
    }

    retornando templates que possuem que possuem em seu nome o script
    """

    templates = [
        file
        for file in os.listdir(Settings().TEMPLATES_PATH)
        if template_name.lower() in file.lower()
    ]

    return {'templates': templates}
