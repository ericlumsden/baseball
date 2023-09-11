import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

# Colors_dict
colors_dict = {
    'FF': ('red', 0, 0),
    'CH': ('green', 0, 1),
    'FC': ('orange', 1, 0),
    'KC': ('yellow', 1, 1),
    'SL': ('blue', 2, 0)
}

legend_handles = [mpatches.Patch(color=colors_dict[key][0], label=key) for key in colors_dict.keys()]

# Function for plotting pie charts based on count
def count_pie_chart(pitches: pd.DataFrame, label: str):
    fig, axs = plt.subplots(3,2)
    for pitch_type in colors_dict.keys():
        ax1 = colors_dict[pitch_type][1]
        ax2 = colors_dict[pitch_type][2]
        count_pitch_tally = {
            "0-0": 0,
            "0-1": 0,
            "0-2": 0,
            "1-0": 0,
            "1-1": 0,
            "1-2": 0,
            "2-0": 0,
            "2-1": 0,
            "2-2": 0,
            "3-0": 0,
            "3-1": 0,
            "3-2": 0
        }

        pitches_all_counts = pitches.loc[(pitches["pitch_type"] == pitch_type)]
        for idx, row in pitches_all_counts.iterrows():
            if (row['balls'] + row['strikes'] == 0):
                continue
            count_pitch_tally[f"{row['balls']}-{row['strikes']}"] += 1

        count_labels = [key for key in count_pitch_tally.keys() if count_pitch_tally[key] != 0]
        if (sum(list(count_pitch_tally.values())) != 0):
            axs[ax1, ax2].pie([count_pitch_tally[key] for key in count_pitch_tally.keys() if count_pitch_tally[key] != 0], labels=count_labels, normalize=True)
            axs[ax1, ax2].set_title(pitch_type)
            axs[ax1, ax2].set_xticks([])
            axs[ax1, ax2].set_yticks([])
        else:
            axs[ax1, ax2].legend(handles=legend_handles, loc="upper left")
            axs[ax1, ax2].set_xticks([])
            axs[ax1, axs].set_yticks([])
        for spine in ["bottom", "top", "right", "left"]:
            axs[ax1, ax2].spines[spine].set_visible(False)
    
    for spine in ["bottom", "top", "right", "left"]:
        axs[2, 1].spines[spine].set_visible(False)
    axs[2,1].set_xticks([])
    axs[2,1].set_yticks([])
    plt.tight_layout()
#    legend_handles = [mpatches.Patch(color=colors_dict[key], label=key) for key in colors_dict.keys()]
    plt.legend()
    plt.savefig(f"./figs/count_specific_pie_chart_{label}.png")

if __name__ == "__main__":
    cole_pitches_v_boston = pd.read_csv('./cole_pitches_vs_boston.csv')
    cole_pitches_season = pd.read_csv('./cole_pitches_SEASON.csv')
    count_pie_chart(cole_pitches_v_boston, "boston_by_count")
    count_pie_chart(cole_pitches_season, "season_by_count")

