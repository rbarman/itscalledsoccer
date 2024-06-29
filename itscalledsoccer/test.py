from client import AmericanSoccerAnalysis
import requests
from pydantic import  ValidationError
from typing import List, Optional
import json
from models import Managers


entity_to_model = {
    "managers": Managers
}


if __name__ == '__main__':

    session = requests.session()
    url = 'https://app.americansocceranalysis.com/api/v1/nwsl/managers'
    response = session.get(url)
    json_response = json.dumps(response.json())

    entity = url.split('/')[-1]
    model = entity_to_model.get(entity)
    
    try:
        validated_response = model.model_validate_json(json_response)
    except ValidationError as e:
        print(f"Validation error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

