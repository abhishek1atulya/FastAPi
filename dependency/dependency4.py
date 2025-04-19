from fastapi import FastAPI, Depends, HTTPException, Request

app = FastAPI()

# Dependency to extract Authorization header
def get_current_user(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or auth_header != "Bearer mysecrettoken":
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {"username": "admin"}

@app.get("/protected/")
def protected_route(user: dict = Depends(get_current_user)):
    return {"message": "This is a protected route.", "user": user}



# In this example, the get_current_user dependency function is used to 
# authenticate the user by checking the authorization header. 
# If the token is valid, the function returns the user information. 
# Otherwise, it raises an HTTPException with a status code of 401 (Unauthorized).