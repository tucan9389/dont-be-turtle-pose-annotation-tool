import os
import shutil

path = "/Users/canapio/Project/machine learning/MoT Labs/dataset/180823_dontbeturtle/original/dataset-180823"

# for dirname, dirnames, filenames in os.walk(path):
#     # print path to all subdirectories first.
#     for subdirname in dirnames:
#         print(os.path.join(dirname, subdirname))

# 1. enclose_video.py
# 2. split_video_to_images.py
# 3. make_annotation_json.py
#
# !! annotate on mobile app
#
# 4. mearge_annotations.py

# print path to all filenames.
for filename in os.listdir(path):
    # print(os.path.join(dirname, filename))
    # old_video_path = os.path.join(path, filename)

    # if len(os.path.splitext(filename))==2 and os.path.splitext(filename)[1].lower()==".mov":
        # foldername = os.path.splitext(filename)[0]
        # new_path = os.path.join(path, foldername)
        #
        # # create new path
        # if not os.path.exists(new_path):
        #     os.makedirs(new_path)
        #
        # # move video
        # new_video_path = os.path.join(new_path, filename)
        # os.rename(old_video_path, new_video_path)
        #
        # # create images path
        # images_path = os.path.join(new_path, 'images')
        # print(new_path)
        # if not os.path.exists(images_path):
        #     os.makedirs(images_path)
    if filename == '.DS_Store': continue;
    target_path = os.path.join(path, filename)
    images_path = os.path.join(target_path, 'images')
    if not os.path.exists(images_path):
        os.makedirs(images_path)

    print(images_path)
    for image_file_name in os.listdir(target_path):
        if image_file_name == 'images': continue;
        if filename == '.DS_STORE': continue;

        image_source_file_path = os.path.join(target_path, image_file_name)
        image_destination_file_path = os.path.join(images_path, image_file_name)

        shutil.move(image_source_file_path, image_destination_file_path)