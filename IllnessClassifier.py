class IllnessClassifier:
    def __init__(self):
        self.illnesses = {
            'coughing': ['pneumonia'],
            'fever': ['pneumonia', 'cold'],
            'shortness of breath': ['pneumonia', 'asthma', 'bronchitis'],
            'chest pain': ['pneumonia', 'asthma'],
            'fatigue': ['pneumonia', 'cold', 'asthma', 'irritable bowel disease', 'influenza', 'bronchitis', 'sinusitis', 'depression'],
            'sore throat': ['cold', 'asthma', 'sinusitis'],
            'runny nose': ['cold', 'sinusitis'],
            'sneezing': ['cold'],
            'headache': ['cold', 'asthma', 'influenza', 'sinusitis'],
            'diarrhea': ['irritable bowel disease'],
            'stomach pain': ['irritable bowel disease'],
            'anima': ['irritable bowel disease'],
            'Fever': ['influenza'],
            'Body aches': ['influenza'],
            'Chills': ['influenza'],
            'Sore throat': ['influenza'],
            'Persistent cough (with or without phlegm)': ['bronchitis'],
            'Mild fever and chills': ['bronchitis'],
            'Chest discomfort': ['bronchitis'],
            'Nasal congestion': ['sinusitis'],
            'Facial pain or pressure': ['sinusitis'],
            'Thick, discolored nasal discharge': ['sinusitis'],
            'Postnasal drip': ['sinusitis'],
            'Sadness': ['depression'],
            'lack of motivation': ['depression'],
            'deserialization': ['depression'],
            'anxiety': ['depression']
        }

    def get_symptoms_by_illness(self, illness):
        return self.illnesses.get(illness, [])

    def get_all_illnesses(self):
        return list(self.illnesses.keys())