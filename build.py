from staticjinja import Site

SITENAME = "Maximos Nikiforakis"
DEFAULT_LANG = "en"

experience = [
    {
        "firm": "Dialectica",
        "href": "https://dialecticanet.com/",
        "location": "Athens, Greece",
        "start_date": "12/2024",
        "end_date": None,
        "title": "Backend Software Engineer",
        "technologies": ["Ruby", "Hanami"],
        "phases": [
            {
                "title": "Backend Software Engineer",
                "description": ""
            }
        ]
    },
    {
        "firm": "Skroutz",
        "href": "https://www.skroutz.gr/?lang=en",
        "location": "Athens, Greece",
        "start_date": "10/2023",
        "end_date": "11/2024",
        "title": "Backend Software Engineer",
        "technologies": ["Ruby on Rails"],
        "phases": [
            {
                "title": "Backend Software Engineer",
                "description": """I am part of the Marketplace team where I work on 
                adding new features to the ecommerce platform and integrating new
                 3rd-party services.""",
            }
        ],
    },
    {
        "firm": "The Signal Group",
        "href": "https://www.thesignalgroup.com/",
        "location": "Athens, Greece",
        "start_date": "01/2021",
        "end_date": "08/2023",
        "title": "Software Engineer",
        "technologies": [
            "Python",
            "microservices",
            "Docker",
            "FastAPI",
            "Azure AKS",
        ],
        "phases": [
            {
                "title": "Software Engineer",
                "description": """I designed, developed and maintained a series of 
                microservices related to shipping market insights. I also contributed to
                some of the company's internal tools as a maintainer of a Python library.""",
            },
            {
                "title": "Shipping Intelligence Intern",
                "description": """I was part of the Shipping Intelligence team where we
                worked on optimizing the commercial performance of the company's fleet.""",
            },
        ],
    },
    {
        "firm": "Centre for Research and Technology Hellas",
        "href": "https://www.certh.gr/root.en.aspx",
        "location": "Thessaloniki, Greece",
        "start_date": "06/2020",
        "end_date": "12/2020",
        "title": "Researcher",
        "technologies": ["MATLAB", "Excel VBA"],
        "phases": [
            {
                "title": "Researcher",
                "description": """I worked in the Lab of Environmental Fuels and 
                Hydrocarbons on creating simulation models for the Fluid Catalytic 
                Cracking process.""",
            }
        ],
    },
]

