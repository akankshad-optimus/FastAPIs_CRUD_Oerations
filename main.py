from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is working"}

@app.get("/add")
def add_numbers(a: int, b: int):
    result = a + b
    return {"result": result}


def run_cli_addition():
    print("Simple addition program")
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    result = a + b
    print(f"Result: {a} + {b} = {result}")


if __name__ == "__main__":
    run_cli_addition()