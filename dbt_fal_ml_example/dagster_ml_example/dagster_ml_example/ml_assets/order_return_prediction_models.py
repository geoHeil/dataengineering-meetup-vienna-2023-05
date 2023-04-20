from dagster import AssetIn, asset,  MonthlyPartitionsDefinition, Output, Field, Int

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import pandas as pd
import uuid
import datetime

@asset(
        compute_kind="scikitlearn",
        io_manager_key="model_io_manager",
        ins={'orders_df':AssetIn(['ml','customer_orders_labeled'])}
)
def order_return_prediction_model(context, orders_df:pd.DataFrame):
    "model to predict if a customer will return an order"
    X = orders_df[['age', 'total_price']]
    y = orders_df['return']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

    context.log.debug("Model init")
    lr_model = LogisticRegression(random_state=123)

    context.log.debug("Model fitting")
    lr_model.fit(X_train, y_train)

    # Test model
    y_pred = lr_model.predict(X_test)

    context.log.debug("Preparing the classification report")
    # Create a report and put it in a DataFrame
    model_name = str(uuid.uuid4())
    y_test = y_test.astype(float)
    report = classification_report(y_test, y_pred, output_dict=True)
    context.log.info(f"Classification report for {model_name}: {report}")
    #report["model_name"] = model_name
    #report["date"] = datetime.datetime.now()
    #output_df = pd.DataFrame([report])
    #output_df = output_df.rename(columns={"0.0": "target_0", "1.0": "target_1"})
    #output_df.set_index("model_name")
    return lr_model
