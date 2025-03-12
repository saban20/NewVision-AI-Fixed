#!/bin/bash

# NewVision AI Fixed - Setup and Run Script
# This script helps set up and run the NewVision AI application with all fixes applied

# Bold and color output
BOLD="\033[1m"
GREEN="\033[0;32m"
RED="\033[0;31m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"
NC="\033[0m" # No Color

# Function to print section headers
print_header() {
    echo -e "\n${BOLD}${BLUE}=== $1 ===${NC}\n"
}

# Function to print success messages
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

# Function to print error messages
print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Function to print warning messages
print_warning() {
    echo -e "${YELLOW}! $1${NC}"
}

# Check for Python and version
check_python() {
    print_header "Checking Python"
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        print_error "Python not found. Please install Python 3.8 or higher."
        exit 1
    fi
    
    PYTHON_VERSION=$($PYTHON_CMD -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
    print_success "Found Python version $PYTHON_VERSION"
    
    if [[ $(echo "$PYTHON_VERSION < 3.8" | bc) -eq 1 ]]; then
        print_warning "Python version is below 3.8. Some features may not work correctly."
    fi
}

# Set up virtual environment
setup_venv() {
    print_header "Setting up Python Virtual Environment"
    
    if [ -d "venv" ]; then
        print_warning "Virtual environment already exists."
        read -p "Do you want to recreate it? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf venv
            print_success "Removed existing virtual environment."
        else
            print_warning "Skipping virtual environment creation."
            return
        fi
    fi
    
    $PYTHON_CMD -m venv venv
    print_success "Created virtual environment."
    
    if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
        source venv/bin/activate
    else
        source venv/Scripts/activate
    fi
    print_success "Activated virtual environment."
}

# Install backend dependencies
install_backend_deps() {
    print_header "Installing Backend Dependencies"
    
    cd backend
    if [ ! -f "requirements-compatible.txt" ]; then
        print_error "requirements-compatible.txt not found."
        exit 1
    fi
    
    pip install --upgrade pip
    print_success "Upgraded pip."
    
    pip install -r requirements-compatible.txt
    if [ $? -eq 0 ]; then
        print_success "Installed backend dependencies."
    else
        print_error "Failed to install backend dependencies."
        exit 1
    fi
    cd ..
}

# Generate model files
generate_models() {
    print_header "Generating Model Files"
    
    cd backend
    if [ ! -f "generate_models_compatible.py" ]; then
        print_error "generate_models_compatible.py not found."
        exit 1
    fi
    
    $PYTHON_CMD generate_models_compatible.py
    if [ $? -eq 0 ]; then
        print_success "Generated model files."
    else
        print_error "Failed to generate model files."
        exit 1
    fi
    cd ..
}

# Install frontend dependencies
install_frontend_deps() {
    print_header "Installing Frontend Dependencies"
    
    if ! command -v npm &> /dev/null; then
        print_error "npm not found. Please install Node.js and npm."
        exit 1
    fi
    
    cd web
    npm install
    if [ $? -eq 0 ]; then
        print_success "Installed frontend dependencies."
    else
        print_error "Failed to install frontend dependencies."
        exit 1
    fi
    cd ..
}

# Run the application (both backend and frontend)
run_app() {
    print_header "Running NewVision AI"
    
    # Check if Docker is available and preferred
    if command -v docker &> /dev/null && command -v docker-compose &> /dev/null; then
        print_warning "Docker detected. Would you like to run using Docker? (Recommended)"
        read -p "Run with Docker? (y/n) " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_success "Starting with Docker Compose..."
            docker-compose up
            return
        fi
    fi
    
    # Run without Docker (development mode)
    print_warning "Running in development mode (without Docker)."
    print_warning "You'll need to open two terminal windows."
    print_warning "Press Ctrl+C to stop the backend when done."
    
    # Activate virtual environment
    if [[ "$OSTYPE" == "darwin"* ]] || [[ "$OSTYPE" == "linux-gnu"* ]]; then
        source venv/bin/activate
    else
        source venv/Scripts/activate
    fi
    
    # Start backend
    cd backend
    print_success "Starting backend server..."
    $PYTHON_CMD app.py
}

# Main function
main() {
    print_header "NewVision AI Setup and Run"
    echo "This script will help you set up and run the fixed NewVision AI application."
    
    check_python
    setup_venv
    install_backend_deps
    generate_models
    install_frontend_deps
    run_app
}

# Execute main function
main