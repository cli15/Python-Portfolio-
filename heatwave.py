#Christina
#Heatwave
#filter data fromn a set

#Challenge 1
# The dates as strings
july_days = [ "July 1", "July 2", "July 3", "July 4", "July 5", "July 6", "July 7", "July 8", "July 9", "July 10", "July 11", "July 12", "July 13", "July 14", "July 15", "July 16", "July 17", "July 18", "July 19", "July 20", "July 21", "July 22", "July 23", "July 24", "July 25", "July 26", "July 27", "July 28", "July 29", "July 30", "July 31" ]
filtered_days = []
# The temperatures in Fahrenheit
july_temps_f = [82, 84, 87, 89, 93, 95, 91, 88, 86, 84,
    86, 89, 95, 97, 98, 101, 97, 93, 89, 87,
    86, 91, 95, 93, 89, 87, 84, 86, 89, 93, 91]

def heatwave(temp):
    for i in range (len(july_temps_f)):
        if july_temps_f[i] >= temp:
            filtered_days.append(july_days[i])

    print (filtered_days)
    filtered_days.clear()

#Challenge 2
# Chicago Streets
chicago_streets = [
    "State St", "Michigan Ave", "Wacker Dr", "Lake Shore Dr", "Western Ave",
    "Halsted St", "Milwaukee Ave", "Fullerton Ave", "Grand Ave", "Belmont Ave",
    "Irving Park Rd", "North Ave", "Lawrence Ave", "Foster Ave", "Bryn Mawr Ave",
    "Peterson Ave", "Touhy Ave", "Devon Ave", "Addison St", "Montrose Ave",
    "Damen Ave", "Elston Ave", "Lincoln Ave", "Archer Ave", "Pulaski Rd",
    "Cicero Ave", "Kedzie Ave", "California Ave", "Homan Ave", "Central Park Ave",
    "Narragansett Ave", "Austin Blvd", "Ashland Ave", "Central Ave", "Laramie Ave",
    "Kostner Ave", "Crawford Ave", "Columbus Dr", "LaSalle St", "Dearborn St",
    "Clark St", "Broadway", "Sheridan Rd", "Ridge Ave", "Clybourn Ave",
    "Ogden Ave", "Roosevelt Rd", "Cermak Rd", "Pershing Rd", "Garfield Blvd"]

# Traffic Volume (cars recorded per hour)
traffic_volume = [
    2800, 5200, 2900, 2500, 4100,
    2100, 2400, 4800, 1800, 2300,
    2200, 4300, 1900, 1500, 1400,
    2600, 2100, 1700, 2400, 1800,
    2000, 1900, 3900, 2500, 2800,
    2900, 2200, 1600, 1200, 1100,
    1300, 1700, 4500, 2100, 1800,
    1400, 1300, 2900, 2700, 2400,
    2200, 2500, 2600, 2100, 1900,
    2300, 2800, 2400, 2100, 1500]
filtered_streets = []
def street(volume):
    for i in range (len(traffic_volume)):
        if traffic_volume[i] >= volume:
            filtered_streets.append(chicago_streets[i])
    print(filtered_streets)
    filtered_streets.clear()

#Challenge 3
# Security Log Entries
security_logs = [
    "System update", "Login success", "File synced", "Unauthorized access attempt", "User logout",
    "Database backup", "Login success", "File deleted", "Unauthorized connection detected", "System update",
    "Login success", "Password changed", "Unauthorized access attempt", "File synced", "Login success",
    "Routine scan", "System update", "Unauthorized login attempt", "User logout", "File synced",
    "Login success", "Database backup", "System update", "Unauthorized port scan", "File deleted",
    "Login success", "Routine scan", "Unauthorized access attempt", "User logout", "File synced",
    "System update", "Login success", "File synced", "Unauthorized connection detected", "User logout",
    "Database backup", "Login success", "File deleted", "Unauthorized access attempt", "System update",
    "Login success", "Password changed", "Unauthorized login attempt", "File synced", "Login success",
    "Routine scan", "System update", "Unauthorized port scan", "User logout", "File synced",
    "Login success", "Database backup", "System update", "Unauthorized access attempt", "File deleted",
    "Login success", "Routine scan", "Unauthorized connection detected", "User logout", "File synced",
    "System update", "Login success", "File synced", "Unauthorized access attempt", "User logout",
    "Database backup", "Login success", "File deleted", "Unauthorized login attempt", "System update",
    "Login success", "Password changed", "Unauthorized port scan", "File synced", "Login success"
]

