#!/usr/bin/env python
"""
Compatible Model Generation Script for NewVision AI

This script generates machine learning models required for the NewVision AI backend
that are compatible with scikit-learn 1.2.2 and TensorFlow 2.13+.
"""

import os
import sys
import numpy as np
import joblib
import tensorflow as tf
from pathlib import Path

# Try importing scikit-learn components and check version
try:
    import sklearn
    from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import DBSCAN
    from sklearn.neighbors import NearestNeighbors
    from sklearn.decomposition import PCA
    
    print(f"Using scikit-learn version: {sklearn.__version__}")
    
    # Check for compatible version
    if sklearn.__version__ < "1.2.0" or sklearn.__version__ >= "1.3.0":
        print("Warning: This script is optimized for scikit-learn 1.2.x.")
        print("You're using version", sklearn.__version__)
        print("Some models may not be compatible. Consider installing scikit-learn 1.2.2")
except ImportError:
    print("Error: scikit-learn is not installed. Please install it with:")
    print("pip install scikit-learn==1.2.2")
    sys.exit(1)

# Check TensorFlow version
print(f"Using TensorFlow version: {tf.__version__}")
if tf.__version__ < "2.13.0":
    print("Warning: This script is optimized for TensorFlow 2.13+.")
    print("You're using version", tf.__version__)
    print("Models may not be compatible. Consider updating TensorFlow.")

def create_directory(directory_path):
    """Create directory if it doesn't exist."""
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Created directory: {directory_path}")
    except Exception as e:
        print(f"Error creating directory {directory_path}: {e}")
        sys.exit(1)

def generate_eye_measurement_models():
    """Generate models for eye measurement analysis compatible with scikit-learn 1.2.2."""
    print("Generating eye measurement models...")
    
    # Create directory for eye measurement models
    model_dir = Path('data/models')
    create_directory(model_dir)
    
    try:
        # Generate PD (Pupillary Distance) Regressor
        # Using a simpler model with fewer features for compatibility
        pd_regressor = RandomForestRegressor(n_estimators=5, max_depth=3, random_state=42)
        # Fit with dummy data
        X = np.random.rand(50, 5)
        y = np.random.rand(50) * 20 + 50  # Random PD values between 50-70mm
        pd_regressor.fit(X, y)
        
        # Save the model with compatible protocol
        joblib.dump(pd_regressor, model_dir / 'pd_regressor.joblib', compress=3)
        print("Generated pd_regressor.joblib")
        
        # Generate Fitting Classifier
        fitting_classifier = RandomForestClassifier(n_estimators=5, max_depth=3, random_state=42)
        # Fit with dummy data
        X = np.random.rand(50, 5)
        y = np.random.randint(0, 3, 50)  # Random class labels 0, 1, 2
        fitting_classifier.fit(X, y)
        
        # Save the model with compatible protocol
        joblib.dump(fitting_classifier, model_dir / 'fitting_classifier.joblib', compress=3)
        print("Generated fitting_classifier.joblib")
        
        # Generate Anomaly Detector using DBSCAN instead of LOF for better compatibility
        anomaly_detector = DBSCAN(eps=0.5, min_samples=5)
        # Fit with dummy data
        X = np.random.rand(50, 5)
        anomaly_detector.fit(X)
        
        # Save the model with compatible protocol
        joblib.dump(anomaly_detector, model_dir / 'anomaly_detector.joblib', compress=3)
        print("Generated anomaly_detector.joblib")
        
        # Generate Feature Scaler
        feature_scaler = StandardScaler()
        # Fit with dummy data
        X = np.random.rand(50, 5)
        feature_scaler.fit(X)
        
        # Save the model with compatible protocol
        joblib.dump(feature_scaler, model_dir / 'feature_scaler.joblib', compress=3)
        print("Generated feature_scaler.joblib")
        
        # Generate Neural Network Model compatible with TF 2.13+
        nn_model_dir = model_dir / 'neural_network_model'
        create_directory(nn_model_dir)
        
        # Create a simple neural network compatible with current TF version
        nn_model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=(5,)),
            tf.keras.layers.Dense(6, activation='relu'),
            tf.keras.layers.Dense(3, activation='relu'),
            tf.keras.layers.Dense(1)
        ])
        
        nn_model.compile(optimizer='adam', loss='mse')
        
        # Fit with dummy data
        X = np.random.rand(50, 5)
        y = np.random.rand(50)
        nn_model.fit(X, y, epochs=2, verbose=1)
        
        # Save the model in SavedModel format (most compatible)
        nn_model.save(nn_model_dir)
        print(f"Generated neural network model in {nn_model_dir}")
    
    except Exception as e:
        print(f"Error generating eye measurement models: {e}")
        print("Please check your scikit-learn and TensorFlow versions.")
        sys.exit(1)

def generate_product_recommendation_models():
    """Generate models for product recommendation compatible with scikit-learn 1.2.2."""
    print("Generating product recommendation models...")
    
    # Create directory for recommendation models
    model_dir = Path('models/trained_models')
    create_directory(model_dir)
    
    try:
        # Generate content-based model
        content_model = NearestNeighbors(n_neighbors=5, algorithm='auto')
        # Fit with dummy data
        X = np.random.rand(30, 3)
        content_model.fit(X)
        
        # Save the model with compatible protocol
        joblib.dump(content_model, model_dir / 'content_model.joblib', compress=3)
        print("Generated content_model.joblib")
        
        # Generate feature scaler
        feature_scaler = StandardScaler()
        # Fit with dummy data
        X = np.random.rand(30, 3)
        feature_scaler.fit(X)
        
        # Save the model with compatible protocol
        joblib.dump(feature_scaler, model_dir / 'feature_scaler.joblib', compress=3)
        print("Generated feature_scaler.joblib for recommendation model")
        
        # Generate PCA model
        pca = PCA(n_components=2)
        # Fit with dummy data
        X = np.random.rand(30, 3)
        pca.fit(X)
        
        # Save the model with compatible protocol
        joblib.dump(pca, model_dir / 'pca_model.joblib', compress=3)
        print("Generated pca_model.joblib")
    
    except Exception as e:
        print(f"Error generating product recommendation models: {e}")
        print("Please check your scikit-learn version.")
        sys.exit(1)

def main():
    """Main function to generate all models."""
    print("Starting compatible model generation for NewVision AI...")
    
    # Check for data directory
    if not os.path.exists('data'):
        create_directory('data')
    
    # Check for models directory
    if not os.path.exists('models'):
        create_directory('models')
        create_directory('models/trained_models')
    
    generate_eye_measurement_models()
    generate_product_recommendation_models()
    print("Compatible model generation complete!")

if __name__ == "__main__":
    main()