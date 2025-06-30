# HITL
Human-in-the-Loop Systems for Warehouse Decision-Making
Overview

This project implements a Human-in-the-Loop (HITL) warehouse staffing model using Streamlit, enabling real-time decision support for warehouse operations. The model allows supervisors and operations managers to input staffing levels, volume, and processing rates across four key areas of a warehouse—Inbound Dock, Outbound Dock, Small Sort, and General Sort—segmented into four operational banks (A–D). The tool evaluates whether current staffing is sufficient based on calculated staffing needs and provides immediate visual feedback.

Purpose

The goal of this tool is to help operations leaders determine if each area of the warehouse is adequately staffed per 6-hour shift bank and to identify imbalances that may require human intervention, such as reassigning staff or escalating staffing concerns.

Authored by Me
	•	Designed the warehouse model framework with four major operational areas and daily shift banks.
	•	Implemented the Streamlit UI, including:
	•	Interactive columns (col1 to col4) representing each warehouse area.
	•	Input fields for volume, staff, and processing rates.
	•	Logical blocks for calculating staff needed per bank and outputting validation feedback (✅ / ❌).
	•	Integrated operational logic assuming each shift bank runs for 6 hours, with staffing need calculated as:
\text{{Staff Needed}} = \frac{{\text{{Volume}}}}{{\text{{Processing Rate}} \times 6}}
	•	Segmented each area into Bank A to D, mirroring real-world warehouse shift management.

Changes Made by ChatGPT
	•	Created a compatible CSV template (hitl_warehouse_data.csv) containing sample data structured as:
	•	Area, Bank, Volume, Staff, ProcessingRate
	•	This supports automated ingestion into the app for testing or batch analysis.
	•	Offered integration strategy for pd.read_csv() and st.file_uploader() to auto-populate fields from the CSV.
	•	Provided a downloadable file and ensured all area/bank configurations aligned with your Streamlit script.

How to Use
	1.	Run the Streamlit app:

 2.	Enter or upload the data for each area:
	•	Volume of packages
	•	Number of staff assigned
	•	Processing rate for each area
	3.	Click the respective “Check Staffing” button to evaluate sufficiency for each bank.
	4.	Review the results to take action on overstaffed or understaffed sections.

Future Enhancements (Optional)
	•	Enable CSV file uploads to pre-fill all fields.
	•	Implement visual dashboards with staffing imbalance summaries.
	•	Add automated recommendations for staffing reallocation.
