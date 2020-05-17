def clean_data(df):
    df.song = df.song.str.replace(r'\[.*','')
    df.song = df.song.str.lower()
    df.song = df.song.str.replace(r',','')
    df.song = df.song.str.replace('\.+(\(.+\))', '')
    df.song = df.song.str.replace('(\(.+\))\.+', '')
    df.song = df.song.str.replace("'", '')
    df.song = df.song.str.replace("’", '')
    df.song = df.song.str.strip()
    return df