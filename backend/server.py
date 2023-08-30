from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route and its corresponding function
@app.get("/")
def read_root():
    return {"message": "Hello, this is a simple FastAPI server!"}

# Run the server using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