# Corresponding IP Addresses
log_ips = [
    "192.168.1.1", "192.168.1.12", "192.168.1.15", "10.0.0.52", "192.168.1.12",
    "192.168.1.1", "192.168.1.45", "192.168.1.15", "10.0.5.112", "192.168.1.1",
    "192.168.1.12", "192.168.1.30", "10.0.0.52", "192.168.1.15", "192.168.1.45",
    "192.168.1.1", "192.168.1.1", "172.16.254.1", "192.168.1.12", "192.168.1.15",
    "192.168.1.45", "192.168.1.1", "192.168.1.1", "10.0.5.112", "192.168.1.15",
    "192.168.1.12", "192.168.1.1", "10.0.0.52", "192.168.1.12", "192.168.1.15",
    "192.168.1.1", "192.168.1.45", "192.168.1.15", "172.16.254.1", "192.168.1.12",
    "192.168.1.1", "192.168.1.12", "192.168.1.15", "10.0.0.52", "192.168.1.1",
    "192.168.1.12", "192.168.1.30", "172.16.254.1", "192.168.1.15", "192.168.1.45",
    "192.168.1.1", "192.168.1.1", "10.0.5.112", "192.168.1.12", "192.168.1.15",
    "192.168.1.45", "192.168.1.1", "192.168.1.1", "10.0.0.52", "192.168.1.15",
    "192.168.1.12", "192.168.1.1", "172.16.254.1", "192.168.1.12", "192.168.1.15",
    "192.168.1.1", "192.168.1.45", "192.168.1.15", "10.0.0.52", "192.168.1.12",
    "192.168.1.1", "192.168.1.12", "192.168.1.15", "172.16.254.1", "192.168.1.1",
    "192.168.1.12", "192.168.1.30", "10.0.5.112", "192.168.1.15", "192.168.1.45"
]
filtered_ip = []
def security(word):
    for i in range(len(security_logs)):
        if word in security_logs[i]:
            filtered_ip.append(log_ips[i])
    print(filtered_ip)
    filtered_ip.clear()

