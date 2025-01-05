import boto3

# اتصال به S3
s3 = boto3.client('s3')

# لیست کردن همه bucketها
response = s3.list_buckets()
print(response['Buckets'])
