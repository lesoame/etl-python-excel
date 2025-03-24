# imports
import pandas as pd
from ydata_profiling import ProfileReport

# Load data
df = pd.read_csv('data.csv')

# Generate report
profile = ProfileReport(df, title="Pandas Profile Report")

# Save report to file
profile.to_file("output.html")
