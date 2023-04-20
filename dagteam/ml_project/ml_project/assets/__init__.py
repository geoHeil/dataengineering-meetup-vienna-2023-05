from dagster import asset, SourceAsset, AssetKey
from sklearn.cluster import KMeans

# use an asset from the analytics project
penguins = SourceAsset(key = AssetKey("penguins"))

@asset(
    group_name = "ml",
    compute_kind = "sklearn"
)
def penguin_cluster(penguins):
    predictors = penguins.drop(columns=['species', 'island', 'year', 'sex']).dropna()
    model = KMeans(n_clusters = 3).fit(predictors)
    predictors['cluster'] = model.labels_
    return predictors
