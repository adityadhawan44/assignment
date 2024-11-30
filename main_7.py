import pandas as pd

# Function to read data from CSV
def read_data(filename):
    try:
        df = pd.read_csv(filename)  # Read the CSV file into a DataFrame
        print(f"Data loaded successfully from {filename}.\n")
        
        # Print the first few rows to inspect the data
        print("First few rows of the dataset:")
        print(df.head(), "\n")
        
        return df
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the file: {e}")
        return None

# Function to calculate and print basic statistics
def basic_statistics(df):
    if df is not None:
        # Print basic statistics for numerical columns only
        print("\nBasic Statistics:")
        
        # Ensure only numeric columns are processed for mean, median, and mode
        numeric_df = df.select_dtypes(include=['number'])  # Only numeric columns
        
        # Calculate mean, median, and mode for each numeric column
        print(f"Mean of each numerical column:\n{numeric_df.mean()}\n")
        print(f"Median of each numerical column:\n{numeric_df.median()}\n")
        print(f"Mode of each numerical column:\n{numeric_df.mode().iloc[0]}\n")
        
        # Display summary statistics
        print(f"Summary statistics (describe):\n{numeric_df.describe()}\n")
    else:
        print("No data available for analysis.")

# Main function to drive the script
def main():
    filename = input("Enter the CSV file name (with extension): ")
    
    # Load data from the CSV file
    df = read_data(filename)
    
    if df is not None:
        # Check if the 'Age' and 'Salary' columns contain numeric data
        if not pd.to_numeric(df['Age'], errors='coerce').isnull().any():
            print("\n'Age' column is valid for analysis.")
        else:
            print("\n'Age' column contains non-numeric values, which may cause issues.")
        
        if not pd.to_numeric(df['Salary'], errors='coerce').isnull().any():
            print("'Salary' column is valid for analysis.\n")
        else:
            print("'Salary' column contains non-numeric values, which may cause issues.\n")
        
        # Generate and display basic statistics
        basic_statistics(df)

if __name__ == "__main__":
    main()