projects = [
    {
        "title": "property-utils",
        "description": """A Python library that makes physical 
        property programming easy. It aims at providing an intuitive and simple API
        for scientists with little programming experience.""",
        "link": "https://maxcode123.github.io/property-utils/",
        "vbox": "0 0 32 32",
        "path": "M13.275 15.88h5.417c1.508 0 2.712-1.241 2.712-2.756v-5.164c0-1.47-1.24-2.574-2.712-2.819-0.932-0.155-1.898-0.226-2.825-0.221s-1.813 0.083-2.592 0.221c-2.295 0.405-2.712 1.254-2.712 2.819v2.067h5.423v0.689h-7.459c-1.576 0-2.956 0.947-3.388 2.75-0.498 2.066-0.52 3.355 0 5.512 0.385 1.606 1.306 2.75 2.882 2.75h1.865v-2.478c0-1.79 1.549-3.369 3.388-3.369zM12.933 8.649c-0.562 0-1.018-0.461-1.018-1.030 0-0.572 0.455-1.037 1.018-1.037 0.56 0 1.018 0.465 1.018 1.037 0 0.57-0.457 1.030-1.018 1.030zM26.826 13.465c-0.389-1.569-1.133-2.75-2.712-2.75h-2.035v2.408c0 1.867-1.583 3.439-3.388 3.439h-5.417c-1.484 0-2.712 1.27-2.712 2.756v5.164c0 1.47 1.278 2.334 2.712 2.756 1.717 0.505 3.363 0.596 5.417 0 1.365-0.395 2.712-1.191 2.712-2.756v-2.067h-5.417v-0.689h8.129c1.576 0 2.163-1.099 2.712-2.75 0.566-1.699 0.542-3.332 0-5.512zM19.033 23.794c0.562 0 1.018 0.461 1.018 1.030 0 0.572-0.456 1.037-1.018 1.037-0.56 0-1.018-0.465-1.018-1.037 0-0.57 0.457-1.030 1.018-1.030z",
    },
    {
        "title": "unittest-extensions",
        "description": """A minimal Python library that aims to simplify behavioral 
        testing with unittest.""",
        "link": "https://github.com/Maxcode123/unittest-extensions",
        "vbox": "0 0 32 32",
        "path": "M13.275 15.88h5.417c1.508 0 2.712-1.241 2.712-2.756v-5.164c0-1.47-1.24-2.574-2.712-2.819-0.932-0.155-1.898-0.226-2.825-0.221s-1.813 0.083-2.592 0.221c-2.295 0.405-2.712 1.254-2.712 2.819v2.067h5.423v0.689h-7.459c-1.576 0-2.956 0.947-3.388 2.75-0.498 2.066-0.52 3.355 0 5.512 0.385 1.606 1.306 2.75 2.882 2.75h1.865v-2.478c0-1.79 1.549-3.369 3.388-3.369zM12.933 8.649c-0.562 0-1.018-0.461-1.018-1.030 0-0.572 0.455-1.037 1.018-1.037 0.56 0 1.018 0.465 1.018 1.037 0 0.57-0.457 1.030-1.018 1.030zM26.826 13.465c-0.389-1.569-1.133-2.75-2.712-2.75h-2.035v2.408c0 1.867-1.583 3.439-3.388 3.439h-5.417c-1.484 0-2.712 1.27-2.712 2.756v5.164c0 1.47 1.278 2.334 2.712 2.756 1.717 0.505 3.363 0.596 5.417 0 1.365-0.395 2.712-1.191 2.712-2.756v-2.067h-5.417v-0.689h8.129c1.576 0 2.163-1.099 2.712-2.75 0.566-1.699 0.542-3.332 0-5.512zM19.033 23.794c0.562 0 1.018 0.461 1.018 1.030 0 0.572-0.456 1.037-1.018 1.037-0.56 0-1.018-0.465-1.018-1.037 0-0.57 0.457-1.030 1.018-1.030z",
    },
    {
        "title": "syntactes",
        "description": "A simple Python parser generator.",
        "link": "https://github.com/Maxcode123/syntactes",
        "vbox": "0 0 32 32",
        "path": "M13.275 15.88h5.417c1.508 0 2.712-1.241 2.712-2.756v-5.164c0-1.47-1.24-2.574-2.712-2.819-0.932-0.155-1.898-0.226-2.825-0.221s-1.813 0.083-2.592 0.221c-2.295 0.405-2.712 1.254-2.712 2.819v2.067h5.423v0.689h-7.459c-1.576 0-2.956 0.947-3.388 2.75-0.498 2.066-0.52 3.355 0 5.512 0.385 1.606 1.306 2.75 2.882 2.75h1.865v-2.478c0-1.79 1.549-3.369 3.388-3.369zM12.933 8.649c-0.562 0-1.018-0.461-1.018-1.030 0-0.572 0.455-1.037 1.018-1.037 0.56 0 1.018 0.465 1.018 1.037 0 0.57-0.457 1.030-1.018 1.030zM26.826 13.465c-0.389-1.569-1.133-2.75-2.712-2.75h-2.035v2.408c0 1.867-1.583 3.439-3.388 3.439h-5.417c-1.484 0-2.712 1.27-2.712 2.756v5.164c0 1.47 1.278 2.334 2.712 2.756 1.717 0.505 3.363 0.596 5.417 0 1.365-0.395 2.712-1.191 2.712-2.756v-2.067h-5.417v-0.689h8.129c1.576 0 2.163-1.099 2.712-2.75 0.566-1.699 0.542-3.332 0-5.512zM19.033 23.794c0.562 0 1.018 0.461 1.018 1.030 0 0.572-0.456 1.037-1.018 1.037-0.56 0-1.018-0.465-1.018-1.037 0-0.57 0.457-1.030 1.018-1.030z",
    }
]

