from fastapi import FastAPI,Request
from extractiveSummarization import get_op

app = FastAPI()

@app.post("/extractiveSummarization/")
async def extractiveSummarizationApi(request: Request):
    data = await request.json()
    summary = '। '.join(get_op(data['text']))
    return {"summary": summary}
