import os
import json
from pathlib import Path


d_customer = {key.lower(): os.environ[key] for key in ('INSTALLER_NAME',
                                                       'SVC_BASE_INSTALLER',
                                                       'CUSTOMER_TITLE',
                                                       'CUSTOMER_SLUG',
                                                       'ORG_ID', 'TOKEN')}

customer_dir = Path(os.environ['BASE_DIR']) / d_customer.pop('customer_slug')
customer_dir.mkdir()
with open(customer_dir/'customer.json', 'w') as fl:
    json.dump(d_customer, fl, indent=4)
