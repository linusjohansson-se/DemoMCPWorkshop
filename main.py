from fastmcp import FastMCP

mcp = FastMCP("Demo Shop resources")

@mcp.resource(uri="shop://products")
def GetProducts():
    return [
        {"name": "Apple", "price": 1.00},
        {"name": "Banana", "price": 0.50},
        {"name": "Orange", "price": 0.75},
    ]

@mcp.resource(uri="shop://categories")
def GetCategories():
    return ["Fruit", "Vegetables", "Dairy"]

@mcp.resource(uri="shop://store-location")
def GetStoreLocation():
    return "123 Main Street, Anytown, USA"

if __name__ == "__main__":
    mcp.run()