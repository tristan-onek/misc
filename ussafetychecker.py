# Signal Variables
disableSignal = True

# Example values (could be replaced with real-time data)
dhsntas = False  # Department of Homeland Safety
osintDEFCON = 3  # Most recent common DEFCON level from OSINT sources
vix = 10  # Just taking an example VIX level

# Define threshold conditions for each parameter
defcon_threshold = 2  # DEFCON level should be greater than this to disable the signal
vix_threshold = 40    # VIX level should be greater than this to disable the signal

# Signal Decision Logic with try/except for error handling
def should_disable_signal(dhsntas, osintDEFCON, vix, defcon_threshold, vix_threshold):
    try:
        # Validate that values are within expected types and ranges
        if not isinstance(dhsntas, bool):
            raise ValueError("dhsntas must be a boolean.")
        if not isinstance(osintDEFCON, int) or osintDEFCON < 1 or osintDEFCON > 5:
            raise ValueError("osintDEFCON must be an integer between 1 and 5.")
        if not isinstance(vix, (int, float)) or vix < 0:
            raise ValueError("vix must be a positive integer or float.")

        # Logic to disable the signal based on thresholds
        if not dhsntas and osintDEFCON > defcon_threshold and vix < vix_threshold:
            return False  # Conditions are met, so disable the signal

    except ValueError as e:
        print(f"Error in input data: {e}")
        return True  # Return True to keep the signal disabled in case of error

    return True  # Default, in case conditions are not met

# Apply signal logic
disableSignal = should_disable_signal(dhsntas, osintDEFCON, vix, defcon_threshold, vix_threshold)

# Next steps
if not disableSignal:
    # Send Signal onward to the next part of the system
    print("Signal is enabled, proceed to next part of the system.")
else:
    print("Signal is disabled, awaiting conditions.")
