import boto3

s3 = boto3.client('s3')

s3_bucket_name = 'intune-music-files'
audio_file_key = 'mb_space_cadet.mp3'

audio_file = s3.get_object(Bucket=s3_bucket_name, Key=audio_file_key)
# Get the audio file's data
audio_data = audio_file['Body'].read()

for k,v in audio_file.items():
    print(k, v)