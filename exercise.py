# Setup
import boto3
from moto import mock_s3
import pandas as pd
from datetime import datetime
#mock = mock_s3()
#mock.start()

# Not 100% sure yet how DataCamp platform works. Assuming we can put these in ENV, and update the boto call
AWS_KEY_ID = 'FAKE'
AWS_SECRET = 'FAKE'

# SETUP END
# Code Start
s3 = boto3.resource('s3', region_name='us-east-1', aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)
ses = boto3.client('ses', region_name='us-east-1', aws_access_key_id=AWS_KEY_ID, aws_secret_access_key=AWS_SECRET)

df1 = pd.read_csv('http://seshat.datasd.org/get_it_done_311/get_it_done_pothole_requests_datasd.csv')
df2 = pd.read_csv('http://seshat.datasd.org/get_it_done_311/get_it_done_graffiti_removal_requests_datasd.csv')
final = pd.concat([df1, df2])
final.to_csv('final_report.csv')
num_reports = len(final)
s3.Bucket('mrm-datacamp-uploads').upload_file(Filename='./final_report.csv', Key='final_report.csv')

ses.send_email(
    Destination={'ToAddresses': ['max@maksimize.com']},
    Message={
        'Body': {'Text': {'Data': 'There have been {} reports so far'.format(num_reports)}},
        'Subject': { 'Data': 'Final Report Updated'},
    },
    Source='max@maksimize.com',
)

# Code End
# Additional MOTO things.
#mock.stop()

