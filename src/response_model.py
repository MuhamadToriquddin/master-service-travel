from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List,Dict,Union,Any,Optional

class ResponseSuccessModel(BaseModel):
    status:str
    message:str
    data: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
    

def error_response (status_code:int, message:str):
    return JSONResponse(
        status_code=status_code,
        content={
            "status":"error",
            "message":message
        }
    )
    
# pre defined exceptions 
def bad_request(message: str = "Bad Request"):
    error_response(status.HTTP_400_BAD_REQUEST, message)

def unauthorized(message: str = "Unauthorized"):
    error_response(status.HTTP_401_UNAUTHORIZED, message)

def forbidden(message: str = "Forbidden"):
    error_response(status.HTTP_403_FORBIDDEN, message)

def not_found(message: str = "Not Found"):
    error_response(status.HTTP_404_NOT_FOUND, message)

def conflict(message: str = "Conflict"):
    error_response(status.HTTP_409_CONFLICT, message)

def internal_error(message: str = "Internal Server Error"):
    error_response(status.HTTP_500_INTERNAL_SERVER_ERROR, message)