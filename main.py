from quantum_adder import quantum_4bit_adder

def main():
    test_cases = [(15, 15), (8, 7)]
    for a, b in test_cases:
        result = quantum_4bit_adder(a, b)
        print(f"Quantum 4-Bit Addition: {a} + {b} = {result}")
        
if __name__ == "__main__":
    main()

