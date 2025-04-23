# https://spacy.io/usage/training#training-data


# for local spaCy training 
import spacy
from spacy.training.example import Example
from spacy.util import minibatch
import random
TRAIN_DATA = [
    ( #Character Offset Based Annotation 
        "Drexel Apartments, Downtown Hyde Park 5011 South Drexel Boulevard, Chicago, IL 60615, United States Wed, Apr 30, 2025 3:00 PM — 9:00 PM Wed, May 14, 2025 8:00 AM — 11:00 AM 2 weeks",
        {  # annotations contain an 'entities' which holds a list of entites
         # (star_char_index, end_char_index, entity label)
            "entities": [
                (0, 44, "PROPERTY"), 
                (45, 109, "LOCATION"),
                (110, 129, "CHECKIN_DATE"),
                (130, 150, "CHECKIN_TIME"),
                (151, 170, "CHECKOUT_DATE"),
                (171, 193, "CHECKOUT_TIME"),
                (194, 202, "DURATION")
            ]
        }
    ),
    (
        "Metal Jazz Fusion Fri, Aug 1 7pm East of Eden Club, San Francisco From $19",
        {
            "entities": [
                (0, 18, "EVENT"),
                (19, 35, "DATETIME"),
                (36, 71, "VENUE"),
                (72, 81, "PRICE")
            ]
        }
    ),
    (
        "Bloomington to Chicago Tuesday, April 15 4:14pm - 5:13pm American Airlines",
        {
            "entities": [
                (0, 23, "ROUTE"),
                (24, 43, "DATE"),
                (44, 66, "TIME_RANGE"),
                (67, 85, "AIRLINE")
            ]
        }
    ),
    (
        "Chicago to Bloomington Tuesday, April 22 2:50pm - 3:41pm American Airlines",
        {
            "entities": [
                (0, 23, "ROUTE"),
                (24, 43, "DATE"),
                (44, 66, "TIME_RANGE"),
                (67, 85, "AIRLINE")
            ]
        }
    ),
    (
        "Courtyard by Marriott Chicago Magnificent Mile Room, 1 King Bed with Sofa bed Check-in: Wed, Apr 2 Check-out: Fri, Apr 4 2-night stay",
        {
            "entities": [
                (0, 53, "PROPERTY"),
                (54, 91, "ROOM_TYPE"),
                (103, 115, "CHECKIN_DATE"),
                (127, 139, "CHECKOUT_DATE"),
                (140, 153, "DURATION")
            ]
        }
    ),
    (
        "Atlanta to Tokyo Thu, Apr 17 9:45 PM Atlanta - ATL Turkish Airlines TK 32 Tokyo - NRT Jeju Air",
        {
            "entities": [
                (0, 17, "ROUTE"),
                (18, 32, "DEPARTURE_DATE"),
                (33, 41, "DEPARTURE_TIME"),
                (42, 57, "DEPARTURE_AIRPORT"),
                (58, 74, "AIRLINE"),
                (75, 80, "FLIGHT_NUMBER"),
                (81, 94, "ARRIVAL_AIRPORT"),
                (95, 103, "ARRIVAL_AIRLINE")
            ]
        }
    ),
    (
        "Tokyo to Atlanta Mon, Apr 21 6:30 PM Tokyo - NRT WestJet Atlanta - ATL",
        {
            "entities": [
                (0, 18, "ROUTE"),
                (19, 34, "DEPARTURE_DATE"),
                (35, 43, "DEPARTURE_TIME"),
                (44, 58, "DEPARTURE_AIRPORT"),
                (59, 66, "AIRLINE"),
                (67, 81, "ARRIVAL_AIRPORT")
            ]
        }
    ),
    (
        "Orbiiit X TIMBO IDO ONLINE CONTEST WORLDWIDE March 31 - 11pm — April 1 - 10:30pm CDT Online",
        {
            "entities": [
                (0, 51, "EVENT"),
                (52, 88, "TIME_RANGE"),
                (89, 95, "LOCATION")
            ]
        }
    ),
    (
        "Whiskey Friends - The Morgan Wallen Experience Friday, April 4 8:30 - 11pm CDT The Cadillac 108 West State Street Paxton, IL 60957",
        {
            "entities": [
                (0, 51, "EVENT"),
                (52, 68, "DATE"),
                (69, 87, "TIME_RANGE"),
                (88, 101, "VENUE"),
                (102, 146, "LOCATION")
            ]
        }
    ),
    (
        "\"Glow in the Dark\" Egg Hunt at the vineyard Friday, April 4 7 - 10pm CDT Mackinaw Valley Vineyard 33633 Illinois 9 Mackinaw, IL 61755",
        {
            "entities": [
                (0, 49, "EVENT"),
                (50, 66, "DATE"),
                (67, 82, "TIME_RANGE"),
                (83, 108, "VENUE"),
                (109, 149, "LOCATION")
            ]
        }
    ),
    (
        "Wreath Making with Happy Home by Holly Saturday, April 5 12 - 2pm CDT Keg Grove Brewing Company 712 East Empire Street #Suite 2 Bloomington, IL 61701",
        {
            "entities": [
                (0, 44, "EVENT"),
                (45, 63, "DATE"),
                (64, 78, "TIME_RANGE"),
                (79, 106, "VENUE"),
                (107, 162, "LOCATION")
            ]
        }
    ),
    (
        "Pick-up location: Bloomington, IL, United States Drop-off location: Downtown Chicago, Chicago, Illinois Pick-up date: Apr 15 Drop-off date: Apr 16 Pick-up time: 10:30 am Drop-off time: 10:30 am",
        {
            "entities": [
                (20, 54, "PICKUP_LOCATION"),
                (77, 117, "DROPOFF_LOCATION"),
                (134, 140, "PICKUP_DATE"),
                (158, 164, "DROPOFF_DATE"),
                (181, 190, "PICKUP_TIME"),
                (207, 216, "DROPOFF_TIME")
            ]
        }
    ),
    (
        "Royal Princess Vancouver to Seattle May 13, 2025 to May 17, 2025 4 Nights Depart Vancouver, Canada at 03:00 PM on May 13 Arrive Seattle, Washington at 07:00 AM on May 17",
        {
            "entities": [
                (0, 15, "SHIP_NAME"),
                (16, 35, "ROUTE"),
                (36, 59, "DATE_RANGE"),
                (60, 69, "DURATION"),
                (77, 94, "DEPARTURE_PORT"),
                (98, 106, "DEPARTURE_TIME"),
                (110, 118, "DEPARTURE_DATE"),
                (127, 148, "ARRIVAL_PORT"),
                (152, 160, "ARRIVAL_TIME"),
                (164, 172, "ARRIVAL_DATE")
            ]
        }
    ),
    (
        "New Patient Appointment with Lily A. Young, APRN on Wednesday April 2, 2025. Arrive by 8:05 AM. Starts at 8:20 AM. Location: OSF Medical Group - Pediatrics - Bloomington, 302 ST JOSEPH DR Bloomington IL 61701-3506.",
        {
            "entities": [
                (30, 51, "DOCTOR"),
                (56, 80, "DATE"),
                (92, 101, "ARRIVAL_TIME"),
                (115, 124, "START_TIME"),
                (136, 181, "CLINIC"),
                (183, 232, "ADDRESS")
            ]
        }
    ),
    (
        "Academic Advisor Meeting on April 4, 2025 from 1:40PM to 2:00PM via ZOOM MEETING online.",
        {
            "entities": [
                (0, 27, "EVENT_TYPE"),
                (31, 45, "DATE"),
                (51, 68, "TIME_RANGE"),
                (73, 94, "MEETING_TYPE")
            ]
        }
    ),
    (
        "Appointment for Oil Change at 108 S Towanda Ave Normal, IL 61761 on 04/03/2025 at 5:00 PM. Customer will drop-off the vehicle. Contact: (309) 888-9333.",
        {
            "entities": [
                (18, 29, "SERVICE"),
                (33, 74, "LOCATION"),
                (78, 88, "DATE"),
                (92, 100, "TIME"),
                (112, 143, "DROP_OFF_TYPE"),
                (153, 167, "PHONE")
            ]
        }
    ),
    (
        "Rent a Fullsize Toyota Camry or similar from Apr 15, 12:00 PM to Apr 16, 12:00 PM at Peoria Airport, Illinois. $81/day, $81 total.",
        {
            "entities": [
                (7, 15, "CAR_TYPE"),
                (16, 42, "CAR_MODEL"),
                (48, 88, "TIME_RANGE"),
                (92, 117, "LOCATION"),
                (119, 127, "DAILY_PRICE"),
                (129, 140, "TOTAL_PRICE")
            ]
        }
    )
]


