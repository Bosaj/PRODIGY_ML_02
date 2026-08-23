# Customer Segmentation — K-Means Clustering

![CI](https://github.com/Bosaj/PRODIGY_ML_02/actions/workflows/ci.yml/badge.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)

Task 02 of the Prodigy InfoTech Machine Learning internship: group retail customers into segments using K-means clustering, based on their purchase history.

## Overview

Using the [Mall Customer Segmentation](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) dataset (200 customers), this project explores age, annual income, and spending score, then applies K-means clustering — selecting the number of clusters via the elbow method — to identify distinct customer segments a retail business can target with different strategies.

## Features

- Exploratory data analysis: distributions, gender breakdown, and pairwise relationships between age, income, and spending score.
- 2D clustering (age vs. spending score, income vs. spending score) and a 3D clustering view (age, income, spending score) visualized with Plotly.
- Elbow-method selection of the optimal number of clusters.
- Final 5-cluster segmentation on annual income vs. spending score, with each segment interpreted for business use (e.g. *high income, high spending* as the priority target segment).

## Tech Stack

Python, pandas, NumPy, scikit-learn, Matplotlib, Seaborn, Plotly.

## Getting Started

### Installation
```bash
pip install -r requirements.txt
```

### Usage
```bash
jupyter notebook Clustering_Algorithm.ipynb
```
The notebook expects `data/Mall_Customers.csv`.

## Testing / CI

[`.github/workflows/ci.yml`](.github/workflows/ci.yml) validates the notebook's structural integrity and installs the full dependency set on every push.

## Project Structure

```
PRODIGY_ML_02/
├── data/
│   └── Mall_Customers.csv
├── Clustering_Algorithm.ipynb
└── requirements.txt
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE).

## Author

Oussama EL HADJI — [github.com/Bosaj](https://github.com/Bosaj)
