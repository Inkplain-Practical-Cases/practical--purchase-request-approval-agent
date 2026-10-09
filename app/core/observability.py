# Structured audit events never log justification, token or personal details.
import json
import logging

logger=logging.getLogger("northstar.purchase")

def service_log_approval_event(event:str, request_id:int, state:str, version:int)->None:
    logger.info(json.dumps({"event":event,"request_id":request_id,"state":state,"version":version}))
