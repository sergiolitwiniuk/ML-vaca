def json_to_df(path):       #convierte datos json del etiquetado de imagenes a formato csv, por @AbhishekKumar

    from pandas.io.json import json_normalize
    import json
    import pandas as pandas

    final_df = pd.DataFrame()

    #json a df
    for json_file in glob.glob(path + '/*.json'):
        with open(json_file) as f:
            data = json.load(f)
            curr_df = json_normalize(data, 'arr_boxes' ,['file_name'])
            final_df = pd.concat([final_df,curr_df])
    return final_df

    # df to csv
    for label_path in ['train_labels', 'test_labels']:
        image_path = os.path.join(os.getcwd(), label_path)
        df = json_to_df(label_path)
        df.to_csv(f'{label_path}.csv', index=None)
        print(f'Succesfully converted {label_path} xml to csv')


