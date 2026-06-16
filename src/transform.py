## Transform the data by renaming the columns and droping some columns


def transform_data(data):
    print("Transforming the data")
    # Rename the columns
    columns_to_drop = ['lowername']
    data = data.drop(columns=columns_to_drop)

    #Rename columns
    data = data.rename(columns = {'name': 'city'})

    return data
