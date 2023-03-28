import boto
import boto.s3.connection
access_key = 'YS5NGNCJJMLOU607ZD5Q'
secret_key = '4BQ03ZSN8xxZ4f6ED7FALSEhOmOZUpsB14u3sKFc'

conn = boto.connect_s3(
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key,
        host = 'zabbix-prod-03.quanyou.com.cn',
        is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

# # 列出bucket信息
# for bucket in conn.get_all_buckets():
#         print(bucket.name,bucket.creation_date)
#
#
# # 创建bucket
# conn.create_bucket('my-new-bucket')

# 生成对象的下载 URLs
bucket = conn.get_bucket(bucket_name='testbucket')
obj1 = bucket.get_key('zabbix-release_6.2-2+ubuntu20.04_all.deb')
obj1.set_canned_acl('public-read')
obj1_url = obj1.generate_url(0, query_auth=False, force_http=True)
print(obj1_url)
