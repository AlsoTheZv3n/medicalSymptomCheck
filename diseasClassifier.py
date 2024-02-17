from IllnessClassifier import IllnessClassifier


class DiseaseClassifier:
    def __init__(self):
        # Instantiate the SymptomClassifier
        self.symptom_classifier = IllnessClassifier()

    def classify_illness(self, user_input):
        user_input_lower = user_input.lower()
        likelihoods = {}

        # Check user input for symptoms
        for symptom, diseases in self.symptom_classifier.illnesses.items():
            if symptom in user_input_lower:
                # Update likelihoods for each disease associated with the symptom
                for disease in diseases:
                    if disease not in likelihoods:
                        likelihoods[disease] = 0
                    likelihoods[disease] += 1

        # Calculate likelihoods based on the number of matching symptoms
        if likelihoods:
            total_symptoms = len(self.symptom_classifier.illnesses())
            illness_likelihoods = {disease: count / total_symptoms for disease, count in likelihoods.items()}
            return illness_likelihoods
        else:
            return {"No illness detected": 0}
