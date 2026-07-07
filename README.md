#  AI Car Valuation Engine (Gradient Boosting Regression)

Welcome! This is an intelligent car valuation system that predicts the market price of a vehicle in real-time based on its mechanical specifications, engine capabilities, and safety features. The core machine learning model was trained in **Google Colab** and deployed as an interactive dashboard using **Streamlit**.

 **Try the live web app here!** -> [👉 Link to my Car Valuation App 👈](AQUÍ_PEGARÁS_TU_LINK_DE_STREAMLIT)

---

##  Project Architecture & ML Core

Unlike simple linear models, this project utilizes **Gradient Boosting Regression**, a powerful ensemble learning method that builds trees sequentially to minimize prediction errors.

###  Model Specifications
* **Algorithm:** `GradientBoostingRegressor` (Scikit-Learn).
* **Hyperparameter Optimization:** Fine-tuned with `n_estimators=150`, `learning_rate=0.05`, and `max_depth=3` to maximize accuracy on diverse powertrains (Gasoline, Diesel, Hybrid, and Electric vehicles).
* **Features Analyzed:** Brand (Manufacturer), Body Category, Airbags configuration, Cylinder count, Engine displacement (Liters), Horsepower (HP), Max RPM, Fuel efficiency (City MPG), and Passenger capacity.
* **Evaluation Metrics:** Achieved a Mean Absolute Error (MAE) of **~5,058 €**, proving solid capabilities in handling non-linear pricing data across multiple car segments.

---

##  Repository Structure

* `app.py`: Main interactive web application script built with Streamlit.
* `modelo_precio_coches_regresion.joblib`: The pre-trained, optimized Gradient Boosting production-ready model binary.
* `requirements.txt`: Configuration file tracking required production dependencies (`streamlit`, `scikit-learn`, `pandas`, `numpy`, `joblib`).

---

##  Local Installation and Usage

To replicate and run this regression engine locally, open your terminal and follow these steps:

1. **Clone the repository or download the source files.**
2. **Install the required dependencies:**
   ```bash
   python -m pip install -r requirements.txt