# Applicant Names
names = [
    "Alice W.", "Bob J.", "Charlie M.", "David L.", "Eve S.", "Frank K.", "Grace H.", "Heidi V.", "Ivan Q.", "Judy P.",
    "Kevin R.", "Liam N.", "Mona B.", "Nathan T.", "Olivia Z.", "Paul X.", "Quinn W.", "Rose V.", "Steve U.", "Tara S.",
    "Ursula R.", "Victor Q.", "Wendy P.", "Xander O.", "Yara N.", "Zack M.", "Amber L.", "Blake K.", "Chloe J.", "Drew I.",
    "Elena H.", "Felix G.", "Gia F.", "Hugo E.", "Isla D.", "Jack C.", "Kira B.", "Leo A.", "Maya Z.", "Nico Y.",
    "Oscar X.", "Piper W.", "Quentin V.", "Ruby U.", "Sam T.", "Tessa S.", "Umar R.", "Vada Q.", "Wyatt P.", "Xena O.",
    "Yusuf N.", "Zoe M.", "Aria L.", "Ben K.", "Cora J.", "Dante I.", "Edith H.", "Finn G.", "Gwen F.", "Hank E.",
    "Ivy D.", "Jon C.", "Kai B.", "Lola A.", "Milo Z.", "Nora Y.", "Otis X.", "Pia W.", "Quinn V.", "Reid U.",
    "Sloane T.", "Toby S.", "Una R.", "Vince Q.", "Wren P.", "Xavier O.", "Yvonne N.", "Zane M.", "Abby L.", "Brooks K.",
    "Clara J.", "Dean I.", "Etta H.", "Ford G.", "Greta F.", "Hayes E.", "Iris D.", "Jude C.", "Kellan B.", "Lana A.",
    "Max Z.", "Nell Y.", "Owen X.", "Pearl W.", "Quincy V.", "Reed U.", "Sasha T.", "Theo S.", "Uri R.", "Vera Q.",
    "Aaron A.", "Bella B.", "Casper C.", "Daisy D.", "Eli E.", "Fiona F.", "Gideon G.", "Hazel H.", "Isaac I.", "June J.",
    "Kasper K.", "Luna L.", "Miller M.", "Nova N.", "Otto O.", "Paige P.", "Quill Q.", "River R.", "Sage S.", "Tucker T.",
    "Ulysses U.", "Violet V.", "Wells W.", "Xylon X.", "Yancy Y.", "Zelda Z.", "Adler A.", "Beckett B.", "Callie C.", "Dash D.",
    "Emery E.", "Foster F.", "Gemma G.", "Holden H.", "Indie I.", "Jasper J.", "Kinsley K.", "Lennon L.", "Maisie M.", "Nash N.",
    "Oakley O.", "Parker P.", "Quinn Q.", "Ryder R.", "Sawyer S.", "Thatcher T.", "Uriel U.", "Vesper V.", "Wilder W.", "Xara X.",
    "Yosef Y.", "Zola Z.", "Atlas A.", "Birdie B.", "Crosby C.", "Della D.", "Elias E.", "Flora F.", "Grady G.", "Hattie H.",
    "Irving I.", "Jolie J.", "Knox K.", "Lulu L.", "Murphy M.", "Nyla N.", "Odin O.", "Poppy P.", "Quest Q.", "Rocco R.",
    "Sunny S.", "Tatum T.", "Urban U.", "Veda V.", "Willa W.", "Xoey X.", "Yael Y.", "Zion Z.", "Alfie A.", "Bodie B.",
    "Cleo C.", "Duke D.", "Enzo E.", "Faye F.", "Gus G.", "Hope H.", "Ike I.", "Joy J.", "Kip K.", "Lux L.",
    "Moe M.", "Noa N.", "Obe O.", "Pip P.", "Quip Q.", "Ray R.", "Sky S.", "Ty T.", "Ugo U.", "Val V."
]

# Years of Experience
experience = [
    2, 8, 5, 12, 1, 6, 9, 3, 10, 4, 0, 7, 15, 2, 8, 4, 11, 6, 3, 9,
    5, 12, 1, 7, 10, 4, 2, 8, 5, 13, 1, 6, 9, 3, 11, 4, 0, 7, 14, 2,
    8, 4, 10, 6, 3, 9, 5, 12, 1, 7, 10, 4, 2, 8, 5, 13, 1, 6, 9, 3,
    11, 4, 0, 7, 14, 2, 8, 4, 10, 6, 3, 9, 5, 12, 1, 7, 10, 4, 2, 8,
    5, 13, 1, 6, 9, 3, 11, 4, 0, 7, 14, 2, 8, 4, 10, 6, 3, 9, 5, 12,
    1, 4, 9, 14, 2, 6, 11, 3, 8, 13, 0, 5, 10, 15, 4, 7, 12, 2, 9, 6,
    8, 3, 11, 1, 10, 5, 14, 2, 7, 13, 4, 9, 0, 12, 6, 11, 3, 8, 1, 15,
    10, 5, 2, 7, 13, 4, 9, 0, 6, 11, 3, 8, 1, 15, 10, 5, 2, 7, 13, 4,
    9, 0, 6, 11, 3, 8, 1, 15, 10, 5, 2, 7, 13, 4, 9, 0, 6, 11, 3, 8,
    1, 15, 10, 5, 2, 7, 13, 4, 9, 0, 4, 7, 2, 0, 0, 23, 4, 0, 21, 7
]

