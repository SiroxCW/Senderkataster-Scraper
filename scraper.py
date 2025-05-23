
from requests import get
import logging
import json
from sys import exit

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_all_senders() -> dict:
    res = get("https://www.senderkataster.at/backend/data/getconfig.php")
    if res.status_code != 200:
        logging.error(f"Failed to fetch sender data. Status code: {res.status_code}")
        exit(1)
    return res.json()

def get_sender_details(sender_id: int, layer: int) -> dict:
    res = get(f"https://www.senderkataster.at/backend/data/getdetails.php?layer={layer}&sender_id={sender_id}")
    if res.status_code != 200:
        logging.error(f"Failed to fetch details for sender_id {sender_id} on layer {layer}. Status code: {res.status_code}")
        return {}
    return res.json()

if __name__ == '__main__':
    senders_dict = get_all_senders()
    total_senders = len(senders_dict["data"])
    logging.info(f"Found {total_senders} senders.")
    save_interval = max(1, total_senders // 10)
    for index, sender in enumerate(senders_dict["data"]):
        sender_details = get_sender_details(sender_id=sender["sender_id"], layer=sender["layer"])
        sender["details"] = sender_details
        print(f"\rGetting details from senders...   {round((100 / total_senders) * (index + 1), 3):<7.3f}%", end="", flush=True)
        if (index + 1) % save_interval == 0 or (index + 1) == total_senders:
            with open("senderkataster.json", "w", encoding="utf-8") as f:
                json.dump(senders_dict, f, ensure_ascii=False, indent=2)

    print()
    logging.info("Operation done!")
