from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.user_controller import router as user_router
from app.controllers.product_controller import router as product_router
from app.controllers.order_controller import router as order_router

# Initialize FastAPI application
app = FastAPI(
    title="E-commerce API",
    description="A FastAPI-based backend for an e-commerce application",
    version="1.0.0",
)

# CORS settings (adjust 'origins' for production)
origins = ["*"]  # Use specific domains in production for security

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # List of allowed origins
    allow_credentials=True,         # Allow cookies
    allow_methods=["*"],            # Allow all HTTP methods
    allow_headers=["*"],            # Allow all headers
)

# Include Routers
app.include_router(user_router, prefix="/api/v1/users", tags=["Users"])
app.include_router(product_router, prefix="/api/v1/products", tags=["Products"])
app.include_router(order_router, prefix="/api/v1/orders", tags=["Orders"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the E-commerce API!"}
