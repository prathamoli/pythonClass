profiles = [{'name':'ram','photo':'url','education':[{'college':'xyz','year':2012},{'college':'abc','year':2018},{'college':'ytx','year':2020}]},{'name':'ram','photo':'url','education':[{'college':'xyz','year':2012},{'college':'abc','year':2018},{'college':'ytx','year':2020}]}]

for profile in profiles:
    name = profile.get("name")
    photo = profile.get("photo")
    education = profile.get("education")
    for key in education:
        college = key.get("college")
        year = key.get("year")
        print("college ",college)
        print("year",year)
    print(name,photo,education)