links = [
    {
        "href": "https://github.com/Maxcode123",
        "text": "GitHub",
        "path_d": "M12 0a12 12 0 1 0 0 24 12 12 0 0 0 0-24zm3.163 21.783h-.093a.513.513 0 0 1-.382-.14.513.513 0 0 1-.14-.372v-1.406c.006-.467.01-.94.01-1.416a3.693 3.693 0 0 0-.151-1.028 1.832 1.832 0 0 0-.542-.875 8.014 8.014 0 0 0 2.038-.471 4.051 4.051 0 0 0 1.466-.964c.407-.427.71-.943.885-1.506a6.77 6.77 0 0 0 .3-2.13 4.138 4.138 0 0 0-.26-1.476 3.892 3.892 0 0 0-.795-1.284 2.81 2.81 0 0 0 .162-.582c.033-.2.05-.402.05-.604 0-.26-.03-.52-.09-.773a5.309 5.309 0 0 0-.221-.763.293.293 0 0 0-.111-.02h-.11c-.23.002-.456.04-.674.111a5.34 5.34 0 0 0-.703.26 6.503 6.503 0 0 0-.661.343c-.215.127-.405.249-.573.362a9.578 9.578 0 0 0-5.143 0 13.507 13.507 0 0 0-.572-.362 6.022 6.022 0 0 0-.672-.342 4.516 4.516 0 0 0-.705-.261 2.203 2.203 0 0 0-.662-.111h-.11a.29.29 0 0 0-.11.02 5.844 5.844 0 0 0-.23.763c-.054.254-.08.513-.081.773 0 .202.017.404.051.604.033.199.086.394.16.582A3.888 3.888 0 0 0 5.702 10a4.142 4.142 0 0 0-.263 1.476 6.871 6.871 0 0 0 .292 2.12c.181.563.483 1.08.884 1.516.415.422.915.75 1.466.964.653.25 1.337.41 2.033.476a1.828 1.828 0 0 0-.452.633 2.99 2.99 0 0 0-.2.744 2.754 2.754 0 0 1-1.175.27 1.788 1.788 0 0 1-1.065-.3 2.904 2.904 0 0 1-.752-.824 3.1 3.1 0 0 0-.292-.382 2.693 2.693 0 0 0-.372-.343 1.841 1.841 0 0 0-.432-.24 1.2 1.2 0 0 0-.481-.101c-.04.001-.08.005-.12.01a.649.649 0 0 0-.162.02.408.408 0 0 0-.13.06.116.116 0 0 0-.06.1.33.33 0 0 0 .14.242c.093.074.17.131.232.171l.03.021c.133.103.261.214.382.333.112.098.213.209.3.33.09.119.168.246.231.381.073.134.15.288.231.463.188.474.522.875.954 1.145.453.243.961.364 1.476.351.174 0 .349-.01.522-.03.172-.028.343-.057.515-.091v1.743a.5.5 0 0 1-.533.521h-.062a10.286 10.286 0 1 1 6.324 0v.005z",
        "vbox": "0 0 24 24",
    },
    {
        "href": "https://www.linkedin.com/in/maximos-nikiforakis/",
        "text": "LinkedIn",
        "path_d": "M19.959 11.719v7.379h-4.278v-6.885c0-1.73-.619-2.91-2.167-2.91-1.182 0-1.886.796-2.195 1.565-.113.275-.142.658-.142 1.043v7.187h-4.28s.058-11.66 0-12.869h4.28v1.824l-.028.042h.028v-.042c.568-.875 1.583-2.126 3.856-2.126 2.815 0 4.926 1.84 4.926 5.792zM2.421.026C.958.026 0 .986 0 2.249c0 1.235.93 2.224 2.365 2.224h.028c1.493 0 2.42-.989 2.42-2.224C4.787.986 3.887.026 2.422.026zM.254 19.098h4.278V6.229H.254v12.869z",
        "vbox": "-2 -2 24 24",
    },
    # {
    #     "href": "something",
    #     "text": "Blog",
    #     "path_d": "M22 7.662l1-1V18h-7v4.745L11.255 18H1V2h16.763l-1 1H2v14h9.668L15 20.331V17h7zm1.657-5.192a.965.965 0 0 1 .03 1.385l-9.325 9.324-4.097 1.755a.371.371 0 0 1-.487-.487l1.755-4.097 9.31-9.309a.98.98 0 0 1 1.385 0zm-10.1 9.965l-1.28-1.28-.961 2.24zm7.243-7.11l-1.414-1.413-6.469 6.47 1.414 1.413zm1.865-2.445l-.804-.838a.42.42 0 0 0-.6-.006l-1.168 1.168 1.414 1.415 1.152-1.152a.42.42 0 0 0 .006-.587z",
    #     "vbox": "0 0 24 24",
    # },
]

mail = {
    "mail": "nikiforos@live.co.uk",
    "path_d": "M1 3.5l.5-.5h13l.5.5v9l-.5.5h-13l-.5-.5v-9zm1 1.035V12h12V4.536L8.31 8.9H7.7L2 4.535zM13.03 4H2.97L8 7.869 13.03 4z",
    "path_d2": "M1 3.5l.5-.5h13l.5.5v9l-.5.5h-13l-.5-.5v-9zm1 1.035V12h12V4.536L8.31 8.9H7.7L2 4.535zM13.03 4H2.97L8 7.869 13.03 4z",
    "vbox": "0 0 16 16",
}


blogs = [
    {
        "title": "C for Python",
        "subtitle": "Building a dictionary type",
        "date": "Oct 15, 2024",
        "link": "https://medium.com/@nikiforos_59437/c-for-python-building-a-dictionary-type-e09146ef052f",
    },
    {
        "title": "Python: Concise unit tests",
        "subtitle": "Testing with unittest-extensions",
        "date": "Feb 24, 2024",
        "link": "https://medium.com/@nikiforos_59437/python-concise-unit-tests-fe4b5c0ebebd",
    },
]

if __name__ == "__main__":
    site = Site.make_site(env_globals=locals(), outpath="output")
    site.render(use_reloader=True)
