from collections import defaultdict

import pandas as pd

from ceam.engine import SimulationModule

class MetricsModule(SimulationModule):
    def setup(self):
        self.metrics = defaultdict(int)
        self.register_event_listener(self.event_sums, 'healthcare_access')
        self.register_event_listener(self.count_deaths_and_ylls, 'deaths')
        self.register_event_listener(self.count_ylds, 'time_step')

    def load_data(self, path_prefix):
        self.life_table = pd.read_csv('/home/j/Project/Cost_Effectiveness/dev/data/gbd/interpolated_reference_life_table.csv')

    def event_sums(self, label, mask, simulation):
        self.metrics[label] += sum(mask)

    def count_deaths_and_ylls(self, label, mask, simulation):
        self.metrics['deaths'] += sum(mask)
        self.metrics['ylls'] += simulation.population.merge(self.life_table, on=['age'])[mask].ex.sum()

    def count_ylds(self, label, mask, simulation):
        self.metrics['ylds'] += sum(simulation.disability_weight()) * (simulation.last_time_step.days/365.0)

    def reset(self):
        self.metrics = defaultdict(int)
