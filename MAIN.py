from LAGRANGE import lagrange
from NEVILLE import neville
def main():
    print("Hello World!")
    table= [(0, 0), (1, 0.8415), (2, 0.9093), (3, 0.1411), (4, -0.7568), (5, -0.9589), (6, -0.2794)]
    x=2.5
    while True:
        print("\nChoose the method you want to use:")
        print("1. Lagrange Interpolation")
        print("2. Neville Interpolation")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice=="3":
            print("Exiting the program...")
            print("Goodbye!")
            break

        try:
            if choice=="1":
                print("\nLagrange Interpolation:")
                y=lagrange(table,x)
                print( "\nInterpolated value at x =", x, "is y =", y)

            elif choice=="2":
                print("\nNeville Interpolation:")
                y=neville(table,x)
                print( "\nInterpolated value at x =", x, "is y =", y)


            else:
                print("Invalid choice. Please enter a valid choice (1/2/3).")

        except ValueError as e:
            print(f"Error: {ValueError}")

        except Exception as e:

            print(f"An unexpected error occurred: {e}")





if __name__ == "__main__":
    main()
