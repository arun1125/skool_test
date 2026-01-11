from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/pricing", response_class=HTMLResponse)
async def pricing(request: Request):
    return templates.TemplateResponse("pricing.html", {"request": request})

@app.get("/case-studies", response_class=HTMLResponse)
async def case_studies(request: Request):
    return templates.TemplateResponse("case_studies.html", {"request": request})

@app.post("/contact")
async def contact(request: Request):
    # In a real app, this would send an email or save to DB.
    # Returning a simple success message for HTMX to swap.
    return HTMLResponse("""
        <div class="p-4 bg-green-900 border border-green-700 text-green-200 font-mono text-sm">
            > REQUEST_RECEIVED: DISCOVERY_CALL_INITIATED...
            <br>
            > STATUS: AGENT_DISPATCHED. WE WILL CONTACT YOU SHORTLY.
        </div>
    """)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
