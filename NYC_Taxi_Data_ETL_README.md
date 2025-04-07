
# NYC Taxi Data ETL Pipeline

## Project Overview
This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using NYC Taxi Zone data. The Python script extracts data from a CSV file, performs basic data cleaning, and loads the transformed data into a PostgreSQL database.

## Prerequisites
- Python 3.x
- pandas library (`pip install pandas`)
- SQLAlchemy library (`pip install sqlalchemy`)
- PostgreSQL database
- psycopg2 library (`pip install psycopg2-binary`)

## Data Source
The NYC Taxi Zone Lookup dataset can be downloaded from:  
[NYC Taxi Zone Lookup Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

## How to Run the Script
1. Clone this repository
2. Install the required dependencies
3. Download the `taxi_zone_lookup.csv` file and place it in the correct path
4. Update the database connection details in the script (username, password, host, port, database name)
5. Run the script:
   ```bash
   python Builidng_an_ETL_PIPELINE_USING_NYC_TAXI_DATA.py
   ```

## Script Details
The script performs the following operations:
1. Reads the taxi zone data from a CSV file
2. Drops rows with missing values in key columns (Borough, Zone, service_zone)
3. Establishes a connection to PostgreSQL
4. Loads the transformed data into a table named "TAXI DATA"

## Database Configuration
Before running the script, ensure you have:
- PostgreSQL installed and running
- A database named `sales_dp` created
- Appropriate permissions for the specified user

## Author
**John Benedict Bello**  
[LinkedIn Profile](https://www.linkedin.com/in/bello-john-493b15155)

## License
This project is open source and available under the MIT License.
