import os
import shutil
from fastapi import APIRouter,UploadFile,File

router = APIRouter(
    prefix="/upload",
    tags=["users"]
)

os.makedirs("uploads", exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "status": "uploaded"
    }