# Varied Job Titles
expertise = [
    "Python Developer", "Java Expert", "Game Coder", "AI Specialist", "App Creator", "Cyber Security", "Robot Builder", "Web Designer", "Java Developer", "Python Coder",
    "Website Tester", "Data Scientist", "System Security", "App Designer", "Java Programmer", "Network Security", "AI Programmer", "Python Expert", "Web Builder", "Game Designer",
    "AI Researcher", "Cloud Security", "Python Developer", "App Creator", "Robot Builder", "Web Designer", "App Tester", "Java Coder", "Data Analyst", "Security Manager",
    "Mobile App Creator", "JavaScript Expert", "Cyber Security", "AI Engineer", "Cloud Engineer", "Web Coder", "Software Tester", "Data Analyst", "System Admin", "App Creator",
    "Python Programmer", "Security Expert", "Robot Specialist", "Technical Support", "Java Developer", "AI Data Analyst", "Cloud Expert", "Web Designer", "App Builder", "Robot Engineer",
    "Game Developer", "Python Expert", "App Tester", "Data Scientist", "Server Manager", "AI Researcher", "App Designer", "JavaScript Developer", "Cyber Security", "AI Specialist",
    "Java Developer", "IT Support", "Software Tester", "Data Analyst", "System Expert", "Mobile Creator", "Web Developer", "Network Security", "Robot Coder", "Web Designer",
    "AI Engineer", "Data Scientist", "Python Programmer", "System Boss", "App Builder", "Web Designer", "Cyber Security", "Robot Builder", "Java Programmer", "App Tester",
    "Data Analyst", "Cloud Specialist", "AI Researcher", "Mobile App Designer", "JavaScript Coder", "Network Security", "Robot Engineer", "Python Developer", "Software Tester", "Data Scientist",
    "System Security", "App Builder", "Web Developer", "Cyber Security", "AI Programmer", "Java Developer", "IT Support", "Data Analyst", "Web Coder", "AI Specialist", "Robot Engineer", "Python Coder", "AI Researcher", "Data Scientist", "Technical Support", "JavaScript Expert", "Web Builder", "Mobile App Creator", "App Tester", "System Security",
    "Network Security", "Data Analyst", "Robot Builder", "Java Developer", "Web Designer", "AI Specialist", "App Creator", "JavaScript Coder", "IT Support", "App Tester",
    "Systems Manager", "Robot Specialist", "Cyber Security", "Java Coder", "Data Scientist", "Web Developer", "AI Researcher", "App Builder", "Python Coder", "Technical Support",
    "Software Tester", "System Security", "Robot Engineer", "Network Security", "Java Developer", "Data Scientist", "Web Designer", "AI Specialist", "App Creator", "JavaScript Coder",
    "IT Support", "App Tester", "Systems Boss", "Robot Builder", "Cyber Security", "Java Programmer", "Data Analyst", "Web Builder", "Cloud Specialist", "Mobile App Designer",
    "Python Developer", "Technical Support", "App Tester", "System Security", "Robot Engineer", "Network Security", "Java Developer", "Data Analyst", "Web Designer", "AI Specialist",
    "Mobile App Creator", "JavaScript Coder", "IT Support", "App Tester", "System Expert", "Robot Builder", "Cyber Security", "Java Programmer", "Data Analyst", "Web Builder",
    "Cloud Specialist", "Mobile App Designer", "Python Developer", "Technical Support", "App Tester", "System Security", "Robot Engineer", "Network Security", "Java Developer", "Data Scientist",
    "Web Designer", "Cloud Specialist", "Mobile App Creator", "JavaScript Coder", "IT Support", "App Tester", "System Expert", "Robot Builder", "Cyber Security", "Java Programmer",
    "Data Analyst", "Web Builder", "AI Specialist", "App Creator", "JavaScript Coder", "IT Support", "App Tester", "System Expert", "Robot Builder", "Network Security"]


dreamteam=[]
def manager(exp, role):
    for i in range (len(expertise)):
        if exp <= experience[i]:
            if role in expertise[i]:
                dreamteam.append(names[i])
    print(dreamteam)
    dreamteam.clear()

#Main
heatwave(90)



