import os
import shutil

from fastapi.responses import FileResponse
from fastapi import APIRouter, File, UploadFile

router = APIRouter(
    prefix="/files",
    tags=["files"]
)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

### UPLOAD FILE
@router.post("/")
async def upload_file(file:UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "status": "uploaded"
    }

### LIST FILE
@router.get("/")
def list_files():

    files = os.listdir(UPLOAD_DIR)

    return {
        "files": files
    }

### DOWNLOADING FILE
@router.get("/{filename}")
def download_file(filename: str):

    file_path = f"{UPLOAD_DIR}/{filename}"

    return FileResponse(
        path=file_path,
        filename=filename
    )

### DELETE FILE

@router.delete("/{filename}")
def delete_file(filename: str):

    file_path = f"{UPLOAD_DIR}/{filename}"

    if not os.path.exists(file_path):
        return {
            "status": "error",
            "message": "File not found"
        }

    os.remove(file_path)

    return {
        "status": "success",
        "message": f"{filename} deleted"
    }



