import requests
import os

path = os.getcwd()
dir_list = os.listdir(f'{path}\\input')

for image in dir_list:
    print('.', image)
    
    if os.path.isfile(f'{path}\\output\\{image}'):
        print(f'ERROR: {image} File already exists.')
    else:
        filetype = image.split('.')[-1]

        r = requests.post('https://clipdrop-api.co/remove-background/v1',
            files={
                'image_file': (
                    image, open(f'{path}\\input\\{image}', 'rb'), f'image/{filetype}'
                )
            },
            headers={'x-api-key': open(f"{path}\\YOUR_API_KEY.txt", 'r+').read().strip()}
        )
        if r.ok:
            with open(f'{path}\\output\\{image.replace(filetype, "png")}', 'wb') as f:
                f.write(r.content)
            print('+', image)
        else:
            r.raise_for_status()
            print('ERROR:', image)