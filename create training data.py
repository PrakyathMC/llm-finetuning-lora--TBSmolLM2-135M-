import json
from pathlib import Path

data = []

def add(category, question, answer):
    data.append({
        "id": len(data) + 1,
        "category": category,
        "question": question,
        "answer": answer
    })


# =========================
# MATHEMATICS
# =========================

math = [
    ("What is 7 multiplied by 8?", "56"),
    ("What is 9 multiplied by 6?", "54"),
    ("What is 14 multiplied by 5?", "70"),
    ("What is 18 multiplied by 4?", "72"),
    ("What is 11 multiplied by 9?", "99"),
    ("What is 16 multiplied by 7?", "112"),
    ("What is 13 multiplied by 6?", "78"),
    ("What is 24 multiplied by 3?", "72"),
    ("What is 45 divided by 5?", "9"),
    ("What is 72 divided by 8?", "9"),
    ("What is 81 divided by 9?", "9"),
    ("What is 96 divided by 12?", "8"),
    ("What is 144 divided by 12?", "12"),
    ("What is 63 divided by 7?", "9"),
    ("What is 100 divided by 4?", "25"),

    ("What is 17 plus 28?", "45"),
    ("What is 56 plus 37?", "93"),
    ("What is 84 minus 29?", "55"),
    ("What is 100 minus 47?", "53"),
    ("What is 135 plus 65?", "200"),
    ("What is 250 minus 125?", "125"),
    ("What is 43 plus 39?", "82"),
    ("What is 90 minus 36?", "54"),

    ("What is 10% of 300?", "30"),
    ("What is 20% of 150?", "30"),
    ("What is 50% of 84?", "42"),
    ("What is 25% of 80?", "20"),
    ("What is 10% of 450?", "45"),
    ("What is 75% of 40?", "30"),
    ("What is 5% of 200?", "10"),
    ("What is 40% of 250?", "100"),

    ("What is the square of 9?", "81"),
    ("What is the square of 11?", "121"),
    ("What is the square of 12?", "144"),
    ("What is the square of 15?", "225"),
    ("What is the square of 20?", "400"),

    ("What is the square root of 81?", "9"),
    ("What is the square root of 100?", "10"),
    ("What is the square root of 169?", "13"),
    ("What is the square root of 196?", "14"),
    ("What is the square root of 225?", "15"),

    ("What is 2 to the power of 6?", "64"),
    ("What is 3 to the power of 4?", "81"),
    ("What is 5 to the power of 3?", "125"),
    ("What is 10 to the power of 3?", "1000"),

    ("Solve for x: x + 7 = 15.", "x = 8"),
    ("Solve for x: x - 9 = 4.", "x = 13"),
    ("Solve for x: 3x = 21.", "x = 7"),
    ("Solve for x: 4x = 32.", "x = 8"),
    ("Solve for x: 2x + 5 = 15.", "x = 5"),
    ("Solve for x: 3x + 6 = 18.", "x = 4"),
    ("Solve for x: 5x - 10 = 20.", "x = 6"),
    ("Solve for x: 4x - 8 = 16.", "x = 6"),

    ("What is the average of 5, 10, and 15?", "10"),
    ("What is the average of 12, 18, and 24?", "18"),
    ("What is the average of 20, 30, and 40?", "30"),
    ("What is the average of 6, 12, and 18?", "12"),

    ("What is the perimeter of a rectangle with length 6 cm and width 4 cm?", "20 centimeters"),
    ("What is the area of a rectangle with length 9 cm and width 3 cm?", "27 square centimeters"),
    ("What is the area of a square with side length 6 cm?", "36 square centimeters"),
    ("What is the perimeter of a square with side length 9 cm?", "36 centimeters"),

    ("What is 1/2 expressed as a percentage?", "50%"),
    ("What is 1/4 expressed as a percentage?", "25%"),
    ("What is 1/5 expressed as a percentage?", "20%"),
    ("What is 3/5 expressed as a percentage?", "60%"),
    ("What is 2/5 expressed as a percentage?", "40%"),
    ("What is 4/5 expressed as a percentage?", "80%"),

    ("What is the next number in the sequence 3, 6, 9, 12, 15?", "18"),
    ("What is the next number in the sequence 5, 10, 15, 20, 25?", "30"),
    ("What is the next number in the sequence 1, 3, 5, 7, 9?", "11"),
    ("What is the next number in the sequence 10, 20, 30, 40, 50?", "60"),

    ("How many degrees are in a right angle?", "90 degrees"),
    ("How many sides does a hexagon have?", "6"),
    ("How many sides does an octagon have?", "8"),
    ("How many sides does a pentagon have?", "5"),
]

for question, answer in math:
    add("Mathematics", question, answer)


# =========================
# CHEMISTRY
# =========================

