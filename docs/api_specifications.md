# API Specifications

This document outlines the API endpoints and communication flow for the ResultFlow application with Streamlit frontend.

## Integration Approaches

With Streamlit as our frontend, we have two main approaches for API integration:

1. **Direct Function Calls**: Streamlit can directly call Python functions, reducing the need for API endpoints in many cases
2. **FastAPI Backend**: For operations requiring background processing or separate services

## Base URLs

- **Backend API**: `/api/v1`
- **Admin API**: `/api/v1/admin`
- **Customer API**: `/api/v1/customer`
- **Auth API**: `/api/v1/auth`

## Authentication

### Admin Authentication

- **Streamlit-Authenticator** for the admin interface
- Session-based authentication
- Token lifetime: 24 hours

While using Streamlit, we can use the streamlit-authenticator package directly in the frontend. For API access:

```
POST /api/v1/auth/login
POST /api/v1/auth/refresh
POST /api/v1/auth/logout
```

### Customer Authentication

- **URL parameter token + password form**
- Token lifetime: 24 hours
- No refresh mechanism (security feature)

With Streamlit, we'll validate the token directly in the app:

```
GET /customer?token=<access_token>  # Streamlit app URL with token
```

Then validate via API:
```
POST /api/v1/customer/validate_token
```

## Admin API Endpoints

### Batch Management

```
GET    /api/v1/admin/batches                   # List all batches
POST   /api/v1/admin/batches                   # Create new batch
GET    /api/v1/admin/batches/{batch_id}        # Get batch details
DELETE /api/v1/admin/batches/{batch_id}        # Delete batch
```

#### Create Batch Request
```json
{
  "name": "string",
  "description": "string",
  "template_id": "string"
}
```

#### Create Batch Response
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "template_id": "string",
  "status": "pending",
  "created_at": "datetime",
  "upload_url": "string"  // Presigned URL for Excel upload
}
```

### File Upload

```
POST   /api/v1/admin/upload/excel              # Upload Excel file
POST   /api/v1/admin/upload/template           # Upload Word template
```

### Template Management

```
GET    /api/v1/admin/templates                  # List all templates
POST   /api/v1/admin/templates                  # Create new template
GET    /api/v1/admin/templates/{template_id}    # Get template details
PUT    /api/v1/admin/templates/{template_id}    # Update template
DELETE /api/v1/admin/templates/{template_id}    # Delete template
```

### Report Management

```
GET    /api/v1/admin/reports                   # List all reports
GET    /api/v1/admin/reports/{report_id}       # Get report details
PUT    /api/v1/admin/reports/{report_id}       # Update report
DELETE /api/v1/admin/reports/{report_id}       # Delete report
GET    /api/v1/admin/reports/{report_id}/pdf   # Get PDF file
```

### Delivery Management

```
POST   /api/v1/admin/reports/{report_id}/send  # Send report to customer
GET    /api/v1/admin/delivery/status           # Get delivery statistics
```

#### Send Report Request
```json
{
  "customer_phone": "string",
  "custom_message": "string",
  "schedule_time": "datetime" // Optional
}
```

### Dashboard Data

```
GET    /api/v1/admin/dashboard/summary         # Get dashboard summary
GET    /api/v1/admin/dashboard/activity        # Get recent activity
```

## Customer API Endpoints

### Authentication

```
POST   /api/v1/customer/authenticate          # Verify access token and password
```

#### Authenticate Request
```json
{
  "token": "string",
  "password": "string"
}
```

### Report Access

```
GET    /api/v1/customer/report                # Get report details (authenticated)
GET    /api/v1/customer/report/pdf            # Get PDF file (authenticated)
POST   /api/v1/customer/report/download       # Record download event
```

## Pipeline Status Webhooks

### SMS Provider Callback

```
POST   /api/v1/webhooks/sms/status            # SMS delivery status updates
```

### Batch Processing Status

```
GET    /api/v1/admin/batches/{batch_id}/status # Get processing status
```

#### Batch Status Response
```json
{
  "id": "string",
  "status": "string",
  "progress": {
    "total": 0,
    "processed": 0,
    "successful": 0,
    "failed": 0
  },
  "started_at": "datetime",
  "updated_at": "datetime",
  "estimated_completion": "datetime"
}
```

## Error Responses

Standard error format:

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": {}
  }
}
```

### Common Error Codes

- `auth_required`: Authentication required
- `invalid_credentials`: Invalid credentials
- `token_expired`: Access token expired
- `not_found`: Resource not found
- `validation_error`: Request validation failed
- `internal_error`: Server error
- `rate_limited`: Too many requests

## Rate Limiting

- Admin API: 100 requests per minute per user
- Customer API: 20 requests per minute per token
- Authentication endpoints: 5 requests per minute per IP

## API Versioning

APIs are versioned in the URL path (e.g., `/api/v1/`). When breaking changes are introduced, a new version will be created.

## Streamlit Session State Updates

Instead of WebSockets, Streamlit uses session state and periodic refreshes for updates:

```python
# In Streamlit app
if st.session_state.get('refresh_dashboard', False):
    status_data = get_status_data()  # API call
    st.session_state.status_data = status_data
```

API endpoints for status updates:
```
GET /api/v1/admin/status/batch/{batch_id}
GET /api/v1/admin/status/delivery
GET /api/v1/admin/status/reports
```

Streamlit will poll these endpoints periodically to update the UI.
