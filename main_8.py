import pandas as pd

# Function to load the dataset
def load_data(filename):
    try:
        df = pd.read_csv(filename)
        print("Data loaded successfully.\n")
        return df
    except FileNotFoundError:
        print("File not found.")
        return None

# Function to handle missing values by filling them with the mean of numeric columns only
def handle_missing_values(df):
    print("\nHandling Missing Values:")
    # Select only numerical columns for filling missing values
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())  # Fill missing values with the mean for numerical columns
    print("Missing values handled.\n")
    return df

# Function to remove duplicate rows
def remove_duplicates(df):
    print("\nRemoving Duplicates:")
    df = df.drop_duplicates()  # Remove duplicate rows
    print(f"Duplicates removed. Remaining rows: {len(df)}\n")
    return df

# Function to scale data manually (Standardization)
def scale_data(df):
    print("\nScaling Data:")
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numerical_cols:
        mean = df[col].mean()
        std = df[col].std()
        df[col] = (df[col] - mean) / std  # Standardization: (value - mean) / std
    print("Data scaled.\n")
    return df

# Main function to run the script
def main():
    filename = input("Enter the CSV file name (with extension): ")
    
    # Load the data
    df = load_data(filename)
    
    if df is not None:
        # Handle missing values
        df = handle_missing_values(df)
        
        # Remove duplicate rows
        df = remove_duplicates(df)
        
        # Scale the data manually
        df = scale_data(df)
        
        # Display the cleaned and transformed data
        print("\nCleaned and Transformed Data:")
        print(df.head())

if __name__ == "__main__":
    main()
