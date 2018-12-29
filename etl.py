import fire, os
import pandas as pd

TEMP_DIR = "./temp"
REQUESTS_URL = "http://seshat.datasd.org/get_it_done_311/get_it_done_2018_requests_datasd.csv"

def _create_directory_if_not_exists():
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)

def extract_gid():
    print("Loading CSV from URL {}".format(REQUESTS_URL))
    df = pd.read_csv(REQUESTS_URL)
    df.to_csv("{}/requests_raw.csv".format(TEMP_DIR), index=False)
    return "Successfully downloaded and wrote GID Requests to {}".format(TEMP_DIR)

def transform_gid():
    # Load the temporrary df that was downloaded.  Throw an error if not available.
    print("Loading raw requests")
    df = pd.read_csv("{}/requests_raw.csv".format(TEMP_DIR))

    # Convert null districts to 0
    df[pd.isnull(df.district)] = 0

    # Convert district column to integer
    df.district = df.district.astype(int)

    # Keep only requests where status is New, Referred, Closed or In Process
    df = df[df.status.isin(['New', 'Referred', 'Closed', 'In Process'])]

    # Verify council districts are in range from 0-9:
    assert len(df[(df.district > 9) | (df.district < 0)]) == 0, "Council District Field out of Range"

    # Select only relevant columns for our report
    df = df[["service_request_id", "requested_datetime", "service_name", "case_record_type", "status", "district", "case_origin", "referred_department"]]

    # Rename columns
    df.columns = ["request_id", "date_requested", "service_subsystem", "service_description", "case_status", "cd", "submitted_via", "referred_to_dept"]

    print("Writing clean requests")
    df.to_csv("{}/requests_clean.csv".format(TEMP_DIR), index=False)

def generate_district_report(district_num, status='All'):
    df = pd.read_csv("{}/requests_clean.csv".format(TEMP_DIR))

    df = df[df.cd == district_num]

    if status is not 'All':
        df = df[df.case_status == status]

    print("Wrote {} records for district {} with status {}".format(df.shape[0], district_num, status))
    df.to_csv("{}/requests_district_{}.csv".format(TEMP_DIR, district_num), index=False)



def gid_etl_report(district_num, status):
    _create_directory_if_not_exists()
    print("Extracting GID Requests from CSV")
    extract_gid()

    print("Transforming GID Requests")
    transform_gid()

    print("Generating report for district {} with status {}".format(district_num, status))
    generate_district_report(district_num, status)



if __name__ == '__main__':
  fire.Fire()
