# FAQ

**Why 5 clusters and not some other number?**
The elbow method plot (inertia vs. number of clusters) flattens out around k=5 for the income/spending pairing, and five segments also produce the cleanest business story (see [Methodology](Methodology)).

**Why cluster on income vs. spending score for the final model, instead of age?**
Income and spending score together produce visually and commercially distinct groups (e.g. "high income, high spending"), which is more directly actionable for a retail business than age-based clusters.

**Is K-means the right algorithm here?**
For roughly spherical, similarly-sized clusters like these — which is what this dataset produces — K-means is a reasonable and standard choice. It wouldn't be ideal for irregularly shaped or highly imbalanced clusters, but that's not the case here.

**What does "Spending Score" actually mean?**
It's a score from 1–100 assigned by the mall based on customer behavior and purchasing data, as defined by the dataset's creators — not a raw currency amount.

**Does the notebook use the gender column in clustering?**
It's explored during EDA (gender breakdown) but the final clustering models use only the numeric attributes (age, income, spending score).

**Does CI verify the cluster assignments or the elbow plot?**
No — CI only checks notebook structure and dependency installability. It doesn't execute the clustering cells.
