from hbim_open_api_client import Client, types
from hbim_open_api_client.models import UserPublic, UserSchema, BodyUpFileUploadFilePost
from hbim_open_api_client.api.default import create_user_users_post, delete_user_users_id_delete, download_file_download_file_file_id_get
from hbim_open_api_client.types import Response

import datetime

client = Client(base_url="http://127.0.0.1:8000/")
# client.__exit__()

with client as client:
    user_info = UserSchema(
        "ffribeiro2",
        "Fernando Ferraz Ribeiro",
        "ffribeir2o@gmail.com",
        "23415",
        "Mestre",
        datetime.date(1975, 9, 2)
    )

    my_data = create_user_users_post.sync(client=client, body= user_info)

    print(my_data)

# with client as client:
#     my_data = delete_user_users_id_delete.sync(client=client, id = 4)
#     print(my_data)


# response = download_file_download_file_file_id_get.sync_detailed(client=client, file_id=1)
