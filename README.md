
# 🔗 Zoho CRM + Trello Integration

This Python script automates the creation of Trello boards based on specific deal conditions in Zoho CRM. When a deal reaches the "Project Kickoff" stage and is of type "New Implementation Project", the script creates a Trello board, adds standard task lists and cards, and then updates the Zoho deal with the board ID.

---

## 🚀 Features

- Authenticates with Zoho CRM using OAuth access token
- Connects to Trello using API key and token
- Detects deals in Zoho that match specific trigger conditions
- Creates Trello boards with standard lists: "To Do", "In Progress", "Done"
- Adds default cards to the "To Do" list
- Updates the Zoho deal with the Trello board ID in the custom field

---

## 🧰 Technologies

- Python 3
- `requests` library
- `time` library
- Trello REST API
- Zoho CRM v2 REST API

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mariamessam123/flake-tech.git

```

### 2. Install Required Packages

```bash
pip install requests
pip install time
```

### 3. Set Your Credentials

In the script (`zoho_trello_sync.py`), replace the placeholders with your actual credentials:

```python
ZOHO_ACCESS_TOKEN = "your_zoho_access_token"
TRELLO_API_KEY = "your_trello_api_key"
TRELLO_API_TOKEN = "your_trello_api_token"
```

Ensure the Zoho CRM **Deals** module includes a custom text field with this exact API name:

```
Project_Board_ID_c
```

This field will store the Trello board ID.

---

## 🧪 How to Use

### 1. In Zoho CRM, create a deal with:

- **Stage**: `Project Kickoff`
- **Type**: `New Implementation Project`
- **Project_Board_ID_c**: *(leave it blank)*

### 2. Run the Script

```bash
python zoho_trello_sync.py
```

If a matching deal is found, it will:

✅ Create a Trello board  
✅ Add 3 lists (To Do, In Progress, Done)  
✅ Add 3 cards (tasks)  
✅ Update the Zoho deal with the Trello board ID


---

## ❗ Notes

- The Zoho access token expires after 1 hour. You can implement token refreshing if needed.
- Make sure the custom field `Project_Board_ID_c` is **writeable** and not restricted by any workflow or validation rule.
- Use Postman or Python to test updates individually if needed.

---

## 📬 Contact

For questions or improvements, please reach out to **Mariam Essam** via GitHub or LinkedIn.
