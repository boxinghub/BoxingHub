class BoxingChatbot:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = 'start'
        self.topics = ['jab', 'cross', 'hook', 'uppercut']
        self.defenses = {
            'jab': ['block', 'deflection and move to the side', 'lean back', 'parry', 'roll under', 'slip', 'step back'],
            'cross': ['slip', 'block', 'parry', 'lean back', 'roll under'],
            'hook': ['block', 'parry', 'roll under', 'slip'],
            'uppercut': ['block', 'lean back', 'parry', 'step back']
        }
        self.feedback = {
            'jab': {'block': 'Not very effective', 'deflection and move to the side': 'Effective', 'lean back': 'Risky', 
                    'parry': 'Effective', 'roll under': 'Not effective', 'slip': 'Very effective', 'step back': 'Good'},
            'cross': {'slip': 'Very effective', 'block': 'Effective', 'parry': 'Good', 'lean back': 'Risky', 'roll under': 'Not effective'},
            'hook': {'block': 'Effective', 'parry': 'Good', 'roll under': 'Effective', 'slip': 'Risky'},
            'uppercut': {'block': 'Effective', 'lean back': 'Risky', 'parry': 'Good', 'step back': 'Very effective'}
        }
        self.counter_punches = ['jab', 'cross', 'hook', 'uppercut']
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
            return {'message': f'You chose {self.topic}. Select a defense move:', 'options': self.defenses[self.topic]}
        
        if self.state == 'defense_selected':
            defense = user_input
            feedback = self.feedback[self.topic].get(defense, 'Not a valid move')
            if feedback == 'Not a valid move':
                self.state = 'topic_selected'
                return {'message': 'Choose a punch:', 'options': self.topics}
            self.state = 'counter_selected'
            return {'message': f'You chose {defense}. Feedback: {feedback}. Now choose a counter punch:', 'options': self.counter_punches}
        
        if self.state == 'counter_selected':
            counter_punch = user_input
            feedback = self.counter_punches_feedback.get(counter_punch, 'Not a valid move')
            if feedback == 'Not a valid move':
                self.state = 'topic_selected'
                return {'message': 'Choose a punch:', 'options': self.topics}
            self.state = 'end'
            return {'message': f'You chose {counter_punch}. {feedback}\nDo you want to restart?', 'options': ['Yes', 'No']}
        
        if self.state == 'end':
            if user_input == 'Yes':
                self.state = 'topic_selected'
                return {'message': 'Conversation started. Choose a punch:', 'options': self.topics}
            elif user_input == 'No':
                return {'message': 'Conversation has ended.', 'options': ['Restart']}
            elif user_input == 'Restart':
                self.state = 'topic_selected'
                return {'message': 'Conversation restarted. Choose a punch:', 'options': self.topics}
            else:
                return {'message': 'Hi, do you want to start learning boxing?', 'options': ['Yes', 'No']}

