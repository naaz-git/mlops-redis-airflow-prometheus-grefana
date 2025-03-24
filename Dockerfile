FROM quay.io/astronomer/astro-runtime:12.6.0

# Install PostgreSQL client and development libraries

# Install required Python dependencies
RUN pip install apache-airflow-providers-google

# Install dependencies from requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt