import requests

areaList = ['Arun', 'Allerdale']

urlTemplate = "https://coronavirus.data.gov.uk/api/v1/data?filters=areaType=ltla;areaName={AreaPlaceHolder}&structure=%7B%22areaType%22:%22areaType%22,%22areaName%22:%22areaName%22,%22areaCode%22:%22areaCode%22,%22date%22:%22date%22,%22newCasesBySpecimenDateAgeDemographics%22:%22newCasesBySpecimenDateAgeDemographics%22,%22newFirstEpisodesBySpecimenDateAgeDemographics%22:%22newFirstEpisodesBySpecimenDateAgeDemographics%22,%22newReinfectionsBySpecimenDateAgeDemographics%22:%22newReinfectionsBySpecimenDateAgeDemographics%22%7D&format=json"

for area in areaList:
    r = requests.get(urlTemplate.format(AreaPlaceHolder = area))
    file = open('{area}.json'.format(area=area), 'w')
    file.write(r.text)
    file.close()


