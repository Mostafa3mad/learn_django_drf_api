# Django REST Framework - API Development & Configuration

This repository demonstrates the setup of an API using **Django** and **Django REST Framework (DRF)**, covering key concepts such as routing, CRUD operations, JWT authentication, file uploads, API documentation, Redis caching, and pagination.

## Topics Covered:

### 1. **Setting Up Django REST Framework (DRF)**
   - **`ViewSets` and `DefaultRouter`**:
     - Used **`ModelViewSet`** and **`DefaultRouter`** to automatically handle CRUD operations without defining individual routes.
     - This allows efficient handling of **list**, **create**, **retrieve**, **update**, and **delete** actions.
   
   - **Example:**
     ```python
     from rest_framework import viewsets
     from .models import Person
     from .serializers import PersonSerializer

     class PersonViewSet(viewsets.ModelViewSet):
         queryset = Person.objects.all()
         serializer_class = PersonSerializer
     ```

### 2. **File Uploads with Django API**
   - **Image Uploads**:
     - Used **`ImageField`** in Django models to handle image uploads through the API.
     - Configured **`MEDIA_URL`** and **`MEDIA_ROOT`** to handle the storage of media files.
   
   - **Example Model for Image Uploads:**
     ```python
     class Person(models.Model):
         name = models.CharField(max_length=255)
         profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
     ```
   
   - **Serving Media Files**:
     - Configured `urls.py` to serve media files during development.

### 3. **JWT Authentication & Permissions**
   - **JWT Authentication**:
     - Implemented **`JWTAuthentication`** to ensure secure API access using **JSON Web Tokens** for user verification.
   
   - **Session Authentication**:
     - Added **`SessionAuthentication`** to enable authentication via sessions for web users.

   - **Permissions**:
     - Restricted access to API endpoints using **`IsAuthenticated`** to ensure only authorized users can access certain views.

### 4. **API Documentation**
   - **drf-spectacular**:
     - Integrated **drf-spectacular** to automatically generate OpenAPI documentation for the API.
     - Enabled **Swagger UI** for interactive API exploration and **Redoc** for clean, static documentation.

   - **Example Swagger UI Configuration:**
     ```python
     SPECTACULAR_SETTINGS = {
         'TITLE': 'E-Commerce API',
         'DESCRIPTION': 'A simple Product & Order API that helps us learn Django REST Framework',
         'VERSION': '1.0.0',
         'CONTACT': {'name': 'Your Name', 'email': 'your_email@example.com'},
         'LICENSE': {'name': 'MIT', 'url': 'https://opensource.org/licenses/MIT'},
         'SCHEMAS': [],
         'SERVE_INCLUDE_SCHEMA': False,
     }
     ```

### 5. **Database Configuration**
   - **SQLite**:
     - Used **SQLite** as the default database backend, which is simple to set up for development.
   
   - **Database Configuration Example:**
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.sqlite3',
             'NAME': BASE_DIR / 'db.sqlite3',
         }
     }
     ```

### 6. **Pagination & Filtering**
   - **Pagination**:
     - Implemented **LimitOffsetPagination** to paginate large datasets efficiently.
   
   - **Filtering**:
     - Used **`django_filters`** to filter querysets dynamically based on parameters passed in the request.

   - **Example:**
     ```python
     REST_FRAMEWORK = {
         'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
         'PAGE_SIZE': 2,
     }
     ```

### 7. **URL Configuration with DefaultRouter**
   - Used **`DefaultRouter`** to automatically generate routes for the **`ModelViewSet`** to handle CRUD operations.
   
   - **Example URL Registration:**
     ```python
     from rest_framework.routers import DefaultRouter
     from .views import PersonViewSet

     router = DefaultRouter()
     router.register('persons', PersonViewSet)

     urlpatterns = [
         path('api/v1/', include(router.urls)),
     ]
     ```

   - **Other API Endpoints**:
     - **Students API**:
       - `GET /students/`: List all students.
       - `GET /students/{id}/`: Retrieve a student by ID.
     - **Employee API**:
       - `GET /employees/`: List all employees.
       - `POST /employees/`: Add a new employee.
       - `GET /employees/{id}/`: Retrieve employee details by ID.
     - **Blogs & Comments API**:
       - `GET /blogs/`: List all blogs.
       - `GET /comments/`: List all comments.
       - `POST /comments/`: Add a new comment.
       - `GET /blogs/{id}/`: Retrieve blog by ID.
       - `GET /comments/{id}/`: Retrieve comment by ID.

### 8. **Error Handling and Debugging**
   - Handled 404 errors for missing media files by configuring `MEDIA_URL` and `MEDIA_ROOT` correctly.
   - Ensured proper URL routing for static files during development.

---

## How to Set Up and Run the Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Mostafa3mad/learn_django_drf_api.git
