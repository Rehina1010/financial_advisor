
# Financial Advisor

**Financial Advisor** is a Python-based project designed to assist with financial data analysis and provide investment insights. Using Data Science and Data Analytics techniques, this tool loads, processes, and visualizes stock data, making it easier to analyze trends and receive investment recommendations.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies and Libraries](#technologies-and-libraries)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Financial Advisor project provides tools for working with stock data from the S&P 500, allowing for analysis and visualization of stock price trends, as well as generating investment recommendations based on market capitalization thresholds.

This project is well-suited for anyone interested in learning financial data analysis, Python programming, and data visualization.

## Features

- **Data Loading and Processing**: Loads and preprocesses financial data from CSV files.
- **Stock Trend Visualization**: Plots historical price trends of specific stocks.
- **Investment Recommendations**: Generates recommendations for stocks based on market capitalization.
- **Jupyter Notebook for EDA**: Includes a Jupyter notebook for data exploration and experimentation.

## Technologies and Libraries

The project relies on the following libraries and tools:

- **Pandas**: For data loading, cleaning, and manipulation.
- **Matplotlib** and **Seaborn**: For data visualization, including price trend plotting and correlation analysis.
- **NumPy**: Assists with numerical data manipulation.
- **Poetry**: Manages dependencies and virtual environments.

## Project Structure

The project is organized as follows:

```plaintext
financial_advisor/
│
├── data/                     # Directory for storing transaction and market data
│   ├── sp500_companies.csv   # Sample data file for S&P 500 companies
│   ├── sp500_index.csv       # S&P 500 index data
│   └── sp500_stocks.csv      # Stock data for individual companies
│
├── notebooks/                # Jupyter notebooks for data exploration
│   └── EDA.ipynb             # Notebook for Exploratory Data Analysis (EDA)
│
├── src/                      # Source code for the project
│   ├── data_processing.py    # Module for loading and processing data
│   ├── visualization.py      # Module for data visualization
│   └── recommendations.py    # Module for generating investment recommendations
│
├── main.py                   # Main script to run the analysis and generate recommendations
└── README.md                 # Project documentation
```

## Installation and Setup

This project requires **Poetry** for dependency management. If Poetry is not already installed, you can find installation instructions on [Poetry's official website](https://python-poetry.org/).

### Steps to Set Up

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/financial_advisor.git
   cd financial_advisor
   ```

2. **Install dependencies** with Poetry:

   ```bash
   poetry install
   ```

3. **Activate the virtual environment**:

   ```bash
   poetry shell
   ```

4. **Run the main script**:

   ```bash
   python main.py
   ```

This will run the data processing, visualization, and recommendation functions, displaying a price trend plot and printed recommendations in the console.

## Usage

Once you have set up and activated the environment, you can run the project as follows:

1. **Load Data**: The `main.py` script calls the `load_data()` function to read in data on S&P 500 companies, stock index values, and stock prices.
2. **Visualize Trends**: The `plot_price_trend()` function in `visualization.py` generates a plot of a stock's historical prices. For example, the script plots Apple's stock trend.
3. **Generate Recommendations**: The `investment_recommendation()` function in `recommendations.py` identifies companies with market capitalizations exceeding a certain threshold, recommending them for investment.

### Sample Output

After running the `main.py` script, the program will display a price trend plot and print investment recommendations similar to:

```plaintext
Consider investing in Apple Inc. - Technology sector.
Consider investing in Microsoft Corporation - Technology sector.
Consider investing in Amazon.com, Inc. - Consumer Cyclical sector.
...
```

## Exploratory Data Analysis (EDA)

The `EDA.ipynb` notebook in the `notebooks` directory is designed for exploring and understanding the data before building visualizations and recommendations. The notebook includes:

- **Data Cleaning**: Handling missing or inconsistent values.
- **Correlation Analysis**: Checking relationships between different financial indicators.
- **Preliminary Visualizations**: Plotting initial trends and distributions.

To use the notebook:

1. Start Jupyter Notebook in the project directory:

   ```bash
   jupyter notebook notebooks/EDA.ipynb
   ```

2. Open `EDA.ipynb` and run the cells to explore the data.

## Contributing

Contributions are welcome! If you would like to improve this project, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch** for your feature or bugfix.
3. **Make your changes** and ensure that they work as expected.
4. **Submit a pull request** to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Financial Advisor** uses Data Science and Data Analytics to make financial data accessible and actionable, helping users make informed investment decisions.
