# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Cleaning of three datasets dowloaded from the ECDS website:
# - employment_setting.xlsx
# - position_type.xlsx
# - sex_ethnicity.xlsx

base_path = "../data/raw/ecdcs/"


# %%
# column name cleaning function
def clean_column_names(df):
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.replace(r"_+", "_", regex=True)
        .str.strip("_")
    )
    return df



# %%
# ******************** Position Type dataset *********************
# Skip messy header rows
position_df = pd.read_excel(
    base_path + "position_type.xlsx", 
    skiprows=4,
    engine="openpyxl")
# %%
print(position_df.head())
# %%
print(position_df.columns)


# %%
# correct column names
position_df = position_df.rename(columns={
    "Unnamed: 0": "selected_characteristic",
    "Unnamed: 1": "total_surveyed",
    "Total": "faculty_total",
    "Unnamed: 7": "post_doctoral_scholar",
    "Total.1": "other_total",
    
    # fix footnotes
    "Other faculty, no rank or tenurea": "other_faculty_no_rank_or_tenure",
    "All other positionsc": "all_other_positions"
})

# drop columns that are whole data set totals (column totals - rather than row)
position_df = position_df.drop(columns=["faculty_total", "other_total"])

# Clean up column names
position_df = clean_column_names(position_df)

# Drop rows that are all NA
position_df = position_df.dropna(how="all")

# Inspect
print(position_df.head())
print(position_df.columns)


# %%
# ******** Create Biology Specific Data Frame *********
# check row names for certainty in subsetting
print(position_df.loc[:, ["selected_characteristic"]])


# %%
# Subset the table only keeping the 3 biology phd rows, new dataframe = biology_position_df
biology_position_df = position_df[
    position_df["selected_characteristic"].isin([
        "Biological, agricultural, and environmental life sciences",
        "Agricultural and environmental life sciences",
        "Biological and biomedical sciences"
    ])
].copy()

# Rename first column, initial spreadsheet had categories in col 0 that were not just field
biology_position_df = biology_position_df.rename(columns={biology_position_df.columns[0]: "field"})

print(biology_position_df)

# %%
# Save biology_position_df as excel file
biology_position_df.to_excel("../data/processed/ecdcs/position_all_biology.xlsx", index=False)

# %%
# ****** Create Biology, Ag, & Life Sciences dataset position_bio_ag_life_values ********
#subset on focal group (most aligned with Okstate bio dept phds)
position_bio_ag_life = position_df[
    position_df["selected_characteristic"].str.strip() == 
    "Biological, agricultural, and environmental life sciences"
].copy()

print(position_bio_ag_life)
print(len(position_bio_ag_life))


# %%
# Save position_bio_ag_life as excel file
position_bio_ag_life.to_excel("../data/processed/ecdcs/position_bio_ag_life.xlsx", index=False)


# %%
# ****** Create Agricultural and environmental life sciences dataset position_ag_life ********

position_ag_life = position_df[
    position_df["selected_characteristic"].str.strip() == 
    "Agricultural and environmental life sciences"
].copy()

print(position_ag_life)
print(len(position_ag_life))


# %%
# Save position_bio_ag_life as excel file
position_ag_life.to_excel("../data/processed/ecdcs/position_ag_life.xlsx", index=False)

# %%
# ****** Create Biological and biomedical sciences dataset position_bio_biomed********

position_bio_biomed = position_df[
    position_df["selected_characteristic"].str.strip() == 
    "Biological and biomedical sciences"
].copy()

print(position_bio_biomed)
print(len(position_bio_biomed))


# %%
# Save position_bio_ag_life as excel file
position_bio_biomed.to_excel("../data/processed/ecdcs/position_bio_biomed.xlsx", index=False)
# %%
