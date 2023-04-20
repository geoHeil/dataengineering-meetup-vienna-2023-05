from ml_project import defs
from utils import helper

def test_ml_project_loads():
    implied_repo = defs.get_repository_def()
    implied_repo.load_all_definitions()

def test_helper_function():
    helper()