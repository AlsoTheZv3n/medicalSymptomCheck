from diseasClassifier import DiseaseClassifier

# Example usage
classifier = DiseaseClassifier()
user_input = input("Please describe your symptoms: ")
illness, likelihood = classifier.classify_illness(user_input)
print(f"Based on your symptoms, you may have {illness} with a likelihood of {likelihood:.2f}.")
