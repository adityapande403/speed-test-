#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import streamlit as st
import speedtest
import csv
import concurrent.futures

# Initialize Streamlit
st.title("Internet Speed Test App")

# Initialize Speedtest
stt = speedtest.Speedtest()

# Function to perform a speed test and return the result as a tuple
def run_speed_test(_):
    stt.get_best_server()
    download_speed = stt.download() / 10**6
    upload_speed = stt.upload() / 10**6
    return download_speed, upload_speed

# Create a CSV file for saving the data
with open('internet_speed_100_rows.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Download (Mbps)', 'Upload (Mbps)'])  # Write header row

    # Perform 100 speed tests concurrently
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(run_speed_test, range(2)))

    # Write results to the CSV file
    for download_speed, upload_speed in results:
        writer.writerow([download_speed, upload_speed])

# Display the saved data
st.subheader("Internet Speed Data")
st.write(results)

# Provide a download link for the CSV file
st.subheader("Download Data")
st.markdown("[Download CSV File](internet_speed_100_rows.csv)")

st.write('Internet speed data saved to internet_speed_100_rows.csv')


# In[ ]:




