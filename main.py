import os

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


def main():
    print("Hello from udemy-class!")
    print(
        os.environ.get("OPENAI_API_KEY")
    )  # Print the OPENAI_API_KEY environment variable


if __name__ == "__main__":
    main()
