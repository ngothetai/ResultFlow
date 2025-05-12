# UI/UX Design

This document outlines the user interface and experience design for both the Admin Portal and Customer Portal of ResultFlow.

## Admin Portal

The Admin Portal is designed for efficiency and clarity, focusing on workflow management and monitoring.

### Dashboard Page

![Dashboard Wireframe](https://via.placeholder.com/800x500?text=Dashboard+Wireframe)

**Components:**
- **Summary Cards**: Display key metrics (total reports, pending deliveries, success rate)
- **Activity Timeline**: Recent activity in the system
- **Status Chart**: Visual representation of report statuses
- **Quick Actions**: Buttons for frequent tasks

### Batch Management Page

![Batch Management Wireframe](https://via.placeholder.com/800x500?text=Batch+Management+Wireframe)

**Components:**
- **Batch Upload Form**:
  - Excel file uploader
  - Template selector
  - Batch name and description fields
  - Mapping validation preview
- **Active Batches Table**:
  - Batch name
  - Date created
  - Progress indicator
  - Status
  - Actions (view details, cancel)
- **Historical Batches**: Paginated list of completed batches

### Report Preview & Delivery Page

![Report Preview Wireframe](https://via.placeholder.com/800x500?text=Report+Preview+Wireframe)

**Components:**
- **PDF Preview**: Embedded PDF viewer
- **Customer Information**: Display recipient details
- **Delivery Form**:
  - Phone number verification
  - Custom message option
  - Schedule delivery option
- **Send Button**: With confirmation dialog
- **Delivery Status**: Real-time updates

### Template Management Page

![Template Management Wireframe](https://via.placeholder.com/800x500?text=Template+Management+Wireframe)

**Components:**
- **Template List**: All available Word templates
- **Upload Form**: For new templates
- **Mapping Configuration**:
  - Visual mapping of Excel columns to Word placeholders
  - Validation tools

### Settings Page

- API configuration for SMS provider
- Email notification settings
- Default expiry settings
- User management

## Customer Portal

The Customer Portal is designed to be simple, secure, and focused on the task of viewing and downloading reports.

### Authentication Page

![Authentication Wireframe](https://via.placeholder.com/800x500?text=Authentication+Wireframe)

**Components:**
- **Password Entry**: For the temporary password received via SMS
- **Access Information**: Clear explanation of access duration
- **Security Information**: Assurance about data protection

### Report Viewer Page

![Report Viewer Wireframe](https://via.placeholder.com/800x500?text=Report+Viewer+Wireframe)

**Components:**
- **PDF Viewer**: Full-screen capable PDF viewer
- **Download Button**: Prominent and clear
- **Patient Information**: Basic details about the report
- **Expiry Notice**: Countdown or information about access expiration
- **Help Information**: Contact details if assistance is needed

## Design Principles

1. **Simplicity**: Focus on core functionality, remove unnecessary elements
2. **Clarity**: Clear labels, intuitive navigation, helpful instructions
3. **Efficiency**: Minimize clicks for common tasks
4. **Consistency**: Uniform design throughout
5. **Python-First**: Use Streamlit's Python-centric approach for all UI components

## Streamlit Theme Customization

Streamlit allows theme customization through a `.streamlit/config.toml` file:

```toml
[theme]
base="light"
primaryColor="#1976D2" # Blue - Trust, security, professionalism
secondaryBackgroundColor="#F5F5F5" # Light Gray - Clean, professional
textColor="#212121" # Dark Gray - Readability
font="sans serif"
```

## Streamlit UI Components

- **st.dataframe/st.table**: For displaying tabular data
- **st.file_uploader**: For Excel and Word template uploads
- **st.progress**: For progress bars during processing
- **st.plotly_chart**: For interactive visualizations
- **st.tabs**: For organizing dashboard sections
- **st.expander**: For collapsible sections of information
- **st_aggrid**: For advanced table features (sorting, filtering)

## Interaction Design with Streamlit

### Admin Portal Workflow

1. **Upload and Process**:
   - Admin uploads Excel using st.file_uploader
   - Admin selects Word template from dropdown
   - System validates data with visual feedback
   - st.progress bar shows conversion process
   - st.success notification appears when complete

2. **Review and Send**:
   - Admin selects report from table
   - PDF preview appears using built-in components
   - Admin verifies information
   - Admin clicks "Send to Customer" button
   - st.confirmation_dialog appears
   - Success notification shows delivery status

### Customer Portal Workflow

1. **Access**:
   - Customer receives SMS with link and password
   - Customer visits Streamlit app and enters password
   - System validates credentials and grants access

2. **View and Download**:
   - Report displays automatically using PDF viewer
   - st.download_button is prominently displayed
   - Session timeout managed by Streamlit

## Streamlit Deployment Considerations

- Streamlit Cloud for easy deployment
- Docker containerization for self-hosting
- Streamlit's built-in responsive design works on most devices
- Streamlit sharing for development and testing

## Implementation Guidelines

- Use Streamlit's built-in components whenever possible
- Use Streamlit-Extras for additional UI components
- Implement session state for preserving user state across interactions
- Use Streamlit's caching mechanisms for performance optimization
- Ensure proper error handling with st.error and st.exception
- Optimize PDF rendering for both display and download
- Follow Streamlit's best practices for app structure
