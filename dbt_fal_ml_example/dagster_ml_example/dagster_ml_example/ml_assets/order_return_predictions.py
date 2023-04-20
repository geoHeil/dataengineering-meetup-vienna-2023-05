from dagster import asset, AssetIn
import pandas as pd

@asset(
        io_manager_key="io_manager",
        compute_kind="pandas",
        ins={'loaded_model':AssetIn(['order_return_prediction_model']),
             'orders_new_df':AssetIn(['ml', 'customer_orders'])}
)
def order_return_predictioons(context, loaded_model, orders_new_df:pd.DataFrame):
    "predicts if a customer will return an order"
    #dbt.config(materialized="table")
    #models_df = dbt.ref("order_return_prediction_models")
    #best_model_name = models_df[models_df.accuracy == models_df.accuracy.max()].model_name[0]
    #with open(f"ml_models/{best_model_name}.pkl", "rb") as f:
    #    loaded_model = pickle.load(f)
    #orders_new_df = dbt.ref("customer_orders")
    predictions = loaded_model.predict(orders_new_df[["age", "total_price"]])
    orders_new_df["predicted_return"] = predictions
    return orders_new_df
