import os


root = os.getcwd()

print('1: rembg module')
print('2: clipdrop API')
mode = input('Your choice: ').replace(' ', '').lower()
mode = 1 if mode.replace('module', '') in ['rembg', '', '1'] else 2

if mode != 2:
    from rembg import remove
else:
    import requests


def rembg(image):
    try:
        with open(f'{root}\\input\\{image}', 'rb') as i:
            with open(f'{root}\\output\\{image}', 'wb') as o:
                input = i.read()
                output = remove(input)
                o.write(output)
    except Exception as e:
        print('ERROR:', image, e)
    else:
        print('+', image)
        
def clipdrop(image):
    filetype = image.split('.')[-1]

    r = requests.post('https://clipdrop-api.co/remove-background/v1',
        files={
            'image_file': (
                image, open(f'{root}\\input\\{image}', 'rb'), f'image/{filetype}'
            )
        },
        headers={'x-api-key': open(f"{root}\\YOUR_API_KEY.txt", 'r+').read().strip()}
    )
    if r.ok:
        with open(f'{root}\\output\\{image.replace(filetype, "png")}', 'wb') as f:
            f.write(r.content)
        print('+', image)
    else:
        print('ERROR:', image)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            print('HTTP error: check your clipdrop API key.')
            exit()
        
def main():
    for image in os.listdir(f'{root}\\input'):
        
        if not os.path.isdir(f'{root}\\output'):
            os.mkdir('output')
        if os.path.isfile(f'{root}\\output\\{image}'):
            print(f'ERROR: {image} File already exists.')
        elif image != 'PUT_YOUR_IMAGES_HERE':
            if mode == 2:
                clipdrop(image)
            else:
                rembg(image)
        else:
            try:
                os.remove(f'{root}\\input\\{image}')
            except Exception:
                pass

if __name__ == '__main__':
    main()