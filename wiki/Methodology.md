# Methodology

## Dataset

The [Mall Customer Segmentation](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) dataset covers 200 mall customers with `Age`, `Annual Income (k$)`, `Spending Score (1-100)`, and `Gender`.

## Exploratory analysis

The notebook examines the distribution of each numeric attribute, the gender breakdown, and pairwise relationships between age, income, and spending score before clustering.

## Clustering approach

1. **Elbow method**: for each candidate feature pairing, K-means is run across a range of cluster counts and the inertia (sum of squared distances between points and their assigned centroid) is plotted to identify the "elbow" — the point of diminishing returns from adding more clusters.
2. **2D views**: separate K-means runs on (age, spending score) and (income, spending score) pairs, each visualized with `matplotlib`/`seaborn` scatter plots colored by cluster and marked centroids.
3. **3D view**: a combined (age, income, spending score) clustering visualized interactively with Plotly.
4. **Final model**: K-means with **k = 5** on annual income vs. spending score, chosen as the most business-interpretable segmentation.

## Resulting segments

| Segment | Profile |
|---|---|
| Cluster 1 | High income, low spending |
| Cluster 2 | Average income, average spending |
| Cluster 3 | High income, high spending — **priority target segment** |
| Cluster 4 | Low income, high spending |
| Cluster 5 | Low income, low spending |

This income-vs-spending framing is the standard interpretation used in retail segmentation exercises on this dataset: Cluster 3 (high income, high spending) is the most attractive segment for premium offers, while Cluster 4 (low income, high spending) represents customers a business might want to understand — or upsell carefully — given their spending outpaces their income bracket.
