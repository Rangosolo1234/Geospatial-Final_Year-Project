# Geospatial IoT Integration For Real-Time Power Monitoring

## Project Overview
This project leverages Geospatial IoT to enable real-time power monitoring using the **ZMPT101B voltage sensor**, **LoRa technology**, and **Arduino Nano**. The system continuously monitors electrical faults and transmits location-based alerts for immediate response.

## Key Technologies
- **Geospatial Framework:** GeoDjango
- **Database:** PostgreSQL with PostGIS for spatial data handling
- **Backend:** Django ORM for managing shapefile uploads and data storage
- **Frontend:** Map-based visualization for real-time fault detection
- **Hardware:** Arduino Nano, ZMPT101B voltage sensor, LoRa modules

## Features
- **Real-Time Monitoring:** Captures voltage fluctuations and detects faults
- **Geospatial Analysis:** Maps electrical faults using uploaded shapefiles
- **LoRa Communication:** Ensures long-range, low-power data transmission
- **Database Integration:** Stores geospatial data using PostgreSQL/PostGIS
- **Django ORM:** Handles spatial queries and shapefile uploads

## Project Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Rangosolo1234/Geospatial-Final_Year-Project.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Geospatial-Final_Year-Project
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   psql -U postgres -c "CREATE DATABASE power_monitoring;"
   psql -U postgres -d power_monitoring -c "CREATE EXTENSION postgis;"
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Start the Django server:
   ```bash
   python manage.py runserver
   ```
7. Upload shapefiles using the web interface.

## Project Results
![1](https://github.com/user-attachments/assets/cf06c20e-c6ef-41bb-86bd-106abb2a8990)
![4](https://github.com/user-attachments/assets/49e32784-6126-4bc4-be35-f0d1f16f9b26)
![3](https://github.com/user-attachments/assets/968e879e-f7ed-4b9e-afd0-4400a915642d)
![2](https://github.com/user-attachments/assets/305762e7-dbc0-46bb-9e9a-37c9e3770453)
![IMG_20240309_101017](https://github.com/user-attachments/assets/e92ec438-1ab1-4222-acd1-9be2161d47d4)
![IMG_20240328_202216](https://github.com/user-attachments/assets/8aefba5d-9f4d-40bb-b472-ff3acba5775c)
![IMG_20240329_190625](https://github.com/user-attachments/assets/54d1ef54-d6d3-4655-a39e-9dbebd672a19)

## Future Improvements
- **Machine Learning Integration:** Predictive analytics for fault detection
- **Mobile App Development:** Extend functionality to mobile devices
- **Enhanced Visualizations:** Advanced dashboards for power analytics

## Contribution
Feel free to fork this project, raise issues, or submit pull requests!

## License
This project is licensed under the MIT License.

---
Developed by **Solomon Kipkirui** | GitHub: [Rangosolo1234](https://github.com/Rangosolo1234)

