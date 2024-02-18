import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import joblib

class RecommendationModel:
    def __init__(self, data_path, model_filename, specialist_dataset_filename, general_physician_dataset_filename):
        # Load the appointment data from the CSV file
        self.data = pd.read_csv(data_path)

        # Preprocess data and build TF-IDF vectors
        self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.compute_tfidf_matrix()

        # Compute cosine similarity between appointments
        self.cosine_sim = linear_kernel(self.tfidf_matrix, self.tfidf_matrix)

        # Load the trained model
        self.model = joblib.load(model_filename)

        # Load the dataset from a CSV file for specialists
        self.specialist_dataset = pd.read_csv(specialist_dataset_filename)
        
        # Create the condition-to-index mapping for specialists
        self.specialist_condition_to_index = {condition: index for index, condition in enumerate(self.specialist_dataset['Condition'])}
        
        # Create the list of specialist doctors
        self.specialist_doctors = self.specialist_dataset['Doctor'].tolist()

        # Load the dataset from a CSV file for general physicians
        self.general_physician_dataset = pd.read_csv(general_physician_dataset_filename)
        
        # Create the condition-to-index mapping for general physicians
        self.general_physician_condition_to_index = {condition: index for index, condition in enumerate(self.general_physician_dataset['Condition'])}
        
        # Create the list of general physicians
        self.general_physician_doctors = self.general_physician_dataset['Doctor'].tolist()

    def compute_tfidf_matrix(self):
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        return tfidf_vectorizer.fit_transform(self.data['medical_condition'])

    def get_recommendations(self, appointment_index, num_recommendations=5):
        # Get the pairwise similarity scores of all appointments with the specified appointment
        sim_scores = list(enumerate(self.cosine_sim[appointment_index]))

        # Sort the appointments based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the top-n most similar appointments
        sim_scores = sim_scores[1:num_recommendations + 1]

        # Get the appointment indices
        appointment_indices = [x[0] for x in sim_scores]

        # Return the top-n most similar appointments
        return appointment_indices

    def recommend_doctor(self, patient_condition):
        # Check if the condition exists in the mapping for specialists
        if patient_condition in self.specialist_condition_to_index:
            condition_index = self.specialist_condition_to_index[patient_condition]
            if 0 <= condition_index < len(self.specialist_doctors):
                recommended_doctor = self.specialist_doctors[condition_index]
                return recommended_doctor
            else:
                return "Invalid condition index"
        else:
            # Check if the condition exists in the mapping for general physicians
            if patient_condition in self.general_physician_condition_to_index:
                condition_index = self.general_physician_condition_to_index[patient_condition]
                if 0 <= condition_index < len(self.general_physician_doctors):
                    recommended_doctor = self.general_physician_doctors[condition_index]
                    return recommended_doctor
                else:
                    return "Invalid condition index for general physicians"
            else:
                # If condition is not recognized for both specialists and general physicians, recommend a default general physician
                default_general_physician = self.general_physician_doctors[0]  # Assuming the first entry is the default general physician
                return default_general_physician

if __name__ == "__main__":
    data_path = "recommend/data/input/appointments.csv"  # Replace with the path to your dataset
    model_filename = 'recommend/data/output/model.pkl'  # Replace with the actual filename
    specialist_dataset_filename = 'recommend/data/input/specialist.csv'  # Replace with the actual file path
    general_physician_dataset_filename = 'recommend/data/input/general.csv'  # Replace with the actual file path

    model = RecommendationModel(data_path, model_filename, specialist_dataset_filename, general_physician_dataset_filename)

    # Example: Get recommendations for a specific appointment index
    appointment_index = 5  # Replace with the index of the appointment you want recommendations for
    recommendations = model.get_recommendations(appointment_index)
    print(f"Recommendations for appointment at index {appointment_index}:")
    for recommendation_index in recommendations:
        print(f"Recommended appointment at index {recommendation_index}")

    # Example: Get doctor recommendation based on user input for patient's condition
    patient_condition = input("Enter patient's condition: ")
    recommended_doctor = model.recommend_doctor(patient_condition)
    print(f"Recommended Doctor for '{patient_condition}': {recommended_doctor}")
