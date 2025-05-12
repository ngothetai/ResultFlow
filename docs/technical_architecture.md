# Technical Architecture

## Technology Stack

### Backend
- **Python 3.9+**: Core programming language
- **FastAPI**: High-performance web framework for building APIs
- **Celery**: Distributed task queue for managing the pipeline steps
- **Redis**: Message broker for Celery and caching
- **MongoDB**: NoSQL database for storing documents and results
- **Pandas**: Data manipulation for Excel processing
- **docxtpl**: Word document templating
- **PyJWT**: For secure token generation for customer access links

### Frontend
- **Streamlit**: Python framework for creating interactive web applications
- **Plotly**: Interactive data visualization for admin dashboard
- **PyPDF2/pdf2image**: PDF processing and preview
- **Streamlit-Authenticator**: Authentication component for Streamlit
- **Streamlit-Extras**: Additional UI components and utilities
- **Streamlit-Aggrid**: Advanced interactive tables

### DevOps
- **Docker**: Containerization
- **Docker Compose**: Multi-container application orchestration
- **Nginx**: Web server and reverse proxy

## System Architecture

```
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│   Data Processing   │     │   Storage Layer     │     │   Delivery Layer    │
│                     │     │                     │     │                     │
│  ┌───────────────┐  │     │  ┌───────────────┐  │     │  ┌───────────────┐  │
│  │ Excel Parser  │  │     │  │               │  │     │  │  SMS Gateway  │  │
│  └───────┬───────┘  │     │  │    MongoDB    │  │     │  │   Integration │  │
│          │          │     │  │               │  │     │  └───────────────┘  │
│  ┌───────▼───────┐  │     │  │               │  │     │                     │
│  │ Word Template │  │     │  │               │  │     │  ┌───────────────┐  │
│  │  Processor    │──┼────►│  │               │──┼────►│  │ Access Token  │  │
│  └───────┬───────┘  │     │  │               │  │     │  │  Generator    │  │
│          │          │     │  │               │  │     │  └───────────────┘  │
│  ┌───────▼───────┐  │     │  │               │  │     │                     │
│  │  PDF Export   │  │     │  │               │  │     │                     │
│  └───────────────┘  │     │  └───────────────┘  │     │                     │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘

                   ┌─────────────────────────────────────┐
                   │              API Layer              │
                   │                                     │
                   │  ┌───────────────┐ ┌─────────────┐  │
                   │  │ Admin API     │ │ Customer API│  │
                   │  └───────────────┘ └─────────────┘  │
                   └─────────────────────────────────────┘
                                    │
                   ┌────────────────┴────────────────────┐
                   │         Streamlit Frontend Layer     │
                   │                                     │
                   │  ┌───────────────┐ ┌─────────────┐  │
                   │  │ Admin Portal  │ │Customer Portal│ │
                   │  └───────────────┘ └─────────────┘  │
                   └─────────────────────────────────────┘
```

## Data Flow

1. **Data Ingestion**
   - Upload Excel files + Word templates
   - Validate data format and completeness
   - Queue processing tasks

2. **Data Processing**
   - Map Excel data to Word template placeholders
   - Generate Word documents
   - Convert Word to PDF

3. **Storage**
   - Store PDF files in MongoDB with metadata
   - Index for quick retrieval

4. **Delivery**
   - Generate secure access tokens and links
   - Send SMS via third-party API
   - Track delivery status

5. **Access**
   - Authenticate customer access requests
   - Serve PDF files with expiring links
   - Log access for auditing
