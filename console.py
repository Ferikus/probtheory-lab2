import device

if __name__ == "__main__":
    n = int(input("Enter the number of subdevices (n): "))
    choice = input("Would you like to set the expected (Q) or variance (R)? Enter 'Q' or 'R': ").strip().upper()

    if choice == 'Q':
        Q = float(input("Enter the expected (Q): "))
        device_instance = device.Device(n, expected=Q)
    elif choice == 'R':
        R = float(input("Enter the variance (R): "))
        device_instance = device.Device(n, variance=R)
    else:
        print("Invalid choice. Please enter 'Q' or 'R'.")
        exit()

    k = int(input("Enter the number of random draws (k): "))

    results = device_instance.RandomDraw(k)

    print("Sorted random values:")
    for i, value in enumerate(results, start=1):
        print(f"x({i}) = {value:.4f}")