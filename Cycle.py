import random


class Cycle:

    def __init__(self, filename='saved_cycle.json'):
        if filename == 'saved_cycle.json':
            physical_health = ['Medical Needs', 'Eat', 'Drink', 'Exercise']
            mood_regulation = ['Hold Emotion to Soothe or Magnify', 'Opposite to Emotion']
            emotional_regulation = ['Build Positive Experience', 'Attend to Relationships', 'Look Back or Plan Ahead',
                                    'GIVE', 'Feelings Statement']
            build_mastery = ['Dishes', 'Shopping for Food', 'Cleaning', 'Laundry Stack', 'Open Mail',
                             'Bill Pay or Paperwork', 'Phone Calls', 'Work', 'Litterbox', 'Declutter',
                             'Deal with Email and Voicemail', 'Prayer']
            distress_tolerance = ['Imagery', 'Do One Thing', 'Meaning', 'Comparisons', 'Tonglen', 'Touch',
                                  'Spiritual Sense', 'Smell', 'Encouragement', 'TIP', 'Activities', 'Thoughts',
                                  'Relaxation', 'Radical Acceptance', 'Sensations', 'Prayer']
            self.distress_cycles = [distress_tolerance]
            self.uncomfortable_cycles = [mood_regulation]
            self.serene_cycles = [physical_health, emotional_regulation, build_mastery]
            self.all_cycles = [self.distress_cycles, self.uncomfortable_cycles, self.serene_cycles]
        else:
            print("File reading not yet implemented")
            assert False
        self.positions = [0, 0, [0, 0, 0]]
        self.initialize_positions()
        self.current_spot = [0, 0]
        self.serene_cycle = 0

    def initialize_positions(self):
        self.positions[0] = random.randint(0, len(self.distress_cycles[0]))
        self.positions[1] = random.randint(0, len(self.uncomfortable_cycles[0]))
        self.positions[2] = [random.randint(0, len(listie)) for listie in self.serene_cycles]
        self.serene_cycle = random.randint(0, 3)

    def update_cycle(self, user_input):
        off_by_one = user_input - 1
        if off_by_one in [0, 1]:
            self.current_spot = [
                off_by_one, (self.positions[off_by_one] + 1) % len(self.all_cycles[off_by_one][0])]
            self.positions[off_by_one] = (self.positions[off_by_one] + 1) % len(self.all_cycles[off_by_one][0])
        else:
            self.current_spot = [2, (self.positions[2][self.serene_cycle] + 1) % len(
                self.serene_cycles[self.serene_cycle])]
            self.positions[2][self.serene_cycle] = (self.positions[2][self.serene_cycle] + 1) % len(
                self.serene_cycles[self.serene_cycle])
            self.serene_cycle = (self.serene_cycle + 1) % 3

    def print_new_idea(self):
        if self.current_spot[0] in [0, 1]:
            print(self.all_cycles[self.current_spot[0]][0][self.current_spot[1]])
        else:
            print(self.serene_cycles[self.serene_cycle][self.positions[2][self.serene_cycle]])

    def print_options(self):
        print("Type 0 to quit")
        print("1. Distress")
        print("2. Uncomfortable Feeling")
        print("3. Serene")
