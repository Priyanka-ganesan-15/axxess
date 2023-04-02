
import pandas as pd
import streamlit as st
import altair as alt
import seaborn as sns
import matplotlib as plt


# Define the function to pull and display patient data
def pull_patient_data(name_sel):
    # Read in the data from the CSV file
    analysis_dataframe = pd.read_csv("input.csv")

# Define the columns to be used in the analysis
    usecols = range(1, 7)

    # Filter the data for the selected patient
    patient_data = analysis_dataframe[analysis_dataframe.Name == name_sel]

    # Sort the data by date in ascending order
    patient_data = patient_data.sort_values(by="TODAY", inplace=False, ascending=True)

    # Group the data by date and calculate the average time taken for each date
    new_df = patient_data.groupby("TODAY")["time_taken"].mean().reset_index()

    # Display the data in a DataFrame format
    st.dataframe(new_df)

    # Convert the date column to a datetime type
    new_df["TODAY"] = pd.to_datetime(new_df["TODAY"])

    # Create a line chart using Altair
    chart = (
        alt.Chart(new_df)
        .mark_line()
        .encode(
            x=alt.X("TODAY:T", title="Date"),
            y=alt.Y("time_taken:Q", title="Time Taken (in minutes)"),
        )
        .properties(width=600, height = 500, title="overall Performance Over Time")
        .interactive()
    )

    # Display the chart in Streamlit
    st.altair_chart(chart)

    # Group the data by date and exercise type and calculate the average time taken for each group
    df_grouped = (
        patient_data.groupby(["TODAY", "exercise type"])["time_taken"]
        .mean()
        .reset_index()
    )

    # Create a line chart using Altair
    chart = (
        alt.Chart(df_grouped)
        .mark_line()
        .encode(
            x=alt.X("TODAY:T", title="Date"),
            y=alt.Y("time_taken:Q", title="Time Taken (in seconds)"),
            color="exercise type:N",
        )
        .properties(width=700, height = 500, title="Exercise Performance Over Time")
        .interactive()
    )

    # Display the chart in Streamlit
    st.altair_chart(chart,use_container_width=True)
  
    # Group the data by date and exercise type and calculate the average time taken for each group
    df_grouped = (
        patient_data.groupby(["TODAY", "test type"])["time_taken"]
        .mean()
        .reset_index()
    )



    # Create a line chart using Altair
    chart = (
        alt.Chart(df_grouped)
        .mark_line()
        .encode(
            x=alt.X("TODAY:T", title="Date"),
            y=alt.Y("time_taken:Q", title="Time Taken (in seconds)"),
            color="test type:N",
        )
        .properties(width=700, height = 500,title="test type Performance Over Time")
        .interactive()
    )

    # Display the chart in Streamlit
    st.altair_chart(chart)

    # # calculate percent change for each exercise type
    # exercise_counts = patient_data.groupby("exercise type").size().reset_index(name="count")
    # total_tests = exercise_counts["count"].sum()
    # exercise_counts["percent"] = exercise_counts["count"] / total_tests * 100

    # # calculate percent change for each exercise type
    # exercise_times = patient_data.groupby("exercise type").agg({"time_taken": ["mean", "first", "last"]})
    # exercise_times.columns = ["_".join(col).strip() for col in exercise_times.columns.values]
    # exercise_times["percent_change"] = ((exercise_times["time_taken_last"] - exercise_times["time_taken_first"]) / exercise_times["time_taken_first"]) * 100

    # # create bar chart using altair
    # bar_chart = alt.Chart(exercise_times.reset_index()).mark_bar().encode(
    #     x=alt.X('index:O', axis=alt.Axis(labelAngle=45)),
    #     y='percent_change:Q'
    # ).properties(
    #     title='Percent Change in Time Taken for Each Exercise Type'
    # )

    # # display bar chart in streamlit
    # st.altair_chart(bar_chart, use_container_width=True)


    # # Create a bar chart using Altair
    # chart = alt.Chart(exercise_times).mark_bar().encode(
    # x='count',
    # y='percent_change',
    # color='count'       
    # ).properties(
    # width=500,
    # height=400,
    # title='Percent Change in Time Taken by Exercise Type'
    # )

    # st.altair_chart(chart)

    # # Display the chart and the exercise dates in Streamlit
    # st.altair_chart(chart)
    