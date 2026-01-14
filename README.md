# Gold Price Prediction with Flask Deployment

This project predicts the **GLD (Gold ETF) price** using a Linear Regression model
trained on historical market data.

## Dataset
- Source: Kaggle
- Features used:
  - SPX (S&P 500 Index)
  - USO (Oil Price)
  - SLV (Silver Price)
  - EUR/USD (Exchange Rate)

## Model
- Algorithm: Linear Regression
- Evaluation Metric: R² Score
- Target Variable: GLD

## Deployment
- Model serialized using Pickle
- Deployed as a REST API using Flask
- API endpoint: `/predict`

### Sample API Request
```json
{
  "SPX": 4500,
  "USO": 70,
  "SLV": 22,
  "EURUSD": 1.10
}
