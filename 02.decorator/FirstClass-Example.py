import requests as req
from bs4 import BeautifulSoup as bs


def edge_course():
    res = req.get("https://davelee-fun.github.io/blog/crawl_html_css.html")
    soup = bs(res.content, "html.parser")

    course_list = soup.select("ul#hobby_course_list > li > a")
    courses = []
    for course in course_list:
        courses.append(course.get_text())

    def _func(prefix):
        for course in courses:
            print("{} {}".format(prefix, course))

    return _func


edge_course()("●")
