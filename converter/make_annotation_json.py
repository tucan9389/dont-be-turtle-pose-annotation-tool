import io, json, os
from PIL import Image

path = "/Users/canapio/Project/machine learning/MoT Labs/dataset/180823_dontbeturtle/original/dataset-180823"


image_id = 1
for filename in os.listdir(path):
    video_path = os.path.join(path, filename)
    if os.path.isdir(video_path):

        print(video_path)
        images_path = os.path.join(video_path, "images")
        image_files = os.listdir(images_path)

        image_infos = []
        for image_name in image_files:
            if image_name == '.DS_Store': continue;
            image_path = os.path.join(images_path, image_name)

            im = Image.open(image_path)
            img_width, img_height = im.size  # (640, 480)#
            image_info = {
                "file_name": image_name,
                "height": img_height,
                "width": img_width,
                "id": image_id
            }
            image_id = image_id + 1

            image_infos.append(image_info)


        jsondata = {
            "images": image_infos,
            "annotations": [],
            "categories": [{
                'supercategory': 'bust',
                'name': 'body pose',
                'id': 1,
                'keypoints': ["head", "nose", "Rshoulder", "Lshoulder"],
                'skeleton': [[1, 2], [2, 3], [2, 4]]
            }]
        }

        annotation_json_path = os.path.join(video_path, "annotation.json")
        with io.open(annotation_json_path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(jsondata, ensure_ascii=False))