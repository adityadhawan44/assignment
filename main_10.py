import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_data(filename):
    try:
        df = pd.read_csv(filename)
        print("Data loaded successfully.\n")
        return df
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

# Perform basic data exploration
def basic_exploration(df):
    print("\nBasic Data Exploration:")
    print(f"First 5 rows of the dataset:\n{df.head()}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nSummary Statistics:\n{df.describe()}")
    print(f"\nMissing Values:\n{df.isnull().sum()}")

# Visualize the distribution of sales
def sales_distribution(df):
    print("\nVisualizing Sales Distribution:")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Sales'], kde=True, bins=30)
    plt.title('Sales Distribution')
    plt.xlabel('Sales')
    plt.ylabel('Frequency')
    plt.show()

# Visualize the sales trend over time
def sales_trend(df):
    print("\nVisualizing Sales Trend Over Time:")
    df['OrderDate'] = pd.to_datetime(df['OrderDate'])  # Ensure the 'OrderDate' is in datetime format
    df.set_index('OrderDate', inplace=True)
    
    plt.figure(figsize=(10, 6))
    df['Sales'].resample('M').sum().plot()
    plt.title('Monthly Sales Trend')
    plt.xlabel('Date')
    plt.ylabel('Total Sales')
    plt.show()

# Check for relationships between variables
def sales_by_region(df):
    print("\nSales by Region:")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Region', y='Sales', data=df)
    plt.title('Sales Distribution by Region')
    plt.show()

# Function to generate the correlation heatmap
def correlation_heatmap(df):
    # Select only numeric columns for correlation
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    
    # Calculate the correlation matrix
    correlation_matrix = numeric_df.corr()

    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()
    
# Main function to execute the EDA
def main():
    filename = input("Enter the sales dataset CSV file name (with extension): ")
    
    # Load the data
    df = load_data(filename)
    
    if df is not None:
        # Basic Exploration of Data
        basic_exploration(df)
        
        # Visualize Sales Distribution
        sales_distribution(df)
        
        # Visualize Sales Trend Over Time
        sales_trend(df)
        
        # Sales by Region
        sales_by_region(df)
        
        # Correlation Heatmap for numeric features
        correlation_heatmap(df)

if __name__ == "__main__":
    main()
