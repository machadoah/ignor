import os

from fastapi import APIRouter

from ignor.schemas import Templates
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
    """

    templates = [
        file
        for file in os.listdir(Settings().TEMPLATES_PATH)
        if template_name.lower() in file.lower()
    ]

    return {'templates': templates}


@router.get('/verify/initial/{template_name}', response_model=Templates)
def verify_template_initial(template_name: str) -> Templates:
    """
    Verify if a template exists
    """

    templates = [
        file
        for file in os.listdir(Settings().TEMPLATES_PATH)
        if file.lower().startswith(template_name.lower())
    ]

    return {'templates': templates}
