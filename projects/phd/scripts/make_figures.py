# %%
#basic plot
plt.bar(position_bio_ag_life_values.index, position_bio_ag_life_values.values)

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
