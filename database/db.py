class DBQuestionEntry():
    def __init__(self, **kwargs):
        self.param_defaults = {
            'id': 0,
            'topic': '',
            'question': '',
            'type': '',
            'subtype': ''
        }
        
        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def __repr__(self):
        return '"{0}" {{id={1} topic=\'{2}\' type=\'{3}\' subtype=\'{4}\'}}'.format(
            self.question, self.id, self.topic, self.type, self.subtype)
