import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Will need to make a dictionary of all pitch combos thrown by Cole
def make_pitch_sequence_dict(pitch_types: list) -> dict:
    temp_dict = {}
    for prev_pitch in pitch_types:
        temp_dict[prev_pitch] = {}
        for pitch in pitch_types:
            temp_dict[prev_pitch][pitch] = 0
    return temp_dict

# Need another function to check for which pitches followed which
# Obviously the first pitch of an at bat doesn't count
def find_following_pitch(pitch_table: pd.DataFrame, pitch_dict: dict) -> dict:
    for index, row in pitch_table.iterrows():
        if (row["balls"] + row["strikes"]) != 0:
            pitch_dict[pitch_table.loc[int(index-1), "pitch_type"]][row["pitch_type"]] += 1
    return pitch_dict


if __name__ == "__main__":
    # Then load in Cole's pitch data and run the make_pitch_sequence_dict function to generate an empty dictionary with all pitch combos
    cole_pitches = pd.read_csv('./cole_pitches_SEASON.csv')
    cole_pitches_BOS = pd.read_csv('./cole_pitches_vs_boston.csv')

    pitch_types = cole_pitches_BOS["pitch_type"].unique()
    pitch_sequence = make_pitch_sequence_dict(pitch_types)
    pitch_sequence = find_following_pitch(cole_pitches, pitch_sequence)

    # Visualize this data
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    colors_dict = {
        'FF': 'red',
        'CH': 'green',
        'FC': 'orange',
        'KC': 'yellow',
        'SL': 'blue'
    }
    import numpy as np
    plt.figure(0)
    legend_handles = []
    for x, first_pitch in enumerate(pitch_types):
        first_pitch_sum = sum(pitch_sequence[first_pitch].values())
        legend_handles.append(mpatches.Patch(color=colors_dict[first_pitch], label=first_pitch))
        bottom = 0
        for pitch in pitch_types:
            plt.bar(x, pitch_sequence[first_pitch][pitch] / first_pitch_sum, color=colors_dict[pitch], bottom=bottom)
            bottom += pitch_sequence[first_pitch][pitch] / first_pitch_sum
    plt.xticks(range(len(pitch_types)), pitch_types)
    plt.xlabel('previous pitch')
    plt.ylim([0,1])
    plt.ylabel('proportion of next pitch')
    plt.title('fraction of pitches based on previous pitch 2023 season')
    plt.legend(handles=legend_handles)
    plt.savefig('./figs/fraction_general_sequence_SEASON.png')