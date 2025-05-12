# Project Structure

The ResultFlow project follows a modular structure for maintainability and separation of concerns.

```
/ResultFlow
├── app/                    # Application code
│   ├── api/                # API endpoints
│   │   ├── admin.py        # Admin API routes
│   │   ├── auth.py         # Authentication routes
│   │   ├── customer.py     # Customer API routes
│   │   └── deps.py         # Dependencies (auth, db)
│   ├── core/               # Core functionality
│   │   ├── config.py       # Configuration settings
│   │   ├── security.py     # Security utilities
│   │   └── logging.py      # Logging setup
│   ├── db/                 # Database models and utilities
│   │   ├── mongo.py        # MongoDB connection
│   │   └── models.py       # Data models
│   ├── pipeline/           # Data processing pipeline
│   │   ├── excel.py        # Excel processing
│   │   ├── template.py     # Word template processing
│   │   ├── pdf.py          # PDF conversion
│   │   └── tasks.py        # Celery tasks
│   ├── services/           # Business logic
│   │   ├── report.py       # Report generation
│   │   ├── storage.py      # File storage
│   │   ├── notification.py # SMS notification
│   │   └── access.py       # Access control
│   └── schemas/            # Pydantic schemas
│       ├── report.py       # Report schemas
│       ├── user.py         # User schemas
│       └── template.py     # Template schemas
├── frontend/               # Frontend code
│   ├── admin/              # Admin UI
│   │   ├── app.py          # Main Streamlit application
│   │   ├── pages/          # Streamlit multi-page app
│   │   │   ├── dashboard.py    # Dashboard page
│   │   │   ├── batch_management.py # Batch management
│   │   │   ├── templates.py   # Template management
│   │   │   └── settings.py    # Settings page
│   │   ├── components/     # Reusable UI components
│   │   ├── utils/          # Utility functions
│   │   └── assets/         # Static assets
│   └── customer/           # Customer UI
│       ├── app.py          # Main customer application
│       ├── components/     # Reusable UI components
│       ├── utils/          # Utility functions
│       └── assets/         # Static assets
├── data/                   # Data directory
│   ├── samples/            # Sample data for testing
│   │   ├── sources/        # Source Excel files
│   │   └── templates/      # Word templates
│   └── temp/               # Temporary storage
├── tests/                  # Test suite
│   ├── api/                # API tests
│   ├── pipeline/           # Pipeline tests
│   └── services/           # Service tests
├── docs/                   # Documentation
├── scripts/                # Utility scripts
├── docker/                 # Docker configuration
│   ├── api/                # API Dockerfile
│   ├── worker/             # Worker Dockerfile
│   ├── nginx/              # Nginx configuration
│   └── mongodb/            # MongoDB configuration
├── docker-compose.yml      # Docker Compose configuration
├── .env.example            # Example environment variables
├── .gitignore              # Git ignore file
├── pyproject.toml          # Python package configuration
├── README.md               # Project README
└── main.py                 # Application entry point
```

## Key Modules

### Backend Modules

1. **API Layer**: Handles HTTP requests and responses
   - Admin API: Management operations for administrators
   - Customer API: Access operations for customers
   - Auth: Authentication and authorization

2. **Pipeline Module**: Core data processing engine
   - Excel processor: Reads and validates Excel input
   - Template processor: Maps data to Word templates
   - PDF converter: Converts documents to final PDF format

3. **Service Layer**: Business logic implementation
   - Report service: Manages report generation
   - Storage service: Handles file storage operations
   - Notification service: Manages SMS notifications

4. **Database Layer**: Data persistence
   - MongoDB connection: Manages database operations
   - Models: Defines data structures

### Frontend Modules

1. **Admin Portal (Streamlit)**
   - Dashboard: Visual representation of pipeline status using Plotly charts
   - Upload interface: Streamlit file uploaders for Excel files and templates
   - Preview component: PDF preview using Streamlit's components
   - Management tables: Interactive tables using Streamlit-AgGrid

2. **Customer Portal (Streamlit)**
   - Authentication: Secure access validation using Streamlit-Authenticator
   - Report viewer: PDF viewing interface with Streamlit components
   - Download functionality: For local copies via Streamlit download buttons

## Implementation Order

When implementing the project, we recommend the following order:

1. Set up project structure and dependencies
2. Implement core pipeline functionality
3. Develop database models and storage
4. Implement API endpoints
5. Build admin frontend
6. Implement notification service
7. Build customer frontend
8. Set up deployment and monitoring
