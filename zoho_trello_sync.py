import requests
import time

# 🔐 Replace these with your real credentials
ZOHO_ACCESS_TOKEN = '1000.9b6a59d23a5a31226f618ec02fe5013c.370f23a74e1b3fc362bf180547c460b3'
TRELLO_API_KEY = 'fd0e0fb73bc3306a7807506f70ca8fdc'
TRELLO_API_TOKEN = 'ATTA6910d1572651ee3a9ad8fccfb215d76cec31cad75e51dd6c6886948931dc634c10CE2882'

# Zoho base
ZOHO_HEADERS = {
    "Authorization": f"Zoho-oauthtoken {ZOHO_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def get_recent_deals():
    url = "https://www.zohoapis.com/crm/v2/Deals"
    response = requests.get(url, headers=ZOHO_HEADERS)
    # print  (response.json().get("data", []))
    return response.json().get("data", [])

def filter_target_deals(deals):
    target = []
    for deal in deals:
        
        stage = deal.get("Stage")
        deal_type = deal.get("Type")
        board_id = deal.get("Project_Board_ID__c")
        if stage == "Project Kickoff" and deal_type == "New Implementation Project" and not board_id:
            target.append(deal)
    return target

def create_trello_board(deal_name):
    url = "https://api.trello.com/1/boards/"
    query = {
        "name": f"Project: {deal_name}",
        "key": TRELLO_API_KEY,
        "token": TRELLO_API_TOKEN
    }
    res = requests.post(url, params=query).json()
    return res["id"]

def create_trello_list(board_id, name):
    url = "https://api.trello.com/1/lists"
    query = {
        "name": name,
        "idBoard": board_id,
        "key": TRELLO_API_KEY,
        "token": TRELLO_API_TOKEN
    }
    return requests.post(url, params=query).json()["id"]

def create_trello_card(list_id, name):
    url = "https://api.trello.com/1/cards"
    query = {
        "name": name,
        "idList": list_id,
        "key": TRELLO_API_KEY,
        "token": TRELLO_API_TOKEN
    }
    requests.post(url, params=query)

def update_zoho_deal(deal_id, board_id):
    #print(board_id)
    url = f"https://www.zohoapis.com/crm/v2/Deals/{deal_id}"
    payload = {
        "data": [{
            "Project_Board_ID_c": board_id
        }]
    }
    requests.put(url, headers=ZOHO_HEADERS, json=payload)

def run_sync():
    print("🔄 Checking for matching deals...")
    deals = get_recent_deals()
    targets = filter_target_deals(deals)
    
    for deal in targets:
        deal_name = deal["Deal_Name"]
        deal_id = deal["id"]
        print(f"📌 Processing: {deal_name}")
        
        # Create Trello board
        board_id = create_trello_board(deal_name)
        
        # Create lists
        todo_id = create_trello_list(board_id, "To Do")
        inprog_id = create_trello_list(board_id, "In Progress")
        done_id = create_trello_list(board_id, "Done")
        
        # Add cards to "To Do"
        create_trello_card(todo_id, "Kickoff Meeting Scheduled")
        create_trello_card(todo_id, "Requirements Gathering")
        create_trello_card(todo_id, "System Setup")
        
        # Update Zoho deal with board ID
        update_zoho_deal(deal_id, board_id)
        print(f"✅ Deal updated with board ID: {board_id}")

# Run once or loop
run_sync()
# To run every 5 minutes:
# while True:
#     run_sync()
#     time.sleep(300)