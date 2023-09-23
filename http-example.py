#!./venv/bin/python

from typing import Any, Optional
from fastapi import FastAPI, Query, Request
from pydantic import BaseModel
import base64


version = "v1.2.3"


app = FastAPI()

#
# RECEIVE AND DO SOMETHIND REQUIRED WITH NOTIFICATIONS DATA
# MAIN
#

class NotifyData(BaseModel):
  recipients: list[str] # recipients list
  subject: str # notification subject
  text: str # text of notification
  image: str # base64 encoded image


# POST / receives prepared notification data to send
# required 
@app.post("/")
async def notify(req: Request, data: NotifyData):
  print("data:", data.recipients, data.subject, data.text, len(data.image))
  
  comp = int(req.query_params['compression'])
  save = req.query_params['save'].lower() == 'true'

  print({"comp":comp,"save":save})
  

  if save == "true":
    f = open("image.jpg", "wb")
    f.write(base64.b64decode(data.image))
    f.close()

  return {}

# 
# STATUS
# OPTIONAL
# 

# the list of contacts will be available for selection in the recipients line
class Contact(BaseModel):
  name: str
  value: str

# list of variables based on which custom fields will be added to the RTMIP
class Variable(BaseModel):
  type: str
  name: str
  label: str
  desc: Optional[str] = None

  readonly: Optional[bool] = None
  value: Optional[Any] = None
  default: Optional[Any] = None
  width: int = 12

# status response
class StatusResp(BaseModel):
  version: Optional[str]
  contacts: Optional[list[Contact]] = None
  variables: Optional[list[Variable]] = None


# GET /status can be useful for transmitting any custom parameters from the
# rtmip to the service
# optional
@app.get("/status", response_model=StatusResp)
async def root():
  return StatusResp(
    version=version, 
    contacts=[Contact(name="test",value="test@example.com")], 
    variables=[
      Variable(type="number", name="compression", label="Compression Level"),
      Variable(type="checkbox", name="save", label="Save Images"), 
    ],
  )


