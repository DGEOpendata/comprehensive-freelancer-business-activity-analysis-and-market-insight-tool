python
import pandas as pd
import matplotlib.pyplot as plt

# Load the Freelancer Business Activities Dataset
data_url = 'https://data.abudhabi/api/datasets/DL06-Freelance-Activities-ADRA-OD-010-AFR.csv'
data = pd.read_csv(data_url)

# User-defined function to filter dataset
def filter_data(category):
    filtered_data = data[data['Category'] == category]
    return filtered_data

# Example: Filter for 'Consultancy Services'
category = 'Consultancy Services'
filtered_data = filter_data(category)
print(filtered_data.head())

# Generate a visualization of the top 10 services in the category
def plot_top_services(filtered_data):
    top_services = filtered_data['ServiceName'].value_counts().head(10)
    top_services.plot(kind='bar', color='skyblue')
    plt.title(f'Top 10 Services in {category}')
    plt.xlabel('Service')
    plt.ylabel('Frequency')
    plt.show()

plot_top_services(filtered_data)