chemistry = [
    ("What is the chemical symbol for hydrogen?", "H"),
    ("What is the chemical symbol for oxygen?", "O"),
    ("What is the chemical symbol for nitrogen?", "N"),
    ("What is the chemical symbol for carbon?", "C"),
    ("What is the chemical symbol for iron?", "Fe"),
    ("What is the chemical symbol for copper?", "Cu"),
    ("What is the chemical symbol for silver?", "Ag"),
    ("What is the chemical symbol for potassium?", "K"),
    ("What is the chemical symbol for calcium?", "Ca"),
    ("What is the chemical symbol for chlorine?", "Cl"),
    ("What is the chemical symbol for magnesium?", "Mg"),
    ("What is the chemical symbol for zinc?", "Zn"),
    ("What is the chemical symbol for helium?", "He"),
    ("What is the chemical symbol for neon?", "Ne"),

    ("What is the chemical formula for methane?", "CH4"),
    ("What is the chemical formula for ammonia?", "NH3"),
    ("What is the chemical formula for oxygen gas?", "O2"),
    ("What is the chemical formula for hydrogen gas?", "H2"),
    ("What is the chemical formula for nitrogen gas?", "N2"),
    ("What is the chemical formula for sulfuric acid?", "H2SO4"),
    ("What is the chemical formula for hydrochloric acid?", "HCl"),
    ("What is the chemical formula for sodium hydroxide?", "NaOH"),
    ("What is the chemical formula for calcium carbonate?", "CaCO3"),
    ("What is the chemical formula for glucose?", "C6H12O6"),

    ("What is the common name for H2O?", "Water"),
    ("What is the common name for CO2?", "Carbon dioxide"),
    ("What is the common name for NaHCO3?", "Baking soda"),
    ("What is the common name for CH4?", "Methane"),
    ("What is the common name for NH3?", "Ammonia"),

    ("What particle in an atom has a positive electrical charge?", "Proton"),
    ("What particle in an atom has no electrical charge?", "Neutron"),
    ("What particle in an atom has a negative electrical charge?", "Electron"),
    ("What is the center of an atom called?", "Nucleus"),

    ("What is the atomic number of hydrogen?", "1"),
    ("What is the atomic number of oxygen?", "8"),
    ("What is the atomic number of nitrogen?", "7"),
    ("What is the atomic number of sodium?", "11"),
    ("What is the atomic number of iron?", "26"),
    ("What is the atomic number of gold?", "79"),

    ("What type of bond involves transfer of electrons?", "Ionic bond"),
    ("What type of bond involves sharing of electrons?", "Covalent bond"),

    ("What is a substance with a pH below 7 called?", "Acid"),
    ("What is a substance with a pH above 7 called?", "Base"),
    ("What is a substance with a pH of 7 generally called?", "Neutral"),

    ("What color does blue litmus paper turn in an acid?", "Red"),
    ("What color does red litmus paper turn in a base?", "Blue"),

    ("What gas is released when many acids react with metals?", "Hydrogen"),
    ("What gas is required for combustion?", "Oxygen"),
    ("What gas is commonly produced when carbon-containing fuels burn completely?", "Carbon dioxide"),

    ("What is the process of a liquid changing into a gas called?", "Vaporization"),
    ("What is the process of a gas changing into a liquid called?", "Condensation"),
    ("What is the process of a solid changing into a liquid called?", "Melting"),
    ("What is the process of a liquid changing into a solid called?", "Freezing"),
    ("What is the process of a solid changing directly into a gas called?", "Sublimation"),
    ("What is the process of a gas changing directly into a solid called?", "Deposition"),

    ("What is a homogeneous mixture called?", "Solution"),
    ("What is the substance that dissolves a solute called?", "Solvent"),
    ("What is the substance dissolved in a solution called?", "Solute"),

    ("What is the smallest unit of an element that retains its chemical properties?", "Atom"),
    ("What is an element?", "A pure substance made of one type of atom"),
    ("What is a compound?", "A substance made of two or more different elements chemically bonded"),

    ("What is the periodic table used to organize?", "Chemical elements"),
    ("Which element has the symbol Na?", "Sodium"),
    ("Which element has the symbol K?", "Potassium"),
    ("Which element has the symbol Fe?", "Iron"),
    ("Which element has the symbol Cu?", "Copper"),
    ("Which element has the symbol Ag?", "Silver"),
    ("Which element has the symbol Au?", "Gold"),
    ("Which element has the symbol Cl?", "Chlorine"),
    ("Which element has the symbol Ca?", "Calcium"),

    ("What is the main gas in Earth's atmosphere?", "Nitrogen"),
    ("What is the approximate pH of pure water at room temperature?", "7"),
]

for question, answer in chemistry:
    add("Chemistry", question, answer)


# =========================
# GENERAL SCIENCE
# =========================

