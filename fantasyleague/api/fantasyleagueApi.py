import requests
from bs4 import BeautifulSoup
from fantasyleague.models import FantasyLeague


def get_fantasyleague_json():
    men_url = "https://www.worldsurfleague.com/athletes/tour/mct?year=2021"
    women_url = "https://www.worldsurfleague.com/athletes/tour/wct?year=2021"
    surfer_stats = {}
    surfer_stats_list = []

    for i in range(2):
        page = requests.get(men_url) if i == 0 else requests.get(women_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        for tr in soup.find_all('tr')[2:]:
            surfer_stats["rank"] = tr.find_all(
                'td', class_="athlete-rank")[0].text
            surfer_stats["name"] = tr.find_all(
                'a', class_="athlete-name")[0].text
            surfer_stats["country_name"] = tr.find_all(
                'span', class_="athlete-country-name")[0].text
            surfer_stats["tour_points"] = tr.find_all(
                'span', class_="tour-points")[0].text
            surfer_stats["athlete_country_flag"] = tr.find_all(
                'span', class_="athlete-country-flag")[0]['data-img-src']
            surfer_stats["athlete_photo"] = tr.find_all(
                'a', class_="headshot")[0]['data-img-src']
            if i == 0:
                surfer_stats["gender"] = "male"
            else:
                surfer_stats["gender"] = "female"

            # print(surfer_stats)
            surfer_stats_list.append(surfer_stats)
            surfer_stats = {}
    # print(surfer_stats_list)
    print(len(surfer_stats_list))
    return surfer_stats_list


def updateFantasyLeague():
    print("inside updateFantasyLeague")
    surfer_stats_list = get_fantasyleague_json()
    if len(surfer_stats_list) != 0:
        print(surfer_stats_list)
        try:
            for surfer_stat in surfer_stats_list:
                fantasy_league = FantasyLeague()
                fantasy_league.rank = surfer_stat['rank']
                fantasy_league.name = surfer_stat['name']
                fantasy_league.country_name = surfer_stat['country_name']
                fantasy_league.tour_points = surfer_stat['tour_points']
                fantasy_league.athlete_country_flag = surfer_stat['athlete_country_flag']
                fantasy_league.athlete_photo = surfer_stat['athlete_photo']
                fantasy_league.gender = surfer_stat['gender']
                fantasy_league.save()
        except:
            return None
