# Database Schema

ResultFlow uses MongoDB as its primary database for storing documents and metadata. This NoSQL approach provides flexibility for storing various document types and supports efficient querying.

## Collections

### 1. Templates

Stores information about Word templates used for report generation.

```javascript
{
  "_id": ObjectId,
  "name": String,             // Template name
  "description": String,      // Description of the template
  "file_path": String,        // Path to the template file
  "placeholder_map": Object,  // Mapping of Excel columns to template placeholders
  "created_at": Date,
  "updated_at": Date,
  "active": Boolean           // Whether the template is active
}
```

### 2. Reports

Stores information about generated reports.

```javascript
{
  "_id": ObjectId,
  "customer_id": String,      // ID or reference to customer
  "customer_name": String,    // Name of the customer
  "customer_phone": String,   // Phone number for SMS delivery
  "source_data": {            // Original data used for report
    "file_id": String,        // Reference to original Excel file
    "row_index": Number       // Row index in the Excel file
  },
  "template_id": ObjectId,    // Reference to template used
  "pdf_file": {
    "file_id": String,        // MongoDB GridFS file ID
    "filename": String,
    "size": Number,
    "mime_type": String
  },
  "word_file": {
    "file_id": String,        // MongoDB GridFS file ID
    "filename": String
  },
  "status": String,           // "pending", "generated", "delivered", "viewed", "expired"
  "access_token": String,     // Token for accessing the report
  "password": String,         // Temporary access password
  "created_at": Date,
  "updated_at": Date,
  "expires_at": Date,         // When access expires
  "delivery": {
    "sent_at": Date,
    "delivery_status": String,  // "pending", "sent", "delivered", "failed"
    "sms_provider_id": String,  // Reference ID from SMS provider
    "access_url": String        // URL sent to customer
  },
  "views": [                  // Tracking of when reports are viewed
    {
      "timestamp": Date,
      "ip_address": String,
      "user_agent": String
    }
  ]
}
```

### 3. BatchJobs

Tracks batches of uploaded Excel files and their processing.

```javascript
{
  "_id": ObjectId,
  "name": String,             // Batch name
  "description": String,
  "source_file": {
    "file_id": String,        // MongoDB GridFS file ID
    "filename": String,
    "size": Number,
    "uploaded_at": Date,
    "row_count": Number       // Number of rows in Excel
  },
  "template_id": ObjectId,    // Reference to template used
  "status": String,           // "pending", "processing", "completed", "failed"
  "progress": {
    "total": Number,
    "processed": Number,
    "successful": Number,
    "failed": Number
  },
  "created_at": Date,
  "completed_at": Date,
  "created_by": String,       // Admin who created the batch
  "reports": [ObjectId]       // References to report documents
}
```

### 4. Users

Stores admin user information.

```javascript
{
  "_id": ObjectId,
  "username": String,
  "email": String,
  "hashed_password": String,
  "full_name": String,
  "role": String,             // "admin", "viewer"
  "is_active": Boolean,
  "last_login": Date,
  "created_at": Date
}
```

### 5. Files

Uses MongoDB GridFS for storing files (PDFs, Word docs, and Excel files).

## Indexes

For optimal performance, the following indexes should be created:

```javascript
// Reports collection
db.reports.createIndex({ "customer_phone": 1 });
db.reports.createIndex({ "access_token": 1 }, { unique: true });
db.reports.createIndex({ "expires_at": 1 }, { expireAfterSeconds: 0 });
db.reports.createIndex({ "status": 1 });

// BatchJobs collection
db.batchJobs.createIndex({ "created_at": -1 });
db.batchJobs.createIndex({ "status": 1 });

// Templates collection
db.templates.createIndex({ "name": 1 }, { unique: true });
db.templates.createIndex({ "active": 1 });
```

## Data Lifecycle

1. **Temporary Storage**: Excel, Word files initially stored in GridFS
2. **Permanent Storage**: Generated PDFs stored in GridFS
3. **Expiry Management**: 
   - Access tokens expire after 24 hours
   - Reports are archived after a configurable retention period (default: 6 months)
   - Original Excel and Word files can be purged after a configurable period

## Data Backup Strategy

1. Daily backups of MongoDB using mongodump
2. Weekly full backups stored on separate storage
3. Backup rotation and retention policy for disaster recovery
