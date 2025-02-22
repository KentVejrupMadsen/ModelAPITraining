from ultralytics \
    import YOLO

import requests

from tqdm import tqdm

from credentials \
    import APICredentials

from io import BytesIO
from PIL import Image

api = APICredentials()

def generateHeader():
    return {
        'Authorization': api.getTokenHeaderString()
    }

def main():
    global api

    maximum_size: int = 50
    limit: int = 50
    offset: int = 0

    all_tasks: list = list()
    size_of_all_tasks: int = 0

    while True:
        size_of_all_tasks = len(all_tasks)
        
        if size_of_all_tasks >= maximum_size:
            break

        response = requests.get(
            str(
                api.getURI() + 
                '/api/projects/1/tasks' + 
                '?limit=' + str(limit) + 
                '&offset=' + str(offset)
            ),
            headers = generateHeader()
        )

        current_result = response.json()
        all_tasks.extend(current_result)
        
        if not current_result:
            break

        offset = offset + limit
    
    annotation_process(
        all_tasks=all_tasks
    )

def download_image(task):
    global api

    appendix = task['data']['image']

    full_url = api.getURI() + appendix
    header = generateHeader()

    response = requests.get(
        full_url, 
        headers=header
    )

    if not (response.status_code == 200):
        return None

    return Image.open(
        BytesIO(
            response.content
        )
    )

def annotation_process(
    all_tasks: list
):
    model = YOLO(
        '/mnt/c/Users/Kentv/Desktop/RavenAPI/Data/model.pt',
        task='detect',
        verbose=False
    )

    all_annotations: list = list()

    for idx in tqdm(
        range(len(all_tasks))
    ):
        selected_task = all_tasks[idx]
        image = download_image(selected_task)

        if not(image is None):
            results = model.predict(
                source = image, 
                verbose         = False,
                stream_buffer   = True
            )
            annotations: list = list()

            for result in results:
                xywh = result.boxes.xywh
                cls_ids = result.boxes.cls
                confidence = result.boxes.conf

                annotations.append({
                    'xywh': xywh.cpu().numpy()[0],
                    'class': str(
                        replaceWithToken(
                            result.names, 
                            cls_ids.cpu()[0].item())
                    ),
                    'confidence': float(
                        confidence.cpu()[0].item()
                    )
                })
            
            all_annotations.append(
                annotations
            )
    

                
            

def replaceWithToken(
    class_names, 
    id
) -> str:
    returnable = int(id)

    for key in class_names.keys():
        if key == id:
            returnable = class_names[key]

    return returnable

if __name__ == '__main__':
    main()
