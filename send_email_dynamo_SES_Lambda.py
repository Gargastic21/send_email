import json
import boto3
from botocore.exceptions import ClientError

#get item from dynamo db code.
def get_data():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('email_userlists')
    response = table.scan()
    data = response['Items']
    print(data)
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    print(json.dumps(data))
    list_of_data= (data)
    list_of_email = []
    for i in list_of_data:
        list_of_email.append((i['email_id']))
    
    print(list_of_email)
    
    return (list_of_email)
    



#send email code


def send_email(userlist):
    SENDER = "Amisha Das <designcreative1811@gmail.com>"
    # RECIPIENT = "designcreative1811@gmail.com"
    RECIPIENT = userlist
    #CONFIGURATION_SET = "ConfigSet"
    AWS_REGION = "us-east-1"
    SUBJECT = "Amazon SES Test (SDK for Python)"
    BODY_TEXT = ("Amazon SES Test (Python)\r\n"
                 "This email was sent with Amazon SES using the "
                 "AWS SDK for Python (Boto)."
                )
    
    BODY_HTML = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href="style.css">
        <title>Email</title>
    </head>
                """            
    
    CHARSET = "UTF-8"
    client = boto3.client('ses',region_name=AWS_REGION)
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': RECIPIENT
                
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER
            
        )
    
    except ClientError as e:
        return(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        return(response['MessageId'])


def lambda_handler(event, context):
    # TODO implement
    userlist=get_data()
    response=send_email(userlist);
    return {
        'statusCode': 200,
        'body': response
    }




# import psycopg2
# import sys
# import boto3
# import os

# main(['install', '-I', '-q', 'psycopg2', '--target', '/tmp/', '--no-cache-dir', '--disable-pip-version-check'])
# sys.path.insert(0,'/tmp/')

# ENDPOINT="database-1-ami.cdu93y40ni7m.us-east-1.rds.amazonaws.com"
# PORT="5432"
# USR="postgres_ami"
# REGION="us-east-1"
# DBNAME="database-1-ami"

# #gets the credentials from .aws/credentials
# session = boto3.Session(profile_name='RDSCreds')
# client = session.client('rds')

# token = client.generate_db_auth_token(DBHostname=ENDPOINT, Port=PORT, DBUsername=USR, Region=REGION)

# def connect_db():
#     try:
#         conn = psycopg2.connect(host=ENDPOINT, port=PORT, database=DBNAME, user=USR, password=token, sslmode='prefer', sslrootcert="[full path]rds-combined-ca-bundle.pem")
#         cur = conn.cursor()
#         #cur.execute("""SELECT now()""")
#         #query_results = cur.fetchall()
#         return (cur)
#     except Exception as e:
#         print("Database connection failed due to {}".format(e))                


# def lambda_handler(event, context):
#     # TODO implement
    
#     response=connect_db();
#     return {
#         'statusCode': 200,
#         'body': response
#     }                   


