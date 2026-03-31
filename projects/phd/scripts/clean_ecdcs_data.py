# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
file_path = "../data/raw/ecdcs/position_type.xlsx"

# Skip messy header rows
df = pd.read_excel(
    file_path, 
    skiprows=4,
    engine="openpyxl")
# %%
print(df.head())
# %%
print(df.columns)

# %%
# correct column names
df = df.rename(columns={
    df.columns[0]: "selected_characteristic",
    df.columns[1]: "total_surveyed",
    df.columns[2]: "faculty_total",
    df.columns[7]: "post_doctoral_scholar",
    df.columns[8]: "other_total"
})

# replace spaces in column names with an underscore
df.columns = (
    df.columns
    .str.strip() # remove leading/trailing spaces
    .str.lower()  # lowercase
    .str.replace(r"[ ,]", "_", regex=True)# spaces + commas to _
)

# Drop rows that are all NA
df = df.dropna(how="all")

# Inspect
print(df.head())
print(df.columns)
# %%
# ******** Create Biology Specific Data Frame *********
# Subset the table only keeping the 3 biology phd rows, new dataframe = biology_df
biology_df = df.iloc[14:17].copy()

# Rename first column, initial spreadsheet had categories in col 0 that were not just field
biology_df = biology_df.rename(columns={biology_df.columns[0]: "field"})

# Save biology_df as excel file
biology_df.to_excel("../data/processed/all_biology_fields.xlsx", index=False)

print(biology_df)
# %%
# ****** Create Biology, Ag, & Life Sciences Series = bio_ag_life_values ********
#subset on focal group (most aligned with Okstate bio dept phds)
# 'Biological, agricultural, and environmental life sciences'=row 14 
# note: subsetting single row is actually creating a series so code changes
bio_ag_life = biology_df.iloc[0]

bio_ag_life_values = bio_ag_life.drop("field") #the column name is part of the series and cannot be plotted

print(bio_ag_life_values)

# %%
#basic plot
bio_ag_life_values = bio_ag_life_values.drop(["faculty_total", "other_total"]) # column totals for whole spreadsheet
plt.bar(bio_ag_life_values.index, bio_ag_life_values.values)

plt.xticks(rotation=45, ha="right")
plt.ylabel("Percent")
plt.title("Position Types of Early-Career Life Sciences PhDs")

plt.tight_layout()
plt.show()
# %%

# Aggregate bio_ag_life_values by job category
bio_ag_life_aggregate = {
    "Tenure track faculty": (
        bio_ag_life_values["tenured_faculty"] +
        bio_ag_life_values["tenure-track_faculty"] #add percentages
    ),

    "Non-tenure track faculty": (
        bio_ag_life_values["non-tenure_track_faculty_with_rank"] +
        bio_ag_life_values["other_faculty__no_rank_or_tenurea"] #add percentages
    ),

    "Postdoctoral scholar": bio_ag_life_values["post_doctoral_scholar"],

    "Non-academic research": bio_ag_life_values["research_scientist_or_nonfaculty_researcher"],

    "Ohter": bio_ag_life_values["all_other_positionsc"]
}

# %%
# Convert to a series so can add %s to make sure the total is ~ 100%
bio_ag_life_aggregate = pd.Series(bio_ag_life_aggregate)
print(bio_ag_life_aggregate)
print(bio_ag_life_aggregate.sum())


# %%
text_color = "#333333"

plt.figure()

bars = plt.bar(bio_ag_life_aggregate.index, 
               bio_ag_life_aggregate.values, 
               color="#50838f",
               edgecolor="#333333")

plt.ylabel("Percent of PhDs")
plt.title(
    "Early-Career Biology, Agriculture, and Life Sciences PhDs by Position Type",
    color=text_color,
    fontweight="bold")

plt.xticks(rotation=30, ha="right", color=text_color)
plt.yticks(color=text_color)
plt.ylabel("Percent of PhDs", color=text_color)

# Clean axes
ax = plt.gca()
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.yaxis.grid(True, linestyle="--", linewidth=0.5)
ax.set_axisbelow(True)

# Add labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f"{height:.1f}",
        ha="center",
        va="bottom",
        color=text_color
    )

plt.tight_layout()
plt.show()
# %%
