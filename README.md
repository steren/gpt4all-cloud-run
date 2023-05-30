# gpt4all-cloud-run

## Build

Build into a container image with: 

```
docker build -t gpt4all-api .
```

## Run locally

Start the container, model will be loaded from the filesystem on first startup.

```
docker run -p8080:8080 -ePORT=8080 gpt4all-api
```

When started, send a POST request:

```
curl http://localhost:8080/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Hi, how are you?"}]
  }'
```

## Deploy to Cloud Run

```
gcloud run deploy gpt4all --source . \ 
   --cpu 8 \
   --memory 8 \ 
   --timeout 900 \
   --execution-environment gen2 \
   --allow-unauthenticated \
   --region us-central1
```
