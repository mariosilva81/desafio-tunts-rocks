from api.connection import (
    SAMPLE_RANGE_NAME,
    SAMPLE_SPREADSHEET_ID,
    spreadsheet_values,
    update_spreadsheet,
)
from spreadsheet.calc import calculate_and_update


# Main function
def main():
    # Authenticate with Google Sheets API to get values
    values = spreadsheet_values()

    # Calculate and update the values list
    updated_values = calculate_and_update(values)

    # Update the spreadsheet with the updated values
    update_spreadsheet(
        SAMPLE_SPREADSHEET_ID,
        SAMPLE_RANGE_NAME,
        updated_values
    )


if __name__ == "__main__":
    main()
