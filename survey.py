class AnonymoussSurvey():
    """Collect anonymous answers to a survey question."""
    
    
    def __init__(self, question):
        """Store a question, and prepare to store response."""
        self.question = question
        self.responses = []
        
        
    def show_question(self):
        """Show the survey question."""
        print(question)
        
        
    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_responses)
        
        
    def show_results(self):
        """Show all responses that have beeen given."""
        print("Survey results:")
        for response in responses:
            print('- ' + response