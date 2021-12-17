from nindex import Index


class TempoEvent:
    def __init__(self, beat: int, mBPM, int):
        self.tick = beat
        self.mBPM = mBPM


class TempoCalculator:
    def __init__(self, resolution: int, tempoevents: list[TempoEvent]):
        self.resolution = resolution
        self.tempoevents = tempoevents
        self.tempoevents_by_tick = Index(self.tempoevents, "tick")
