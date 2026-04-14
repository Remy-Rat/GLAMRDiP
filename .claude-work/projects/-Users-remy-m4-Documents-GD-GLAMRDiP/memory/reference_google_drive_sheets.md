---
name: Google Drive Sheet IDs
description: Google Drive file IDs for Order Schedule sheets, used to export via gcloud + Drive API
type: reference
---

## Order Schedules folder
- Folder ID: `1wCqXmUtHlzwypaqdE3TOGzhfB2ONF00t`

## AUS Order Schedule
- Shortcut ID: `1wbBUOOIHeruEC4KhNBtG2ZzCvQsspaC-`
- Actual Sheet ID: `1fUitkQWryQmKdWLwvjyRG_C_-yh0v5lHjvQa3urBGr8`

## How to export
```bash
TOKEN=$(/opt/homebrew/share/google-cloud-sdk/bin/gcloud auth print-access-token)
curl -s -H "Authorization: Bearer $TOKEN" \
  "https://www.googleapis.com/drive/v3/files/SHEET_ID/export?mimeType=application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" \
  -o /tmp/output.xlsx
```

## CA Order Schedule
- Sheet ID: `1mCE2X25Fw67liKBgyvNMf3JGOwLM5ufQJTGPEJH1VEw`

## UK Order Schedule
- Sheet ID: `1G7kzaGst8vyjgySiGJJC7BjdRf7eJiU-aHUsaE3PyXE`

## Nordic Order Schedule
- Sheet ID: `1aBa7b5KZkOYYOfuBK3OHYENUQrFgrRtDwouL6fj2hTw`

## Auth
- Authenticated via `gcloud auth login --enable-gdrive-access`
- Token has Drive read-only scope
- If token expires, user needs to re-run the auth command
