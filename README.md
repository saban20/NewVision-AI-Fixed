# NewVision AI - Fixed

This repository contains a fixed version of the NewVision AI project, addressing several key compatibility issues and bugs. The original project is a system that uses augmented reality and artificial intelligence to provide accurate eye measurements and personalized eyewear recommendations.

## Issues Fixed

1. **Dependency Compatibility Issues**
   - Updated scikit-learn and TensorFlow dependencies to compatible versions
   - Fixed version conflicts between libraries
   - Created proper version pinning in requirements files

2. **Model Generation Scripts**
   - Updated model generation scripts to be compatible with current library versions
   - Fixed path and directory creation issues
   - Improved error handling

3. **Docker Configuration**
   - Enhanced Docker setup for more reliable deployment
   - Updated environment variables

4. **Testing Support**
   - Improved test scripts and mocks
   - Added better test documentation

## Project Components

- `web/` - React-based web application
- `backend/` - Python Flask backend and AI engine
- `iOS/` - Swift-based iOS application
- `shared/` - Shared libraries and utilities
- `docs/` - Documentation

## Getting Started

### Setup

1. Clone this repository
   ```
   git clone https://github.com/saban20/NewVision-AI-Fixed.git
   cd NewVision-AI-Fixed
   ```

2. Use the compatible requirements file
   ```bash
   cd backend
   pip install -r requirements-compatible.txt
   ```

3. Generate test models
   ```bash
   python generate_models_compatible.py
   ```

4. Start the backend
   ```bash
   python app.py
   ```

5. In a separate terminal, start the frontend
   ```bash
   cd ../web
   npm install
   npm start
   ```

## Key Improvements

- All dependencies are now compatible with modern macOS and Linux systems
- TensorFlow and scikit-learn versions are properly aligned
- Model generation produces models compatible with the libraries used
- Better error handling for missing models and data files

See the [CHANGES.md](CHANGES.md) file for a complete list of changes and improvements.

## Original Project

This is an improved version of the original NewVision AI project, addressing compatibility and functionality issues while maintaining the original features and goals of the system.