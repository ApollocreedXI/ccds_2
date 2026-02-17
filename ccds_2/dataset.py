

from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer
import pandas as pd


from ccds_2.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()

@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = RAW_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    # ----------------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    # Loading data
    loc = input_path
    df = pd.read_csv(loc)

    # Creating a 'less than a high school diploma attribute'
    df['Edu_attain_less_than_High_school_graduate_Population_25_years_and_over'] = df['education_b15003_lt9th'] + df['education_b15003_9th_to_12thnodiploma']
    # Creating a 'some college or associate degree' attribute
    df['Edu_attain_some_college_or_associates_Population_25_years_and_over'] = df['education_b15003_somecollegenodegree'] + df['education_b15003_021e']    
    # Creating a subset of neighborhoods to analyze
    sub_set = ['South Boston', 'South Boston Waterfront', 'South End', 'Downtown']
    df_subset = df[df['name'].isin(sub_set)]

    # Renaming the sum of the population counts for the population 25 years older in the following categories
    # - Less than a high school diploma
    # - High school graduate
    # - Some college or associate's degree
    # - Bachelor's degree
    # - Graduate or professional degree
    df_subset.rename(columns={"education_b15003_001e": "Edu_attain_all_Total_Population_25_years_and_over_"}, inplace=True)
    # Renaming the highschool educational attainment category for those who are of 25 or older of age
    df_subset.rename(columns={"education_b15003_hsgrad_and_ged": "Edu_attain_High_school_graduate_Population_25_years_and_over_"}, inplace=True)
    # Renaming the bachelors educational attainment category for those who are of 25 or older of age
    df_subset.rename(columns={"education_b15003_022e": "Edu_attain_Bachelor_25_years_and_over_"}, inplace=True)
    # Renaming the graduate or professional educational attainment category for those who are of 25 or older of age
    df_subset.rename(columns={"education_b15003_gradprofdegree": "Edu_attain_graduate_or_professional_25_years_and_over_"}, inplace=True)

    # Outputting data to directory
    df_subset.to_csv(output_path)

    # -----------------------------------------


if __name__ == "__main__":
    app()
