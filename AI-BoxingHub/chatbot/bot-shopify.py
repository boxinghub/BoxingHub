class BoxingChatbot:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = 'start'
        self.plans = ['Basic Plan', 'Professional Plan', 'Advanced Plan']
        self.user_data = {}

    def get_response(self, user_input):
        if self.state == 'start':
            self.state = 'account_decision'
            return {
                'message': 'Welcome to Shopify! Do you want to create an account?',
                'options': ['Yes', 'No']
            }
        
        if self.state == 'account_decision':
            if user_input == 'Yes':
                self.state = 'bank_decision'
                return {
                    'message': 'Great! Please click the link to create your account: <a href="https://www.shopify.com/signup">Create Account</a><br><br>After creating your account, would you like to enter your bank details?',
                    'options': ['Yes', 'No']
                }
            elif user_input == 'No':
                self.state = 'existing_account'
                return {
                    'message': 'Do you already have a Shopify account?',
                    'options': ['Yes', 'No']
                }
            else:
                return {
                    'message': 'Please select an option:',
                    'options': ['Yes', 'No']
                }

        if self.state == 'existing_account':
            if user_input == 'Yes':
                self.state = 'bank_decision'
                return {
                    'message': 'Would you like to enter your bank details now?',
                    'options': ['Yes', 'No']
                }
            elif user_input == 'No':
                self.state = 'end'
                return {
                    'message': 'No problem! Feel free to create an account anytime at <a href="https://www.shopify.com/signup">Shopify Signup</a>. Have a great day!',
                    'options': []
                }
            else:
                return {
                    'message': 'Please select an option:',
                    'options': ['Yes', 'No']
                }

        if self.state == 'bank_decision':
            if user_input == 'Yes':
                self.state = 'plan_decision'
                return {
                    'message': 'Please click the link to enter your bank details: <a href="https://www.shopify.com/bank-details">Enter Bank Details</a><br><br>Would you like to subscribe to a plan?',
                    'options': ['Yes', 'No']
                }
            elif user_input == 'No':
                self.state = 'plan_decision'
                return {
                    'message': 'Would you like to subscribe to a plan?',
                    'options': ['Yes', 'No']
                }
            else:
                return {
                    'message': 'Please select an option:',
                    'options': ['Yes', 'No']
                }

        if self.state == 'plan_decision':
            if user_input == 'Yes':
                self.state = 'select_plan'
                return {
                    'message': 'Please select a plan:',
                    'options': self.plans
                }
            elif user_input == 'No':
                self.state = 'end'
                return {
                    'message': 'No worries! You can subscribe to a plan anytime. Thank you for visiting Shopify!',
                    'options': []
                }
            else:
                return {
                    'message': 'Please select an option:',
                    'options': ['Yes', 'No']
                }

        if self.state == 'select_plan':
            if user_input in self.plans:
                self.user_data['plan'] = user_input
                self.state = 'confirm_subscription'
                return {
                    'message': f"You have selected the **{user_input}**. Do you want to confirm your subscription?",
                    'options': ['Yes', 'No']
                }
            else:
                return {
                    'message': 'Please select a valid plan:',
                    'options': self.plans
                }

        if self.state == 'confirm_subscription':
            if user_input == 'Yes':
                self.state = 'end'
                return {
                    'message': f'Thank you! You have successfully subscribed to the **{self.user_data["plan"]}**.',
                    'options': []
                }
            elif user_input == 'No':
                self.state = 'select_plan'
                return {
                    'message': 'Please select a plan:',
                    'options': self.plans
                }
            else:
                return {
                    'message': 'Please select an option:',
                    'options': ['Yes', 'No']
                }

        if self.state == 'end':
            if user_input == 'Restart':
                self.reset()
                return {
                    'message': 'Conversation restarted. Welcome to Shopify! Do you want to create an account?',
                    'options': ['Yes', 'No']
                }
            else:
                return {
                    'message': 'Thank you for visiting Shopify. Have a great day!',
                    'options': []
                }

        # Default response for unexpected input
        return {
            'message': 'I did not understand that. Please select an option from the list.',
            'options': []
        }
