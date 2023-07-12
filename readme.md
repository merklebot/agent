# Usage of Easy Uploading Script

1. #### Obtain user key

To obtain the user key, follow these steps:

- Make a GET request to `{TENANT_NAME}.storage.api2.merklebot.com/users/` endpoint.
- If you have no users created yet, send a POST request to create one.

Examples using cURL:

```bash
curl -X 'GET' \
  'https://{TENANT_NAME}.storage.api2.merklebot.com/users/' \
  -H 'accept: application/json' \
  -H 'Authorization: TENANT_TOKEN'
```

```bash
curl -X 'POST' \
  'https://{TENANT_NAME}.storage.api2.merklebot.com/users/' \
  -H 'accept: application/json' \
  -H 'Authorization: TENANT_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{}'
```

- Obtain a token with a POST request to `{TENANT_NAME}.storage.api2.merklebot.com/tokens/` endpoint.
Specify `ownerId` and `expiry`:

```bash
curl -X 'POST' \
  'https://{TENANT_NAME}.storage.api2.merklebot.com/tokens/' \
  -H 'accept: application/json' \
  -H 'Authorization: TENANT_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
  "ownerId": 0,
  "expiry": "2023-07-12T22:26:49.986Z"
}'
```

All the previous steps can be performed interactively using the documentation at `{TENANT_NAME}.storage.api2.merklebot.com/docs`

From now on, you need to use the **USER TOKEN** instead of the **TENANT TOKEN**.


2. #### Insert you credentials in script

Insert `USER_KEY`, `TENANT_NAME` and `FOLDER_PATH` to start uploading files to MerkleBot's Storage in `easy_upload.py` script

3. #### Run the script
Run `easy_upload.py`, it will upload all the files from `FOLDER_PATH` directory, as they will appear. 

---
# Check, Upload and Download files
With a USER_KEY, you can work with files in storage.

- Enlist uploaded files:

```bash
curl -X 'GET' \
  'https://{TENANT_NAME}.storage.api2.merklebot.com/contents/' \
  -H 'accept: application/json' \
  -H 'Authorization: USER_KEY'
```

- Upload new file:

```bash
curl -X 'POST' \
  'https://{TENANT_NAME}.storage.api2.merklebot.com/contents/' \
  -H 'accept: application/json' \
  -H 'Authorization: USER_KEY' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file_in=@example.txt;type=application/txt'
```

- Download file by content_id:

```bash
curl -X 'GET' \
  'https://{TENANT_NAME}.storage.api2.merklebot.com/contents/{CONTENT_ID}/download' \
  -H 'accept: application/json' \
  -H 'Authorization: USER_KEY'
```

