from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove
from io import BytesIO
from PIL import Image

app = FastAPI()

@app.post("/remove-background/")
async def remove_background(file: UploadFile = File(...)):
    # Read the uploaded file
    contents = await file.read()
    
    # Remove the background using rembg
    output = remove(contents)
    
    # Convert the output to an image
    img = Image.open(BytesIO(output))
    
    # Convert the image to bytes
    img_byte_arr = BytesIO()
    img.save(img_byte_arr, format='PNG')
    
    # Return the image directly as the response
    return Response(content=img_byte_arr.getvalue(), media_type="image/png")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
