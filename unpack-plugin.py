import json
import argparse
import os


def main():
    parser = argparse.ArgumentParser("Unpacks a packaged tiddlywiki plugin")
    parser.add_argument("plugin_file")
    parser.add_argument("extract_path")
    args = parser.parse_args()

    with open(args.plugin_file) as pfile:
        plugin_file = json.load(pfile)[0]
    extract_path = args.extract_path
    tiddlers = json.loads(plugin_file['text'])['tiddlers']

    for tiddler_name, fields in tiddlers.items():
        text = fields['text']
        del fields['text']
        with open(os.path.join(extract_path, tiddler_name.replace('/', '_') + '.tid'), 'w') as tfile:
            for field_name, field_value in fields.items():
                tfile.write(f'{field_name}: {field_value}\n')
            tfile.write(f'\n\n{text}\n')
    
    del plugin_file['text']
    with open(os.path.join(extract_path, 'plugin.info'), 'w') as info_file:
        json.dump(plugin_file, info_file, indent=4)


if __name__ == '__main__':
    main()
