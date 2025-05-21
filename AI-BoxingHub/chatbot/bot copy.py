class BoxingChatbot:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = 'start'
        punches = ['jab', 'cross', 'hook', 'uppercut']
        self.topics = punches
        defenses = ['block', 'lean back', 'parry', 'roll under', 'slip', 'step back']
        self.defenses = {
            'jab': defenses,
            'cross': defenses,
            'hook': defenses,
            'uppercut': defenses,
        }
        effective_level = ['Not effective', 'Risky', 'Not very effective', 'Effective', 'Very effective']
        self.feedback = {
            'jab': {'block': effective_level[2],
                    'lean back': effective_level[1],
                    'parry to deflect': effective_level[3],
                    'roll under': effective_level[2],
                    'slip': effective_level[4],
                    'step back': effective_level[3]},
            'cross': {'block': effective_level[2],
                      'lean back': effective_level[1],
                      'parry': effective_level[1],
                      'roll under': effective_level[3],
                      'slip': effective_level[4],
                      'step back': effective_level[3]},
            'hook': {'block': effective_level[2],
                     'lean back': effective_level[1],
                     'parry': effective_level[1],
                     'roll under': effective_level[4],
                     'slip': effective_level[0],
                     'step back': effective_level[2]},
            'uppercut': {'block': effective_level[3],
                         'lean back': effective_level[3],
                         'parry': effective_level[1],
                         'roll under': effective_level[0],
                         'slip': effective_level[2],
                         'step back': effective_level[4]},
                        
        }
        self.counter_punches = punches
        self.counter_punches_feedback = {
            'jab': 'Good choice! The jab is a versatile punch that can be used to keep your opponent at a distance.',
            'cross': 'Nice! The cross is a powerful punch that can be used to counter your opponent effectively.',
            'hook': 'Well done! The hook is a great punch to use when your opponent is open.',
            'uppercut': 'Great choice! The uppercut is a sneaky punch that can catch your opponent off guard.'
        }

    def get_response(self, user_input):
        if self.state == 'start':
            self.state = 'topic_selected'
            return {'message': 'Choose a punch:', 'options': self.topics}
        
        if self.state == 'topic_selected':
            if user_input not in self.topics:
                return {'message': 'Choose a punch:', 'options': self.topics}
            self.topic = user_input
            self.state = 'defense_selected'
            return {'message': f'You chose {self.topic}.<br>- Select a defense move:', 'options': self.defenses[self.topic]}
        
        if self.state == 'defense_selected':
            defense = user_input
            feedback = self.feedback[self.topic].get(defense, 'Not a valid move')
            if feedback == 'Not a valid move':
                self.state = 'topic_selected'
                return {'message': 'Choose a punch:', 'options': self.topics}
            self.state = 'counter_selected'
            return {'message': f'You chose {defense}.<br>- Feedback: {feedback}.<br>Now choose a counter punch:', 'options': self.counter_punches}
        
        if self.state == 'counter_selected':
            counter_punch = user_input
            feedback = self.counter_punches_feedback.get(counter_punch, 'Not a valid move')
            if feedback == 'Not a valid move':
                self.state = 'topic_selected'
                return {'message': 'Choose a punch:', 'options': self.topics}
            self.state = 'end'
            return {'message': f'You chose {counter_punch}.<br>- Feedback: {feedback}<br>Do you want to restart?', 'options': ['Yes', 'No']}
        
        if self.state == 'end':
            if user_input == 'Yes':
                self.state = 'topic_selected'
                return {'message': 'Conversation started.<br>- Choose a punch:', 'options': self.topics}
            elif user_input == 'No':
                return {'message': 'Conversation has ended.', 'options': ['Restart']}
            elif user_input == 'Restart':
                self.state = 'topic_selected'
                return {'message': 'Conversation restarted.<br>- Choose a punch:', 'options': self.topics}
            else:
                return {'message': 'Hi, do you want to start learning boxing?', 'options': ['Yes', 'No']}

