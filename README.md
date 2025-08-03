# FastAPI example

uv
alembic
sqlite
pydantic
scalar

### Build Images
```bash
# Development
docker build -t fastapi-notes:dev .

# Production
docker build -f Dockerfile.prod -t fastapi-notes:prod .
```

### Run Containers
```bash
# Development
docker run -p 8000:8000 fastapi-notes:dev

# Production
docker run -p 8000:8000 --env-file .env fastapi-notes:prod
```

## 📚 API Endpoints

- `GET /health` - Health check
- `GET /notes` - List all notes
- `POST /notes` - Create a note
- `GET /notes/{id}` - Get a specific note
- `PUT /notes/{id}` - Update a note
- `DELETE /notes/{id}` - Delete a note
- `GET /docs` - Swagger documentation
- `GET /scalar` - Scalar documentation 