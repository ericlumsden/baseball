from dataclasses import dataclass

@dataclass
class PitchNode:
    balls: int
    strikes: int
    pitch_type: str
    pitch_num: int 
    children = []
    count: int = 0
    def increase_count(self) -> self:
        self.count += 1
        return self

def at_bat_sequence(sequence_class: PitchNode, pitches_in_at_bat: pd.DataFrame) -> dict:
    temp_sequence = sequence_class
    for idx, row in pitches_in_at_bat.iterrows():
        if PitchNode(row["pitch_type"] ...) # HOW DO I KEEP TRACK OF WHERE I AM IN THE TREE?
    return sequence_class


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import pandas as pd
    
    sequence = PitchNode(0, 0, "", 0)
