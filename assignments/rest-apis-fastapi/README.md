# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build scalable REST APIs using the FastAPI framework. Gain hands-on experience with HTTP methods, request/response handling, data validation, and interactive API documentation.

## 📝 Tasks

### 🛠️ Create a Basic API with FastAPI

#### Description
Set up a FastAPI application with multiple endpoints that accept different HTTP methods (GET, POST, PUT, DELETE). Implement request/response models using Pydantic for data validation and automatic documentation.

#### Requirements
Completed program should:

- Import and initialize a FastAPI application
- Create at least 4 endpoints (GET, POST, PUT, DELETE) following REST conventions
- Use Pydantic models to define request/response schemas with data validation
- Implement proper status codes for different scenarios (200, 201, 404, 400)
- Include path parameters, query parameters, and request body handling
- Provide example data in endpoint documentation using Pydantic field examples
- Serve the API on `http://localhost:8000` with automatic OpenAPI (Swagger) documentation accessible at `/docs`

### 🛠️ Implement Error Handling and Validation

#### Description
Add robust error handling to your API endpoints, including custom exception handlers, input validation, and meaningful error messages.

#### Requirements
Completed program should:

- Validate incoming data using Pydantic models with custom validation rules
- Handle edge cases (e.g., item not found, invalid input) with appropriate HTTP status codes and error messages
- Implement at least one custom exception handler for specific error scenarios
- Return JSON error responses with descriptive messages and status codes
- Test endpoints with invalid inputs and verify error handling works correctly

### 🛠️ Test and Document Your API

#### Description
Create tests for your API endpoints and verify they work correctly with different inputs and edge cases.

#### Requirements
Completed program should:

- Use the FastAPI test client (`TestClient`) to write unit tests for at least 4 endpoints
- Test successful requests and expected responses
- Test error cases (e.g., invalid input, missing resources) and verify appropriate status codes and error messages
- Include tests for different HTTP methods (GET, POST, PUT, DELETE)
- Verify that auto-generated API documentation is accessible and complete
