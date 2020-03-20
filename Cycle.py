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
            distress_tolerance = ['Imagery', ]
            cycle_list = [physical_health, mood_regulation, emotional_regulation, build_mastery]
        else:
            print("File reading not yet implemented")
            assert False

    def update_cycle(self, user_input):
        pass

    def print_new_idea(self):
        pass

    def print_options(self):
        print("Type 0 to quit")
