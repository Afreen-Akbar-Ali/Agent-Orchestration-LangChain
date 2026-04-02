from langchain_core.tools import tool

# -----------------------------
# TOOL 1: Calculator
# -----------------------------
@tool
def calculator(expression: str) -> str:
    """Useful for solving math calculations."""
    try:
        result = eval(expression)
        return f"The result is {result}"
    except Exception:
        return "Invalid math expression"


# -----------------------------
# TOOL 2: Weather API (Simulated)
# -----------------------------
@tool
def weather(city: str) -> str:
    """Get weather of a city."""

    weather_data = {
        "delhi": "30°C and sunny",
        "mumbai": "28°C with humidity",
        "kerala": "27°C with light rain",
        "london": "15°C and cloudy"
    }

    city = city.lower()

    if city in weather_data:
        return f"The weather in {city.title()} is {weather_data[city]}"
    else:
        return "Weather data not available."


# -----------------------------
# SIMPLE AGENT LOGIC
# -----------------------------
print("=== LangChain Tool Agent (Simulated) ===")
print("Ask math or weather questions")
print("Type 'exit' to quit\n")


while True:

    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Goodbye!")
        break

    # Calculator tool trigger
    if any(op in user_input for op in ["+", "-", "*", "/"]):

        try:
            expression = user_input.replace("what is", "").replace("calculate", "")
            result = calculator.invoke(expression)
            print("Agent used Calculator Tool")
            print("AI:", result)

        except:
            print("Error using calculator tool")

    # Weather tool trigger
    elif "weather" in user_input:

        words = user_input.split()
        city = words[-1]

        result = weather.invoke(city)

        print("Agent used Weather Tool")
        print("AI:", result)

    else:

        print("AI: I can help with math calculations or weather queries.")