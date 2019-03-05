"""Hyperparameters of the algorithm."""

from models.individual import Individual

class Config:
    INDIVIDUALS = 5
    GNRTS = 10
    CURR_GENERATION = 0
    OFFSPRING = 2
    MUTATATION_PROB = 0.2
    DISCARD_PER = 0
    # EXTN_PER = 0.2
    TUPLE_SIZE = 3
    STEP = 10

    def add_meta(i: Individual) -> Individual:
        config_vals = [a for a in dir(Config) if not a.startswith('__')]
        config_vals.remove('add_meta')
        config_vals.remove('TUPLE_SIZE')
        config_vals.remove('CURR_GENERATION')
        for attr in config_vals:
            i.meta.update({attr: getattr(Config, attr)})
        return i
