import bs4
import requests

kills_url = "https://apex.tracker.gg/apex/leaderboards/origin/Kills?page=1"
pistol_url = "https://apex.tracker.gg/apex/leaderboards/origin/PistolKills"
shotgun_url = "https://apex.tracker.gg/apex/leaderboards/origin/ShotgunKills"
smg_url = "https://apex.tracker.gg/apex/leaderboards/origin/SmgKills"
ar_url = "https://apex.tracker.gg/apex/leaderboards/origin/ArKills"
lmg_url = "https://apex.tracker.gg/apex/leaderboards/origin/LmgKills"
sniper_url = "https://apex.tracker.gg/apex/leaderboards/origin/SniperKills"


def get_soup_from_url(url):
    r = requests.get(url)
    r.raise_for_status()
    return bs4.BeautifulSoup(r.text, 'html.parser')


def get_soup_from_html_file(filename):
    with open(filename) as f:
        page_html = f.read()
    return bs4.BeautifulSoup(page_html, 'html.parser')


def get_top_10(soup):
    test = soup.select("tbody tr")
    top10 = []
    for i in range(1, 11):
        name = test[i].select("td")[1].select("a")[0].getText()
        kills = test[i].select("td")[2].getText()
        top10.append({"name": name, "kills": kills, "place": i})
    return top10


def print_top_10(top10):
    for x in top10:
        print("Place:", x["place"])
        print("Name:", x["name"])
        print("Kills:", x["kills"], "\n")

if __name__ == "__main__":
    print("Top 10 Ar Kills")
    ar_kills = get_top_10(get_soup_from_html_file("arKills.html"))
    print_top_10(ar_kills)

    print("----------------------------------------------\n")

    print("Top 10 Kills")
    kills = get_top_10(get_soup_from_html_file("kills.html"))
    print_top_10(kills)
