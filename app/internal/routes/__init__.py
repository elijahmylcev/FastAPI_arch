import os
from app.helpers import combine_modules_in_all
from fastapi import APIRouter

current_package = os.path.dirname(__file__)
module_files = [f[:-3] for f in os.listdir(current_package) if f.endswith('.py') and f != '__init__.py']

__all__ = combine_modules_in_all(__name__, module_files, APIRouter)
