#Pranjal Adhikari pa8729

import random
import json

meteorite_compositions = ["stony", "iron", "stony-iron"]

random_sites = { "sites": 
    [ 
        {"site_id": 1, "latitude": random.uniform(16.0, 18.0), "longitude": random.uniform(82.0, 84.0), "meteorite composition": random.choice(meteorite_compositions) },
        {"site_id": 2, "latitude": random.uniform(16.0, 18.0), "longitude": random.uniform(82.0, 84.0), "meteorite composition": random.choice(meteorite_compositions) },
        {"site_id": 3, "latitude": random.uniform(16.0, 18.0), "longitude": random.uniform(82.0, 84.0), "meteorite composition": random.choice(meteorite_compositions) },
        {"site_id": 4, "latitude": random.uniform(16.0, 18.0), "longitude": random.uniform(82.0, 84.0), "meteorite composition": random.choice(meteorite_compositions) },
        {"site_id": 5, "latitude": random.uniform(16.0, 18.0), "longitude": random.uniform(82.0, 84.0), "meteorite composition": random.choice(meteorite_compositions) },
    ]
}

with open('random_sites.json', 'w') as out:
    json.dump(random_sites, out, indent = 2)