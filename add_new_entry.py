import pandas as pd

def add_new_entry(revenue, year, studio_entertainment, disney_products, disney_parks_resorts, disney_media_networks):
    """
    Add a new data entry to the revenue DataFrame.

    This function accepts values for each column and calculates the 'Total' column,
    and appends the new entry to the DataFrame. If the year already exists, it will ask whether to update or skip.

    Input:
        - revenue: The DataFrame to which the entry will be added.
        - year: The year for the new entry.
        - studio_entertainment: The Studio Entertainment revenue.
        - disney_products: The Disney Products revenue.
        - disney_parks_resorts: The Disney Parks & Resorts revenue.
        - disney_media_networks: The Disney Media Networks revenue.

    Output:
        The new data entry is added or updated in the DataFrame.
    """
    assert isinstance(year, int), "Year should be an integer."
    assert all(isinstance(value, float) for value in [studio_entertainment, disney_products, disney_parks_resorts, disney_media_networks]), "Revenue values should be floats."

    # Calculate the 'Total' column
    total = (
        studio_entertainment
        + disney_products
        + disney_parks_resorts
        + disney_media_networks
    )

    # Create a dictionary with the data
    new_entry = {
        "Year": year,
        "Studio_Entertainment": studio_entertainment,
        "Disney_Products": disney_products,
        "Disney_Parks_Resorts": disney_parks_resorts,
        "Disney_Media_Networks": disney_media_networks,
        "Total": total,
    }

    # Check if the year already exists in the DataFrame
    if year in revenue["Year"].values:
        # Ask the user for the action to take (update or skip)
        action = input(f"The year {year} already exists. Do you want to update it? (yes/no): ")
        if action.lower() == "yes":
            # Update the existing entry
            revenue.loc[revenue["Year"] == year] = new_entry
            revenue = revenue.append(new_entry, ignore_index=True)
            print(f"The data entry for the year {year} has been updated.")
        else:
            print(f"No changes were made for the year {year}.")
    else:
        # Append the new entry to the DataFrame
        revenue = revenue.append(new_entry, ignore_index=True)
        print(f"The data entry for the year {year} has been added to the DataFrame.")

    # Print the updated DataFrame
    return revenue