# creat a blank model
nlp = spacy.blank("en")
# Add NER pipline
if "ner" not in nlp.pipe_names:
    ner= nlp.add_pipe("ner") # add new NER componet
else:
    ner = nlp.get_pipe("ner") # if already exists,just get it 
# add label from Train_data, tell the NEr compoment about the labels need to recognize
for _, annotations in TRAIN_DATA:
    for start, end, label in annotations["entities"]:
        ner.add_label(label)
 # check for misaligned entity spans       
from spacy.training import offsets_to_biluo_tags
for text, ann in TRAIN_DATA:
    try:
        offsets_to_biluo_tags(nlp.make_doc(text), ann["entities"])
    except Exception as e:
        print("Misaligned entities in:", text)
        print("  Error:", e)
        print("—" * 80)

# start training 
optimizer = nlp.begin_training()

for itn in range(30):  # train for 30 iterations
    random.shuffle(TRAIN_DATA) # shuffle the data for each iteration
    losses ={}          # dictionary to store loss values
    batches = minibatch(TRAIN_DATA, size =2)# Split int omini_batches
    for batch in batches:
        for text, annotations in batch:
            doc = nlp.make_doc(text)  #create a spacy Doc object
            example = Example.from_dict(doc, annotations) # convert to training format
            nlp.update([example], drop=0.2, sgd=optimizer, losses =losses)
    print(f"Iteration {itn+1} complete. Loss: {losses.get('ner', 0.0):.2f}")

import os        
# save model to local directory
output_dir = "custom_ner_model"
os.makedirs(output_dir, exist_ok=True) # create directory if it doesn't exist
nlp.to_disk(output_dir) 
print(f"Model saved to :{output_dir}")


