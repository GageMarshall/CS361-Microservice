# Written by: Gage Marshall
# Last modified: 5/19/2025

import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
    
state_fun_facts = {
  "Alabama": "In 2016, Alabama saw a surge in Pokémon Go players, with local parks becoming unexpected gathering spots for trainers.",
  "Alaska": "Alaska's vast wilderness makes it a challenging yet adventurous place for Pokémon Go players seeking rare finds.",
  "Arizona": "Tucson, Arizona, became a hotspot for Pokémon Go enthusiasts, thanks to its numerous parks and public spaces.",
  "Arkansas": "Arkansas hosted several community Pokémon Go events in 2017, drawing players from neighboring states.",
  "California": "In 2025, Los Angeles hosted the Pokémon GO Tour: Unova at the Rose Bowl Stadium, attracting thousands of trainers.",
  "Colorado": "Denver's Civic Center Park was transformed into a Pokémon Go arena during the 2016 summer craze.",
  "Connecticut": "Connecticut libraries embraced the Pokémon Go trend by setting up lures to attract both Pokémon and readers.",
  "Delaware": "Delaware's coastal towns became unexpected Pokémon Go hotspots, with rare water-type Pokémon sightings.",
  "Florida": "Florida's beaches, like those in Miami and Tampa, became prime locations for catching water-type Pokémon in Pokémon Go.",
  "Georgia": "Atlanta's Piedmont Park was a central hub for Pokémon Go players during the game's peak popularity.",
  "Hawaii": "Hawaii's unique geography made it a treasure trove for region-specific Pokémon in Pokémon Go.",
  "Idaho": "Idaho's scenic trails offered Pokémon Go players both exercise and the chance to catch elusive Pokémon.",
  "Illinois": "Chicago hosted the first-ever Pokémon Go Fest in 2017, marking a significant event in the game's history.",
  "Indiana": "Indianapolis saw a record number of PokéStops per capita during the initial Pokémon Go surge.",
  "Iowa": "Des Moines organized community walks centered around Pokémon Go, promoting both health and gaming.",
  "Kansas": "Kansas City's parks department collaborated with Niantic to enhance Pokémon Go experiences in public spaces.",
  "Kentucky": "Louisville's waterfront became a gathering spot for Pokémon Go raids and community events.",
  "Louisiana": "New Orleans is set to host the Pokémon North America International Championships in June 2025, highlighting its vibrant gaming community.",
  "Maine": "Portland, Maine, integrated Pokémon Go into its city tours, blending history with gaming.",
  "Maryland": "Baltimore's Inner Harbor was a focal point for Pokémon Go players seeking rare catches.",
  "Massachusetts": "Boston's Freedom Trail offered both historical insights and a plethora of PokéStops for trainers.",
  "Michigan": "Detroit revitalized its downtown by encouraging Pokémon Go events, drawing in crowds and boosting local businesses.",
  "Minnesota": "Minneapolis' Chain of Lakes area became a serene yet active spot for Pokémon Go enthusiasts.",
  "Mississippi": "Jackson's parks saw increased foot traffic due to Pokémon Go community days and events.",
  "Missouri": "St. Louis integrated Pokémon Go into its annual fairs, combining traditional festivities with modern gaming.",
  "Montana": "Montana's vast landscapes provided a unique challenge for Pokémon Go players seeking diverse habitats.",
  "Nebraska": "Omaha's Henry Doorly Zoo became a dual attraction for both animal lovers and Pokémon trainers.",
  "Nevada": "Las Vegas casinos reported increased Wi-Fi usage attributed to Pokémon Go players exploring the Strip.",
  "New Hampshire": "Portsmouth's historic sites doubled as PokéStops, blending colonial history with augmented reality.",
  "New Jersey": "Jersey City will host Pokémon GO Fest 2025 at Liberty State Park, drawing trainers nationwide.",
  "New Mexico": "Albuquerque's Balloon Fiesta incorporated Pokémon Go challenges, adding a digital twist to the event.",
  "New York": "Central Park in NYC became an iconic Pokémon Go location, often featured in media during the game's peak.",
  "North Carolina": "Charlotte's uptown area organized Pokémon Go bar crawls, merging nightlife with gaming.",
  "North Dakota": "Fargo's downtown embraced Pokémon Go by setting up themed events and competitions.",
  "Ohio": "Cleveland's Rock & Roll Hall of Fame became a popular PokéStop, attracting both music and Pokémon fans.",
  "Oklahoma": "Oklahoma City's Bricktown district saw businesses offering discounts to Pokémon Go players.",
  "Oregon": "Portland's tech-savvy community organized Pokémon Go hackathons to enhance gameplay experiences.",
  "Pennsylvania": "Philadelphia's historic landmarks served as prime locations for PokéStops and gyms.",
  "Rhode Island": "Providence hosted themed Pokémon Go nights, turning the city into a trainer's playground.",
  "South Carolina": "Charleston's waterfront parks became serene spots for catching water-type Pokémon.",
  "South Dakota": "Rapid City's public art installations doubled as PokéStops, merging culture with gaming.",
  "Tennessee": "Nashville's music venues embraced Pokémon Go, hosting themed nights and events.",
  "Texas": "At the 2025 South Texas Comic Con in McAllen, a heartwarming proposal unfolded between two cosplayers. Jonathan Cu, dressed as Ash Ketchum, proposed to his girlfriend Crystal Hernandez, who was dressed as Pikachu. The couple, both avid Pokémon fans and special cosplay guests at the convention, shared the moment during a cosplay contest. Cu cleverly incorporated a Poké Ball prop containing an engagement ring into his surprise proposal. Hernandez joyfully accepted, and Cu delivered the iconic phrase, “Pikachu, I choose you!”",
  "Utah": "Salt Lake City's Liberty Park was highlighted as a top Pokémon Go hotspot in 2025.",
  "Vermont": "Burlington's community centers hosted Pokémon Go workshops for players of all ages.",
  "Virginia": "Richmond integrated Pokémon Go into its historical tours, offering a unique blend of past and present.",
  "Washington": "Seattle's tech hubs organized Pokémon Go developer meetups, fostering innovation in gameplay.",
  "West Virginia": "Charleston's riverfront parks became popular spots for Pokémon Go community gatherings.",
  "Wisconsin": "Milwaukee's lakefront festivals incorporated Pokémon Go challenges, enhancing attendee engagement.",
  "Wyoming": "Cheyenne's Frontier Days festival added Pokémon Go events, blending tradition with modern gaming."
}

while True:
    # recieve JSON from client
    request_json = socket.recv_json()
    print("Received:", request_json)

    # verify JSON file for "state"
    if "state" not in request_json:
        reply = {"error": "Missing 'state' field in JSON"}
    else:
        state_name = request_json["state"]
        # searches for the fact using the state and stores it in reply if found
        if state_name in state_fun_facts:
            fact_text = state_fun_facts[state_name]
            reply = {"state": state_name, "fact": fact_text}
        else:
            reply = {"error": "State fact not found in database"}
    socket.send_json(reply)
    print("Replied with:", reply)
