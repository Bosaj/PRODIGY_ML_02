from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans

DATA_DIR = Path(__file__).parent / "data"
N_CLUSTERS = 5


@st.cache_resource
def fit_model():
    df = pd.read_csv(DATA_DIR / "Mall_Customers.csv")
    X = df[["Annual Income (k$)", "Spending Score (1-100)"]].values
    model = KMeans(n_clusters=N_CLUSTERS, init="k-means++", random_state=0)
    labels = model.fit_predict(X)
    df["Cluster"] = labels
    return model, df


def describe_cluster(center):
    income, spending = center
    income_level = "high" if income > 60 else "low" if income < 40 else "moderate"
    spending_level = "high" if spending > 60 else "low" if spending < 40 else "moderate"
    return f"{income_level} income, {spending_level} spending"


st.title("Retail Customer Segmentation")
st.caption(
    "K-means clustering trained live (on app start) on the Mall Customer "
    "dataset, exactly as in the original notebook. Prodigy InfoTech ML "
    "internship, Task 02."
)

model, df = fit_model()

st.subheader("Explore the segments")
fig, ax = plt.subplots(figsize=(8, 6))
colors = plt.cm.tab10.colors
for c in range(N_CLUSTERS):
    subset = df[df["Cluster"] == c]
    ax.scatter(
        subset["Annual Income (k$)"], subset["Spending Score (1-100)"],
        label=f"Cluster {c}", s=60, alpha=0.7, color=colors[c],
    )
ax.scatter(
    model.cluster_centers_[:, 0], model.cluster_centers_[:, 1],
    s=250, c="black", marker="X", label="Centroids",
)
ax.set_xlabel("Annual Income (k$)")
ax.set_ylabel("Spending Score (1-100)")
ax.legend()
st.pyplot(fig)

st.subheader("Classify a new customer")
income = st.number_input("Annual income (k$)", min_value=0, max_value=200, value=60)
spending = st.number_input("Spending score (1-100)", min_value=1, max_value=100, value=50)

if st.button("Assign segment"):
    cluster = model.predict([[income, spending]])[0]
    center = model.cluster_centers_[cluster]
    st.success(f"Assigned to Cluster {cluster} ({describe_cluster(center)})")

with st.expander("Cluster profiles (centroids)"):
    profile_df = pd.DataFrame(
        model.cluster_centers_, columns=["Annual Income (k$)", "Spending Score (1-100)"]
    )
    profile_df["Profile"] = profile_df.apply(
        lambda r: describe_cluster((r["Annual Income (k$)"], r["Spending Score (1-100)"])), axis=1
    )
    st.dataframe(profile_df)
