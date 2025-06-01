import matplotlib.pyplot as plt

# Data
years = [2015, 2016, 2017, 2019, 2021, 2024]
revenue = [33.24, 10.99, 35.22, 31.25, 41.41, 4300]  # 2024 in billion INR

# Create the plot
plt.figure(figsize=(10, 5))
plt.plot(years, revenue, marker='o')

# Adding titles and labels
plt.title('Tata Motors Revenue Growth (2015-2024)')
plt.xlabel('Year')
plt.ylabel('Revenue (in billion INR)')
plt.xticks(years)
plt.grid()

# Show the plot
plt.show()