import os

from download_request import DownloadFile

if __name__ == "__main__":
    save_data_path = os.getenv("STG_DATA_PATH")
    files = [
        DownloadFile(
            url=(
                "https://www.medellin.gov.co/mapas/rest/services/"
                "ServiciosPlaneacion/POT48_Base/MapServer/3/query?"
                "where=1%3D1&outFields=*&outSR=4326&f=json"
            ),
            filepath=f"{save_data_path}/comunas.geojson",
        ),
        DownloadFile(
            url="http://medata.gov.co/node/24723/download",
            filepath=f"{save_data_path}/homicidio.csv",
        ),
        DownloadFile(
            url="http://medata.gov.co/node/24728/download",
            filepath=f"{save_data_path}/hurto_a_persona.csv",
        ),
    ]
    for file in files:
        file.request_data()
        file.save()
