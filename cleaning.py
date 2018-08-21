home_folder = 'C:\\Users\\Flor\\Downloads\\insurance'
files = [
    "\\instagram\\insurance_instagram_grafos_comments.csv",
    "\\twitter\\insurance_twitter_grafos_auto.csv",
    "\\twitter\\insurance_twitter_grafos_mentions.csv",
    "\\twitter\\insurance_twitter_grafos_quote.csv",
    "\\twitter\\insurance_twitter_grafos_reply.csv",
    "\\twitter\\insurance_twitter_grafos_retweet.csv"
]
unique_outfile = '\\insurance_grafos.csv'
with open(home_folder + unique_outfile, 'w') as outFile:
    header = "ssnn,interaccion,target,source,weight\n"
    outFile.writelines(header)
    for File in files:
        print(File)
        parts = File.split('_')
        ssnn = parts[1]
        interaccion = parts[-1].replace('.csv', '')
        with open(home_folder+File, 'r') as inFile:
            print(inFile.readline())
            for line in inFile.readlines():
                Line = line.lower().replace('\n', '').split(',')
                target, source, weight = Line[0], Line[1], Line[2]
                if source == '':
                    source = target
                if weight == '':
                    weight = 1
                new_line = "{},{},{},{},{}\n".format(ssnn, interaccion, target, source, weight)
                outFile.writelines(new_line)
