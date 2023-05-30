# gpt4all-cloud-run

```
docker build -t gpt4all-api .
```

```
docker run -p8080:8080 -ePORT=8080 gpt4all-api
```

```
curl http://localhost:8080/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "Hi, how are you?"}]
  }'
```