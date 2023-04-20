from dagster import load_assets_from_package_module, repository, define_asset_job, ScheduleDefinition

from analytics_project import assets

update_penguins = define_asset_job("update_penguins", selection = "penguins")
update_penguins_alot = ScheduleDefinition("penguin_update_minutely", cron_schedule= "* * * * *", job = update_penguins)

@repository
def analytics_project():
    return [load_assets_from_package_module(assets), [update_penguins_alot]]
