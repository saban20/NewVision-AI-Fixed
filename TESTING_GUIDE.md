# NewVision AI Testing Guide

This document provides comprehensive instructions for testing the NewVision AI application with the fixed dependencies and model generation scripts.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup for Testing](#setup-for-testing)
3. [Model Generation](#model-generation)
4. [Backend Testing](#backend-testing)
5. [Frontend Testing](#frontend-testing)
6. [Integration Testing](#integration-testing)
7. [Common Issues and Solutions](#common-issues-and-solutions)

## Prerequisites

Before beginning testing, ensure you have:

- **Python Environment**: Python 3.9+ is recommended (3.8 minimum)
- **Node.js**: Version 14+ for frontend testing
- **Git**: For version control and fetching the latest code
- **Virtual Environment**: For isolated Python dependency installation
- **macOS Compatibility**: For macOS users, especially with Apple Silicon, use the compatibility fixes

## Setup for Testing

### Clone the Repository

```bash
git clone https://github.com/saban20/NewVision-AI-Fixed.git
cd NewVision-AI-Fixed
```

### Python Environment Setup

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install compatible dependencies
pip install -r backend/requirements-compatible.txt
```

### Frontend Setup

```bash
# Navigate to the web directory
cd web

# Install dependencies
npm install
```

## Model Generation

### Generate Compatible ML Models

The updated script generates models compatible with scikit-learn 1.2.2 and TensorFlow 2.13+:

```bash
# Navigate to the backend directory
cd backend

# Run the compatible model generation script
python generate_models_compatible.py
```

This script will:
1. Check for compatible scikit-learn and TensorFlow versions
2. Create necessary directories if they don't exist
3. Generate test models for eye measurements
4. Generate test models for product recommendations
5. Save all models in formats compatible with current versions

### Verification

Verify that the following model files were created:

- `data/models/pd_regressor.joblib`
- `data/models/fitting_classifier.joblib`
- `data/models/anomaly_detector.joblib`
- `data/models/feature_scaler.joblib`
- `data/models/neural_network_model/` (directory containing TensorFlow model)
- `models/trained_models/content_model.joblib`
- `models/trained_models/feature_scaler.joblib`
- `models/trained_models/pca_model.joblib`

## Backend Testing

### Unit Tests

```bash
# Navigate to the backend directory
cd backend

# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests/test_api.py
```

### API Tests with Model Mocks

If you want to test the API without generating real models:

```bash
# Run tests with mocked models
python -m unittest tests/test_api_mocks.py
```

### Running the Backend Server

```bash
# Start the Flask backend
python app.py
```

The server should start without errors, and you should see a message indicating it's running at `http://localhost:5000`.

## Frontend Testing

### Unit Tests

```bash
# Navigate to the web directory
cd web

# Run React tests
npm test
```

### Running the Frontend Dev Server

```bash
# Start the React development server
npm start
```

The frontend should open in your browser at `http://localhost:3000`.

## Integration Testing

For full integration testing, you need both the backend and frontend running:

```bash
# Terminal 1: Start the backend
cd backend
python app.py

# Terminal 2: Start the frontend
cd web
npm start
```

### Testing Flow

1. Open the web app in your browser
2. Upload a test image of a face
3. Verify measurements are calculated
4. Test recommendation features
5. Test user account features if applicable

## Common Issues and Solutions

### Model Loading Errors

**Issue**: `ImportError` or errors about incompatible models

**Solution**:
- Ensure you've generated models using the compatible script
- Verify scikit-learn version is 1.2.2
- Check TensorFlow version is 2.13+

### TensorFlow GPU Issues

**Issue**: TensorFlow GPU errors

**Solution**:
- Use the CPU version of TensorFlow on the compatible requirements
- If GPU is needed, ensure CUDA and cuDNN versions match TensorFlow requirements

### Dependency Conflicts

**Issue**: Dependency version conflicts or incompatibilities

**Solution**:
- Use fresh virtual environment
- Use the `requirements-compatible.txt` file
- For specific conflicts, try pinning problematic packages to known working versions

### macOS Apple Silicon Issues

**Issue**: Problems with TensorFlow on Apple Silicon (M1/M2/M3)

**Solution**:
- Use TensorFlow 2.13+ which has better Apple Silicon support
- Install Apple's ML Python packages if needed: `pip install tensorflow-macos tensorflow-metal`

### CORS Issues

**Issue**: Frontend can't connect to backend due to CORS

**Solution**:
- Ensure backend has CORS properly configured
- Check the frontend is using the correct API URL
- Verify the browser isn't blocking requests

### Missing Files or Directories

**Issue**: Scripts complain about missing directories

**Solution**:
- The updated script creates needed directories automatically
- Manually create any missing directories if needed

## Next Steps

After successful testing, you can:

1. Deploy the backend to a production server
2. Deploy the frontend to a web server or hosting service
3. Set up continuous integration for automated testing
4. Configure production settings in environment variables

For more detailed information on deployment, refer to the README.md file.

---

If you encounter any issues not covered in this guide, please open an issue on the GitHub repository.