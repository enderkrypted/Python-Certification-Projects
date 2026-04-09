

def add_setting(settings, pair):
    # Unpack the tuple
    key, value = pair
    # Convert both to lowercase
    key, value = key.lower(), value.lower()
    
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    # Add to dictionary
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings, pair):
    key, value = pair
    key, value = key.lower(), value.lower()
    
    if key in settings:
        # Update the existing value
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    # Standardize the key to lowercase
    key = key.lower()
    
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    
    return "Setting not found!"


def view_settings(settings):
    # Check for empty dictionary
    if not settings:
        return "No settings available."
    
    # Build the display string
    result = "Current User Settings:\n"
    for key, value in settings.items():
        # Capitalize key for the "Front-End" display
        result += f"{key.capitalize()}: {value}\n"
        
    return result

# --- Testing Section ---
# 1. Create the dictionary
test_settings = {}

# 2. Populate it with values to pass the final requirement
add_setting(test_settings, ("theme", "dark"))
add_setting(test_settings, ("language", "english"))
add_setting(test_settings, ("notifications", "enabled"))

# 3. Final display
print(view_settings(test_settings))
