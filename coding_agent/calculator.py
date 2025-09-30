import sys
import pkg.calculator as calculator
from pkg.render import render

def main():
    calculato = calculator.Calculator()
    if len(sys.argv) <= 4:
        print("Usage: python main.py <num1> <operator> <num2>")
        sys.exit(1)

    expression = ' '.join(sys.argv[1:4])
    try:
        result = calculato.evaluate(expression)
        render(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()