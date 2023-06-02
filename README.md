## About
Json migrator for personal purpose

## Python instalation:
- install python
- install pip

## Package instalation:
```
pip install pymongo oss2 dotenv
```

## Create env file with template:
```
OSS_ENDPOINT=
OSS_BUCKET_NAME=
OSS_ACCESS_KEY=
OSS_SECRET_KEY=

# Exampe for parent directory
OSS_PARENT_DIRECTORY=submissions_result_final

# Exampe for child directory with group ids
OSS_CHILD_DIRECTORYS=792,791,790,786,785784,783,782,781,780,779,778,777,776

MONGODB_URI=
MONGODB_DATABASE=
MONGODB_COLLECTION=
```

## Run script:
```
cd ~/oss-to-monggodb-migrater

py migrator.py
```