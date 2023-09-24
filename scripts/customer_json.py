import os
import json
from pathlib import Path


d_customer = {key.lower(): os.environ[key] for key in ('INSTALLER_NAME',
                                                       'SVC_BASE_INSTALLER',
                                                       'CUSTOMER_TITLE',
                                                       'ORG_ID', 'TOKEN')}
# Customer slug obtained from customer_title + org_id
customer_slug = (d_customer['customer_title'].lower().replace(' ', '-') + '_' +
                 d_customer['token'][:5])
customer_dir = Path(os.environ['BASE_DIR']) / customer_slug
customer_dir.mkdir()
with open(customer_dir/'customer.json', 'w') as fl:
    json.dump(d_customer, fl, indent=4)
    fl.write('\n')
