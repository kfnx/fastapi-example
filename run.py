#!/usr/bin/env python3
"""
FastAPI Ext - Startup Script
"""
import uvicorn
from app.database import create_db_and_tables

def main():
    """Initialize database and start the FastAPI server"""
    print("Creating database tables...")
    create_db_and_tables()
    print("Database tables created successfully!")
    
    print("Starting FastAPI server...")
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main() 