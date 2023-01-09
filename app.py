import pandas as pd
import streamlit as st
import src.answers as asw
from src.extraction import load_data

st.set_page_config(layout="wide")

def create_dataframe_section(df):
    st.title("Sections - Database Description")

    col_1, col_2 = st.columns(2)

    col_1.header("Database")
    col_1.dataframe(df, height=530)

    col_2.header("Data Description")

    data_description = """
                        | Feature | Description |
                        | :----- | --------: |
                        | ID | Identification |
                        | name | Motorcycle manufacturer and model |
                        | selling_price | Selling price |
                        | year | Motorcycle year of manufacture |
                        | seller_type | Individual, personal, seller or reseller |
                        | owner | If the motorcycle had one, two, three of four owners |
                        | km_driven | Number of kilometers driven on the motorcycle |
                        | ex_showroom_price | Motorcycle price without insurance and registration fees |
                        | age | Number of years the motorcycle has been in use |
                        | km_class | Classification of motorcycles according to mileage driven |
                        | km_per_year | Kilometers driven each year |
                        | km_per_month | Kilometers driven per month |
                        | company | Motorcycle manufacturer |
    """

    col_2.markdown(data_description)


def create_answers_section(df):
    st.title("Main Questions Answers")

    st.header("First Round")
    st.subheader("How many motorcycles are being sold by their owners and how many are being sold by resellers?")
    asw.rd1_question_9(df)

    st.subheader("How many motorcycles in the database had only one owner?")
    asw.rd1_question_13(df)

    st.subheader("Are the motorcycles with the highest mileage the cheapest motorcycles in the database?")
    asw.rd1_question_14(df)

    st.subheader("Are motorcycles that only had 1 owner more expensive on average than motorcycles that have had more owners?")
    asw.rd2_question_1(df)

    st.subheader("Are the bikes that have had more owners the bikes that have higher average mileage than the bikes that have had fewer owners?")
    asw.rd2_question_2(df)

    st.subheader("Of the manufacturers, which has the largest number of motorcycles registered in the database?")
    asw.rd2_question_5(df)

    st.subheader("Which of the manufacturers has the highest average price of their motorcycles?")
    asw.rd3_question_2(df)

    st.subheader("Is the manufacturer that has the most expensive bike in the Dataset, also the manufacturer that has the fewest registered bikes?")
    asw.rd3_question_5(df)

    st.subheader("Which Motorcycles should be acquired?")
    asw.rd3_question_7(df)

def create_main_layout():
    df = load_data()
    create_dataframe_section(df)
    create_answers_section(df)

if __name__ == "__main__":
    create_main_layout()
