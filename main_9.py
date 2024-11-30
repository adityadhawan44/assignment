import pandas as pd

# Function to load and display basic information about the dataset
def load_data(file_name):
    try:
        # Load the dataset from CSV
        df = pd.read_csv(file_name)
        print(f"Data loaded successfully from {file_name}.")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
        return None

# Function to perform initial exploration of the data
def data_overview(df):
    print("\n--- Data Overview ---")
    # Display basic information about the dataset
    print(f"Shape of the data (Rows, Columns): {df.shape}")
    print(f"Columns in the data: {df.columns}")
    print(f"Data types of columns: {df.dtypes}")
    print(f"Missing values per column:\n{df.isnull().sum()}")
    print(f"First 5 rows of the dataset:\n{df.head()}")
    
# Function to generate summary statistics for the data
def data_statistics(df):
    print("\n--- Summary Statistics ---")
    # Display summary statistics for numerical columns
    print(f"Summary statistics for numerical columns:\n{df.describe()}")
    
    # Display unique counts for categorical columns
    print("\nUnique values in categorical columns:")
    for col in df.select_dtypes(include='object').columns:
        print(f"{col}: {df[col].nunique()} unique values")
        print(df[col].value_counts())

# Function to handle missing values
def handle_missing_values(df):
    print("\n--- Handling Missing Values ---")
    
    # Separate numeric and non-numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    non_numeric_cols = df.select_dtypes(include=['object']).columns
    
    # Fill missing values for numeric columns with the mean
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    # Fill missing values for non-numeric columns with the mode (most frequent value)
    for col in non_numeric_cols:
        df[col] = df[col].fillna(df[col].mode()[0])
    
    print(f"Missing values after filling:\n{df.isnull().sum()}")
    
    return df

# Function to find correlations among numeric columns
def find_correlations(df):
    print("\n--- Correlations Among Numeric Columns ---")
    numeric_cols = df.select_dtypes(include=['int64', 'float64'])
    correlation_matrix = numeric_cols.corr()
    print(f"Correlation matrix:\n{correlation_matrix}")

# Main function to tie everything together
def main():
    # Input dataset filename (adjust this to your file path)
    file_name = input("Enter the CSV file name (with extension): ")
    
    # Load the data
    df = load_data(file_name)
    if df is None:
        return
    
    # Data Overview
    data_overview(df)
    
    # Summary Statistics
    data_statistics(df)
    
    # Handle Missing Values
    df_filled = handle_missing_values(df)
    
    # Find Correlations
    find_correlations(df_filled)

if __name__ == "__main__":
    main()
