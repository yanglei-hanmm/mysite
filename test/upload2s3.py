import boto3
from botocore.client import Config
session = boto3.session.Session()

file_path = '/home/pk/Zabbix.mp4'
key_name = 'Zabbix.mp4'
bucket_name = 'testbucket'
access_key = 'YS5NGNCJJMLOU607ZD5Q'
secret_key = '4BQ03ZSN8xxZ4f6ED7FALSEhOmOZUpsB14u3sKFc'
endpoint = 'http://zabbix-prod-03.quanyou.com.cn'

s3 = session.client('s3',use_ssl=False,endpoint_url=endpoint,
                    aws_access_key_id=access_key,aws_secret_access_key=secret_key,
                    config=Config(signature_version='s3v4',s3={'addressing_style':'path'}))
response = s3.create_bucket(Bucket=bucket_name)
print(response)

s3.upload_file(file_path,bucket_name,key_name,ExtraArgs={'ContentType':'video/mp4'})
params = {'Bucket': bucket_name,'Key': key_name}
url = s3.generate_presigned_url('get_object',Params=params,ExpiresIn=3600)
print(url)