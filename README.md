# youtube-data-engineerig-project
AWS data pipeline infra build up for youtube data

**Overview**:
Designed and implemented a scalable data pipeline architecture on AWS for processing YouTube data. The pipeline leverages various AWS services to efficiently extract, transform, and load data, providing insights through BI tools.

**Architecture Components:**
**AWS S3 (Raw Storage):**
Store raw YouTube data in CSV and JSON formats.
**AWS Lambda:**
Triggered to process and transform JSON data from S3, ensuring data consistency and format standardization.
**AWS Glue ETL:**
Perform Extract, Transform, Load (ETL) operations on CSV data from S3.
Clean and prepare the data for further analysis.
**AWS S3 (Processed Storage):**
Store cleaned and transformed data from both Lambda and Glue ETL processes.
**AWS Glue Crawlers:**
Crawl the processed data in S3 to catalog the data, making it queryable in AWS Athena.
**AWS Athena:**
Query the cataloged data for analysis.
Serve as the data source for BI tools.
**Amazon QuickSight (BI Tool):**
Visualize the queried data from Athena.
Provide interactive dashboards and reports for data-driven decision-making.

**Process Flow:**
Raw YouTube data is uploaded to S3 in CSV and JSON formats.
Lambda functions process JSON data, transforming it into a standardized format.
Glue ETL jobs extract data from CSV files, clean and transform it.
The transformed data is stored back in S3 (Processed Storage).
Glue Crawlers scan the processed data and update the data catalog in Glue.
Athena queries the cataloged data for analysis.
QuickSight connects to Athena to visualize data and generate reports.

**Tools and Technologies:**
AWS S3: Data storage (raw and processed)
AWS Lambda: Data transformation
AWS Glue ETL: Data cleaning and transformation
AWS Glue Crawlers: Data cataloging
AWS Athena: Data querying
Amazon QuickSight: Data visualization and reporting