science = [
    ("What organ pumps blood around the human body?", "Heart"),
    ("What organ is primarily responsible for breathing?", "Lungs"),
    ("What organ controls most activities of the human body?", "Brain"),
    ("What organ filters waste from the blood and produces urine?", "Kidneys"),
    ("What organ produces bile and helps process nutrients?", "Liver"),

    ("What is the basic unit of the nervous system?", "Neuron"),
    ("What is the basic unit of the human body?", "Cell"),
    ("What molecule carries genetic information?", "DNA"),
    ("What structure contains most of a cell's DNA?", "Nucleus"),

    ("What process do plants use to make food using light?", "Photosynthesis"),
    ("What pigment gives plants their green color?", "Chlorophyll"),
    ("What gas do plants take in during photosynthesis?", "Carbon dioxide"),
    ("What gas do plants release during photosynthesis?", "Oxygen"),
    ("What part of a plant transports water upward?", "Xylem"),
    ("What part of a plant transports sugars?", "Phloem"),
    ("What part of a plant usually contains the reproductive structures?", "Flower"),
    ("What part of a plant anchors it in the soil?", "Roots"),

    ("What force attracts objects toward Earth?", "Gravity"),
    ("What force opposes motion between surfaces?", "Friction"),
    ("What is the SI unit of force?", "Newton"),
    ("What is the SI unit of energy?", "Joule"),
    ("What is the SI unit of power?", "Watt"),
    ("What is the SI unit of electric current?", "Ampere"),
    ("What is the SI unit of temperature?", "Kelvin"),

    ("What is the speed of sound in air approximately?", "343 meters per second"),
    ("What is the speed of light in a vacuum approximately?", "3 × 10^8 meters per second"),

    ("What instrument measures temperature?", "Thermometer"),
    ("What instrument measures atmospheric pressure?", "Barometer"),
    ("What instrument measures earthquakes?", "Seismometer"),
    ("What instrument is used to observe distant stars?", "Telescope"),

    ("What is Earth's natural satellite?", "Moon"),
    ("What planet is closest to the Sun?", "Mercury"),
    ("What planet is known for its prominent rings?", "Saturn"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What planet is known as the Red Planet?", "Mars"),
    ("What planet is farthest from the Sun among the eight planets?", "Neptune"),
    ("What star is at the center of our solar system?", "Sun"),
    ("How many planets are in the solar system?", "8"),
    ("What galaxy contains our solar system?", "Milky Way"),

    ("What causes day and night on Earth?", "Earth's rotation"),
    ("What causes the seasons on Earth?", "Earth's axial tilt as it orbits the Sun"),
    ("What is the layer of gases surrounding Earth called?", "Atmosphere"),
    ("What gas makes up most of Earth's atmosphere?", "Nitrogen"),
    ("What gas do humans need for aerobic respiration?", "Oxygen"),

    ("What is water's freezing point in Celsius at standard pressure?", "0 degrees Celsius"),
    ("What is water's boiling point in Celsius at standard pressure?", "100 degrees Celsius"),
    ("At what temperature does water freeze in Fahrenheit?", "32 degrees Fahrenheit"),
    ("At what temperature does water boil in Fahrenheit at standard pressure?", "212 degrees Fahrenheit"),

    ("What is the change from liquid water to water vapor called?", "Evaporation"),
    ("What is the water cycle process where water vapor forms clouds?", "Condensation"),
    ("What is precipitation?", "Water falling from the atmosphere to Earth's surface"),

    ("How many bones are in a typical adult human skeleton?", "206"),
    ("How many chambers does the human heart have?", "4"),
    ("How many lungs does a typical human have?", "2"),
    ("How many teeth does a typical adult human have?", "32"),

    ("What blood cells help fight infections?", "White blood cells"),
    ("What blood cells carry oxygen?", "Red blood cells"),
    ("What protein in red blood cells carries oxygen?", "Hemoglobin"),
    ("What vitamin is produced in skin in response to sunlight?", "Vitamin D"),

    ("What is the process by which organisms produce offspring?", "Reproduction"),
    ("What is an animal that eats only plants called?", "Herbivore"),
    ("What is an animal that eats only other animals called?", "Carnivore"),
    ("What is an animal that eats both plants and animals called?", "Omnivore"),

    ("What is the study of living organisms called?", "Biology"),
    ("What is the study of matter and its interactions called?", "Chemistry"),
    ("What is the study of forces, motion, and energy called?", "Physics"),
    ("What is the study of Earth's rocks and structure called?", "Geology"),
    ("What is the study of weather and the atmosphere called?", "Meteorology"),

    ("What is a habitat?", "The natural environment where an organism lives"),
    ("What is an ecosystem?", "A community of organisms and their physical environment"),
    ("What is biodiversity?", "The variety of living organisms in an area"),
    ("What is a food chain?", "A sequence showing how energy and nutrients pass between organisms"),

    ("What is a renewable energy source?", "An energy source that is naturally replenished"),
    ("What is solar energy?", "Energy from the Sun"),
    ("What is wind energy?", "Energy obtained from moving air"),
    ("What is an electric circuit?", "A closed path through which electric current can flow"),
]

for question, answer in science:
    add("General Science", question, answer)


# =========================
# SAVE DATASET
# =========================

output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "train.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("=" * 50)
print("TRAINING DATA CREATED")
print("=" * 50)
print(f"Total examples: {len(data)}")
print(f"Mathematics: {len(math)}")
print(f"Chemistry: {len(chemistry)}")
print(f"General Science: {len(science)}")
print(f"Saved to: {output_file}")