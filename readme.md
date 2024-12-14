# Personal Finance Expense Tracker

## Overview

A robust Python-based personal finance management tool that helps users track, analyze, and visualize their spending habits through an intuitive command-line interface.

## Features

- **Expense Logging**: 
  - Add expenses with amount, category, and date
  - Automatic timestamp recording
  - Persistent storage using CSV

- **Financial Insights**:
  - Calculate total expenses
  - Categorize and summarize spending
  - Generate visual expense distribution reports

- **Data Visualization**:
  - Create pie charts showing expense breakdown by category
  - Save visualizations as PNG files

## Prerequisites

- Python 3.7+
- Required Libraries:
  - matplotlib
  - csv (built-in)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install matplotlib
   ```

## Usage

Run the script and select from the following options:

1. **Add Expense**
   - Record new expenses with amount and category
   - Optional date specification

2. **View Total Expenses**
   - See cumulative spending

3. **View Expenses by Category**
   - Breakdown of spending per category

4. **Generate Expense Report**
   - Create a pie chart visualization of expense distribution
   - Saves 'expense_distribution.png'

5. **Exit**
   - Close the application

## Example Workflow

```bash
python expense_tracker.py

--- Personal Expense Tracker ---
1. Add Expense
2. View Total Expenses
3. View Expenses by Category
4. Generate Expense Report
5. Exit

Enter your choice (1-5): 1
Enter expense amount: $45.50
Enter expense category: Groceries
Expense added successfully!
```

## Project Structure

- `Expense` class: Represents individual expense entries
- `ExpenseTracker` class: Manages expense operations
- `main()` function: Provides command-line interface

## Data Persistence

- Expenses stored in `expenses.csv`
- Automatic loading and saving of expense data
- Maintains expense history between application sessions

## Potential Improvements

- Implement date range filtering
- Add expense editing and deletion
- Create more advanced financial reports
- Develop a graphical user interface (GUI)
- Add budget tracking and alerts

## Technologies Used

- Python
- CSV for data storage
- Matplotlib for data visualization

## License

[Specify your license here]

## Contributing

Contributions are welcome! Please submit pull requests or open issues to suggest improvements.