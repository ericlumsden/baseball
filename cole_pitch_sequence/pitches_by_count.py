import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pandas as pd

# Colors_dict
colors_dict = {
    'FF': 'red',
    'CH': 'green',
    'FC': 'orange',
    'KC': 'yellow',
    'SL': 'blue'
}
legend_handles = [mpatches.Patch(color=colors_dict[key], label=key) for key in colors_dict.keys()]

# Function for plotting pie charts based on count
def count_pie_chart(pitches: pd.DataFrame, label: str):
    fig, axs = plt.subplots(4,3)
    for ball in range(4):
        for strike in range(3):
            count_pitch_tally = {
                "FF": 0,
                "CH": 0,
                "FC": 0,
                "KC": 0,
                "SL": 0
                }

            pitches_in_count = pitches.loc[(pitches["balls"] == ball) & (pitches["strikes"] == strike)]
            for pitch in pitches_in_count['pitch_type'].unique():
                count_pitch_tally[pitch] += pitches_in_count["pitch_type"].value_counts()[pitch]

            if (sum(list(count_pitch_tally.values())) != 0):
                axs[int(abs(ball-3)), strike].pie(list(count_pitch_tally.values()), colors=list(colors_dict.values()), normalize=True)
                axs[int(abs(ball-3)), strike].set_title(f"{ball}-{strike}")
                axs[int(abs(ball-3)), strike].set_xticks([])
                axs[int(abs(ball-3)), strike].set_yticks([])
            else:
                axs[int(abs(ball-3)), strike].legend(handles=legend_handles, loc="upper left")
                axs[int(abs(ball-3)), strike].set_xticks([])
                axs[int(abs(ball-3)), strike].set_yticks([])
            for spine in ["bottom", "top", "right", "left"]:
                axs[int(abs(ball-3)), strike].spines[spine].set_visible(False)
    plt.tight_layout()
#    legend_handles = [mpatches.Patch(color=colors_dict[key], label=key) for key in colors_dict.keys()]
    plt.legend()
    plt.savefig(f"./figs/count_specific_pie_chart_{label}.png")

if __name__ == "__main__":
    cole_pitches_v_boston = pd.read_csv('./cole_pitches_vs_boston.csv')
    cole_pitches_season = pd.read_csv('./cole_pitches_SEASON.csv')
    count_pie_chart(cole_pitches_v_boston, "boston")
    count_pie_chart(cole_pitches_season, "season")

