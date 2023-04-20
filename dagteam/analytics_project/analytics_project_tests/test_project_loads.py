from analytics_project import analytics_project

def test_analytics_project_loads():
    # will raise errors if the project can't load
    # similar to loading a failing project in dagit
    analytics_project.load_all_definitions()
