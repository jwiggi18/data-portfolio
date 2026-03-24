# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
file_path = "../../data/phd/raw/ecdcs/position_type.xlsx"

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

# replace spaces in column names with and underscore
df.columns = (
    df.columns
    .str.strip() # remove leading/trailing spaces
    .str.lower()  # lowercase
    .str.replace(r"[ ,]", "_", regex=True)# spaces + commas → _
)

# Drop rows that are all NA
df = df.dropna(how="all")

# Inspect
print(df.head())
print(df.columns)
# %%
#subset the table only keeping the 3 biology phd rows, new dataframe = biology_df
biology_df = df.iloc[14:17].copy()
# Rename first column
biology_df = biology_df.rename(columns={biology_df.columns[0]: "field"})
print(biology_df)
# %%
#subset on focal group (most aligned with Okstate bio dept phds)
# 'Biological, agricultural, and environmental life sciences'=row 14 
# note becaue subsetting single row is actually creating a series)
bio_row14 = biology_df.iloc[0]

values14 = bio_row14.drop("field") #the column name is part of the series and cannot be plotted

print(values14)

# %%
#basic plot
values14 = values14.drop(["faculty_total", "other_total"])
plt.bar(values14.index, values14.values)

plt.xticks(rotation=45, ha="right")
plt.ylabel("Percent")
plt.title("Position Types of Early-Career Life Sciences PhDs")

plt.tight_layout()
plt.show()
# %%
#Build a new clean series with aggregated data

clean_values = {
    "Tenure track faculty": (
        values14["tenured_faculty"] +
        values14["tenure-track_faculty"] #add percentages
    ),

    "Non-tenure track faculty": (
        values14["non-tenure_track_faculty_with_rank"] +
        values14["other_faculty__no_rank_or_tenurea"] #add percentages
    ),

    "Postdoctoral scholar": values14["post_doctoral_scholar"],

    "Non-academic research": values14["research_scientist_or_nonfaculty_researcher"],

    "All other positions": values14["all_other_positionsc"]
}

# %%
# Convert to a series to make sure the total is 100%
clean_values = pd.Series(clean_values)
print(clean_values)
print(clean_values.sum())

# %%
# clean up labels
clean_values.index = [
    "Tenure-track faculty",
    "Non-tenure faculty",
    "Postdoc",
    "Non-academic research",
    "Other"
]
# %%
text_color = "#333333"

plt.figure()

bars = plt.bar(clean_values.index, 
               clean_values.values, 
               color="#50838f",
               edgecolor="#333333")

plt.ylabel("Percent of PhDs")
plt.title(
    "Early-Career Life Sciences PhDs by Position Type",
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
