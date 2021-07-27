# Real Estate Data Engineering Project
Goal: Track individual properties that match a predetermined set of desired criteria
* Criteria 
  * Location
  * Bathrooms
  * Bedrooms
  * Sq ft
  * Yard/land


* Methods:
  * Web scraping from zillow
  * pipeline orchestration with dagster
  * visualize with live dashboard
  * download the latest properties or those who have changed with a change data capture (CDC) mechanism
  * Zipping and uploading them to S3. With a Delta Lake table, we merge new changes with schema evolution
    


