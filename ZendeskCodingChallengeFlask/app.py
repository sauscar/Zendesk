import unittest
from flask import Flask, render_template, request
import requests
import pdb

app = Flask(__name__, static_folder="static/css")
pages = None
glo_pages_number = None
global_password = None
global_user = None
global_subdomain = None


def create_pages(url, user, pw, headers):

    page_content = []
    pages = []
    while url:
        r = requests.get(
            url,
            auth=(user, pw),
            headers=headers,
        )
        content = r.json()
        tickets = content["tickets"]
        for ticket in tickets:
            vals = [
                ticket["id"],
                ticket["requester_id"],
                ticket["subject"],
                ticket["type"],
                ticket["priority"],
                ticket["status"],
                ticket["created_at"],
            ]
            page_content.append(vals)
        pages.append(page_content)
        page_content = []

        if r.status_code != 200:
            if r.status_code == 401 or 422:
                status = "Could not authenticate you. Check your email address or register."
                return render_template("error", feedback=status)
            else:
                status = "Problem with the request. Status " + str(r.status_code)
                return render_template("error", feedback=status)
        else:
            status = pages
        if content["meta"]["has_more"]:
            url = content["links"]["next"]
        else:
            url = None
    return status


@app.route("/get_tickets", methods=["GET"])
def handle_form():
    global pages
    global glo_pages_number
    global global_user
    global global_password
    global global_subdomain
    status = ""
    # print("This is the request:", app.request)

    if request.method == "GET":
        user = global_user
        pw = global_password
        url = "https://" + global_subdomain + ".zendesk.com/api/v2/tickets.json?page[size]=25"
        headers = {"content-type": "application/json"}
        page_content = []
        pages = []

        status = create_pages(url, user, pw, headers)
        pages = status
        pages_number = len(status)
        glo_pages_number = pages_number
        status = status[0]

        return render_template("index.html", feedback=status, number=pages_number)


@app.route("/retrieve_page", methods=["POST"])
def get_page():
    global pages

    index = request.form["submit_button"]

    pages_number = len(pages)
    status = pages[int(index) - 1]
    return render_template("index.html", feedback=status, number=pages_number)


@app.route("/single_ticket", methods=["POST"])
def redirect():
    global glo_pages_number
    global global_user
    global global_password
    global global_subdomain
    ticket_id = request.form["id"]
    user = global_user
    pw = global_password
    url = "https://" + global_subdomain + ".zendesk.com/api/v2/tickets/" + ticket_id + ".json"
    headers = {"content-type": "application/json"}
    r = requests.get(
        url,
        auth=(user, pw),
        headers=headers,
    )
    if r.status_code != 200:
        if r.status_code == 401 or r.status_code == 422:
            status = "Could not authenticate you. Check your email address or register."
            return render_template("error", feedback=status)
        else:
            status = (
                "Problem with the request. Status "
                + str(r.status_code)
                + ". Please make sure you click the ID number of ticket."
            )
            return render_template("error.html", feedback=status)

    content = r.json()["ticket"]
    vals = [
        content["raw_subject"],
        content["description"],
        content["requester_id"],
        content["created_at"],
        content["status"],
    ]
    status = vals

    return render_template("ticket.html", feedback=status)


@app.route("/nav_back", methods=["POST"])
def nav():
    global pages
    global glo_pages_number
    return render_template("index.html", feedback=pages[0], number=glo_pages_number)


# @app.route("/css/<filename>")
# def send_css(filename):

#     # return app.static_file(filename, root="static/css")
#     return app.send_static_file(filename, root="static/css")


app.run(host="localhost", port=8080, debug=False)
