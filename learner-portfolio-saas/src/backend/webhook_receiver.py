from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/webhook")
async def webhook_listener(request: Request):
    payload = await request.json()
    print("Received event:", payload)
    return {"status": "ok", "event": payload.get("event")}
