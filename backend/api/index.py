"""
Vercel serverless function entry point for Flask app.
This file is required for Vercel to properly deploy the Flask backend.
"""
import sys
import os

# Get the absolute path to the backend directory
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add backend directory to Python path
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Add Chart-Generation-using-LLMs directory to path
chart_gen_dir = os.path.join(backend_dir, "Chart-Generation-using-LLMs")
if chart_gen_dir not in sys.path:
    sys.path.insert(0, chart_gen_dir)

# Import the Flask app
from app import app

# This is the WSGI handler for Vercel
handler = app
