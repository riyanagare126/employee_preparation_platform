"""
AI Employee Preparation Platform - Master Aptitude Question Bank
Curated pool of 100+ placement-level assessment questions categorized across:
- Quantitative Aptitude (25 questions)
- Logical Reasoning (25 questions)
- Verbal Ability (25 questions)
- Data Interpretation (15 questions)
- Basic Technical Aptitude (30 questions: Java, Python, Web/Frontend, SQL, DSA, System)
"""

MASTER_APTITUDE_BANK = [
    # =========================================================================
    # 1. QUANTITATIVE APTITUDE (25 Questions)
    # =========================================================================
    {
        "id": 101,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A train running at 54 km/hr crosses a bridge of length 240 m in 26 seconds. What is the length of the train?",
        "options": ["120 m", "150 m", "180 m", "200 m"],
        "correctIndex": 1,
        "explanation": "Speed = 54 * (5/18) = 15 m/s. Total distance = Speed * Time = 15 * 26 = 390 m. Train length = 390 - 240 = 150 m.",
        "tags": ["speed", "distance", "trains"],
        "roles": ["all"]
    },
    {
        "id": 102,
        "category": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A can finish a work in 12 days and B in 18 days. If they work together on it for 4 days, what fraction of the work remains unfinished?",
        "options": ["1/3", "4/9", "5/9", "7/18"],
        "correctIndex": 1,
        "explanation": "1 day work of (A + B) = 1/12 + 1/18 = 5/36. In 4 days work done = 4 * (5/36) = 5/9. Remaining work = 1 - 5/9 = 4/9.",
        "tags": ["time-and-work"],
        "roles": ["all"]
    },
    {
        "id": 103,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A sum of money invested at compound interest doubles itself in 4 years. In how many years will it amount to 8 times itself at the same rate?",
        "options": ["8 years", "12 years", "16 years", "24 years"],
        "correctIndex": 1,
        "explanation": "P becomes 2P in 4 years. 8P = (2^3)P, so time = 3 * 4 = 12 years.",
        "tags": ["interest", "compound-interest"],
        "roles": ["all"]
    },
    {
        "id": 104,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "The average weight of 8 persons increases by 2.5 kg when a new person replaces one person weighing 65 kg. What is the weight of the new person?",
        "options": ["75 kg", "80 kg", "85 kg", "90 kg"],
        "correctIndex": 2,
        "explanation": "Total increase in weight = 8 * 2.5 = 20 kg. Weight of new person = 65 + 20 = 85 kg.",
        "tags": ["averages"],
        "roles": ["all"]
    },
    {
        "id": 105,
        "category": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A shopkeeper marks an article 25% above cost price and allows a discount of 10% on the marked price. What is his actual profit percentage?",
        "options": ["10%", "12.5%", "15%", "17.5%"],
        "correctIndex": 1,
        "explanation": "Let CP = 100. Marked Price = 125. Selling Price = 125 * 0.90 = 112.5. Profit = 112.5 - 100 = 12.5%.",
        "tags": ["profit-and-loss"],
        "roles": ["all"]
    },
    {
        "id": 106,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "Two pipes A and B can fill a tank in 20 and 30 minutes respectively. If both pipes are opened together, when should pipe B be turned off so the tank is filled in 15 minutes?",
        "options": ["6 min", "7.5 min", "8 min", "10 min"],
        "correctIndex": 1,
        "explanation": "Pipe A works for full 15 min: 15/20 = 3/4. Remaining 1/4 filled by B. Time for B = (1/4) * 30 = 7.5 min.",
        "tags": ["pipes-and-cisterns"],
        "roles": ["all"]
    },
    {
        "id": 107,
        "category": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "If 15% of A is equal to 20% of B, what is the ratio A : B?",
        "options": ["3 : 4", "4 : 3", "5 : 4", "2 : 3"],
        "correctIndex": 1,
        "explanation": "0.15 * A = 0.20 * B => A/B = 20/15 = 4/3.",
        "tags": ["percentages", "ratio"],
        "roles": ["all"]
    },
    {
        "id": 108,
        "category": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "In how many different ways can the letters of the word 'CORPORATION' be arranged so that the vowels always come together?",
        "options": ["50,400", "28,800", "14,400", "7,200"],
        "correctIndex": 0,
        "explanation": "Vowels in CORPORATION: O, O, A, I, O (5 vowels, O repeats 3 times). Consonants: C, R, P, R, T, N (6 consonants, R repeats 2 times). Group vowels as 1 unit: 7 units arranged in 7! / 2! ways = 2520. Vowels arranged among themselves in 5! / 3! = 20 ways. Total = 2520 * 20 = 50,400.",
        "tags": ["permutations", "combinations"],
        "roles": ["all"]
    },
    {
        "id": 109,
        "category": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A bag contains 6 red, 4 blue, and 5 green balls. If one ball is drawn at random, what is the probability that it is neither red nor blue?",
        "options": ["1/3", "2/5", "4/15", "1/5"],
        "correctIndex": 0,
        "explanation": "Total balls = 6 + 4 + 5 = 15. Ball is neither red nor blue => it must be green (5 balls). P(green) = 5/15 = 1/3.",
        "tags": ["probability"],
        "roles": ["all"]
    },
    {
        "id": 110,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A boat can travel with a speed of 13 km/hr in still water. If the speed of the stream is 4 km/hr, find the time taken by the boat to go 68 km downstream.",
        "options": ["3 hours", "4 hours", "5 hours", "6 hours"],
        "correctIndex": 1,
        "explanation": "Downstream speed = 13 + 4 = 17 km/hr. Time taken = Distance / Speed = 68 / 17 = 4 hours.",
        "tags": ["boats-and-streams"],
        "roles": ["all"]
    },
    {
        "id": 111,
        "category": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "The ratio of present ages of two brothers is 4 : 5. Six years ago, the ratio of their ages was 3 : 4. Find the sum of their present ages.",
        "options": ["45 years", "54 years", "60 years", "72 years"],
        "correctIndex": 1,
        "explanation": "Let ages be 4x and 5x. (4x - 6)/(5x - 6) = 3/4 => 16x - 24 = 15x - 18 => x = 6. Sum = 4x + 5x = 9x = 9 * 6 = 54 years.",
        "tags": ["ages", "ratio"],
        "roles": ["all"]
    },
    {
        "id": 112,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A sum of $12,500 amounts to $15,500 in 4 years at the rate of simple interest. What is the annual rate of interest?",
        "options": ["5%", "6%", "7.5%", "8%"],
        "correctIndex": 1,
        "explanation": "Simple Interest = 15500 - 12500 = 3000. Rate = (SI * 100) / (P * T) = (3000 * 100) / (12500 * 4) = 300000 / 50000 = 6%.",
        "tags": ["simple-interest"],
        "roles": ["all"]
    },
    {
        "id": 113,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "A mixture contains milk and water in the ratio 7 : 5. If 15 liters of water is added to it, the ratio of milk to water becomes 7 : 8. Find the quantity of milk in the mixture.",
        "options": ["28 liters", "35 liters", "42 liters", "49 liters"],
        "correctIndex": 1,
        "explanation": "Milk quantity remains unchanged (7 units). Water increases from 5 units to 8 units (3 units = 15 L => 1 unit = 5 L). Milk = 7 units = 7 * 5 = 35 liters.",
        "tags": ["alligation", "mixture"],
        "roles": ["all"]
    },
    {
        "id": 114,
        "category": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "What is the smallest number that must be added to 1056 so that the sum is completely divisible by 23?",
        "options": ["2", "3", "18", "21"],
        "correctIndex": 0,
        "explanation": "1056 / 23 = 45 with remainder 21. Required number to add = 23 - 21 = 2.",
        "tags": ["number-system"],
        "roles": ["all"]
    },
    {
        "id": 115,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "The HCF of two numbers is 11 and their LCM is 7700. If one of the numbers is 275, find the other number.",
        "options": ["285", "308", "312", "330"],
        "correctIndex": 1,
        "explanation": "Product of two numbers = HCF * LCM. Other number = (11 * 7700) / 275 = 84700 / 275 = 308.",
        "tags": ["hcf-lcm"],
        "roles": ["all"]
    },
    {
        "id": 116,
        "category": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "A man walks at 5 km/hr from his house to the office and arrives 6 minutes late. If he walks at 6 km/hr, he arrives 2 minutes early. What is the distance between his house and the office?",
        "options": ["3 km", "4 km", "5 km", "6 km"],
        "correctIndex": 1,
        "explanation": "Difference in arrival times = 6 - (-2) = 8 minutes = 8/60 hours. Distance = (S1 * S2 / (S2 - S1)) * Delta_t = (5 * 6 / 1) * (8/60) = 30 * (2/15) = 4 km.",
        "tags": ["speed", "distance"],
        "roles": ["all"]
    },
    {
        "id": 117,
        "category": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A trader sells two bullocks for $8,400 each, neither losing nor gaining in total. If he sold one bullock at a 20% gain, the other is sold at a loss of:",
        "options": ["14 2/7%", "16 2/3%", "18 2/9%", "20%"],
        "correctIndex": 0,
        "explanation": "Total SP = 16800 => Total CP = 16800. For first: SP = 8400, Gain = 20% => CP1 = 8400 / 1.2 = 7000. So CP2 = 16800 - 7000 = 9800. Loss on second = 9800 - 8400 = 1400. Loss% = (1400/9800) * 100 = 100/7% = 14 2/7%.",
        "tags": ["profit-and-loss"],
        "roles": ["all"]
    },
    {
        "id": 118,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "Find the compound interest on $10,000 in 2 years at 4% per annum, the interest being compounded half-yearly.",
        "options": ["$824.32", "$816.00", "$800.00", "$832.16"],
        "correctIndex": 0,
        "explanation": "Rate per half-year = 2%, n = 4 periods. Amount = 10000 * (1.02)^4 = 10000 * 1.082432 = $10,824.32. CI = 10824.32 - 10000 = $824.32.",
        "tags": ["compound-interest"],
        "roles": ["all"]
    },
    {
        "id": 119,
        "category": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "If 12 men or 18 women can reap a field in 14 days, then in how many days can 8 men and 16 women reap the same field?",
        "options": ["7 days", "9 days", "10 days", "12 days"],
        "correctIndex": 1,
        "explanation": "12 Men = 18 Women => 1 Man = 1.5 Women. 8 Men + 16 Women = 8 * 1.5 + 16 = 28 Women. Days = (18 * 14) / 28 = 9 days.",
        "tags": ["time-and-work"],
        "roles": ["all"]
    },
    {
        "id": 120,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "The perimeter of a rectangle is 82 meters and its area is 400 square meters. Find the breadth of the rectangle.",
        "options": ["14 meters", "16 meters", "20 meters", "25 meters"],
        "correctIndex": 1,
        "explanation": "2(l + b) = 82 => l + b = 41. l * b = 400. Factors of 400 adding to 41 are 25 and 16. So breadth is 16 meters.",
        "tags": ["mensuration"],
        "roles": ["all"]
    },
    {
        "id": 121,
        "category": "Quantitative Aptitude",
        "difficulty": "Hard",
        "question": "Two numbers are in the ratio 3 : 5. If 9 is subtracted from each, the new numbers are in the ratio 12 : 23. What is the smaller number?",
        "options": ["27", "33", "45", "55"],
        "correctIndex": 1,
        "explanation": "(3x - 9)/(5x - 9) = 12/23 => 69x - 207 = 60x - 108 => 9x = 99 => x = 11. Smaller number = 3x = 3 * 11 = 33.",
        "tags": ["ratio-proportion"],
        "roles": ["all"]
    },
    {
        "id": 122,
        "category": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A clock is started at noon. By 10 minutes past 5, the hour hand has turned through how many degrees?",
        "options": ["145°", "150°", "155°", "160°"],
        "correctIndex": 2,
        "explanation": "Total minutes from 12:00 to 5:10 = 5 * 60 + 10 = 310 minutes. The hour hand rotates at 0.5° per minute. Angle = 310 * 0.5° = 155°.",
        "tags": ["clocks"],
        "roles": ["all"]
    },
    {
        "id": 123,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "What day of the week was 15th August 1947?",
        "options": ["Wednesday", "Thursday", "Friday", "Saturday"],
        "correctIndex": 2,
        "explanation": "Standard calendar odd day calculation: 1600 yrs (0) + 300 yrs (1) + 46 yrs (11 leap + 35 ord = 57 odd days = 1) + 15 Aug (Jan 3 + Feb 0 + Mar 3 + Apr 2 + May 3 + Jun 2 + Jul 3 + Aug 15 = 31 = 3) => Total odd days = 1 + 1 + 3 = 5 (Friday).",
        "tags": ["calendar"],
        "roles": ["all"]
    },
    {
        "id": 124,
        "category": "Quantitative Aptitude",
        "difficulty": "Medium",
        "question": "In a 100 m race, A beats B by 10 m and C by 13 m. In a race of 180 m, by what distance will B beat C?",
        "options": ["5.4 m", "6 m", "6.5 m", "7.2 m"],
        "correctIndex": 1,
        "explanation": "When A covers 100 m, B covers 90 m and C covers 87 m. When B covers 90 m, C covers 87 m => B beats C by 3 m. In 180 m race, B beats C by (3/90) * 180 = 6 meters.",
        "tags": ["races"],
        "roles": ["all"]
    },
    {
        "id": 125,
        "category": "Quantitative Aptitude",
        "difficulty": "Easy",
        "question": "A sum of $700 is divided among A, B, C such that A receives half of what B receives and B receives half of what C receives. What is B's share?",
        "options": ["$100", "$200", "$300", "$400"],
        "correctIndex": 1,
        "explanation": "Let C = 4x, B = 2x, A = x. Total = 7x = 700 => x = 100. B's share = 2x = $200.",
        "tags": ["ratio-proportion"],
        "roles": ["all"]
    },

    # =========================================================================
    # 2. LOGICAL REASONING (25 Questions)
    # =========================================================================
    {
        "id": 201,
        "category": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Look at this series: 7, 10, 8, 11, 9, 12, ... What number should come next?",
        "options": ["7", "10", "12", "13"],
        "correctIndex": 1,
        "explanation": "Alternating pattern: +3, -2, +3, -2. 12 - 2 = 10.",
        "tags": ["number-series"],
        "roles": ["all"]
    },
    {
        "id": 202,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Pointing to a photograph of a boy, Suresh said, 'He is the son of the only son of my mother.' How is Suresh related to that boy?",
        "options": ["Brother", "Uncle", "Father", "Cousin"],
        "correctIndex": 2,
        "explanation": "The only son of Suresh's mother is Suresh himself. So the boy is Suresh's son, making Suresh the Father.",
        "tags": ["blood-relations"],
        "roles": ["all"]
    },
    {
        "id": 203,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "In a certain code, 'COMPUTER' is written as 'RFUVQNPC'. How is 'MEDICINE' written in that code?",
        "options": ["MFEDJJOE", "EOJDEJFM", "EOJDJEFM", "MFEJDJOE"],
        "correctIndex": 2,
        "explanation": "Reverse the word and shift intermediate letters by +1: MEDICINE -> E(N+1=O)(I+1=J)(C+1=D)(I+1=J)(D+1=E)(E+1=F)M -> EOJDJEFM.",
        "tags": ["coding-decoding"],
        "roles": ["all"]
    },
    {
        "id": 204,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Statements: All flowers are trees. No tree is a fruit.\nConclusions:\nI. No flower is a fruit.\nII. Some trees are flowers.",
        "options": ["Only I follows", "Only II follows", "Either I or II follows", "Both I and II follow"],
        "correctIndex": 3,
        "explanation": "Since all flowers are inside trees and no tree is fruit, no flower is fruit (I follows). Since flowers are inside trees, some trees are flowers (II follows).",
        "tags": ["syllogisms"],
        "roles": ["all"]
    },
    {
        "id": 205,
        "category": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Five friends P, Q, R, S, and T are sitting in a row facing North. R is sitting adjacent to Q and P. S is at the extreme right end. T is to the left of P. Who is sitting in the middle?",
        "options": ["P", "Q", "R", "T"],
        "correctIndex": 2,
        "explanation": "Arrangement from left to right: T, P, R, Q, S. The person in the middle is R.",
        "tags": ["seating-arrangement"],
        "roles": ["all"]
    },
    {
        "id": 206,
        "category": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "A man walks 5 km East, turns right and walks 4 km, then turns left and walks 5 km. In which direction is he now with respect to the starting point?",
        "options": ["North-East", "South-East", "North-West", "South-West"],
        "correctIndex": 1,
        "explanation": "He is 10 km East and 4 km South of the starting point, placing him in the South-East direction.",
        "tags": ["direction-sense"],
        "roles": ["all"]
    },
    {
        "id": 207,
        "category": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Find the odd one out from the given list: Zinc, Iron, Aluminum, Mercury, Gold.",
        "options": ["Zinc", "Iron", "Mercury", "Gold"],
        "correctIndex": 2,
        "explanation": "Mercury is the only metal that is in liquid state at room temperature.",
        "tags": ["classification"],
        "roles": ["all"]
    },
    {
        "id": 208,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Complete the letter series: SCD, TEF, UGH, ____, WKL",
        "options": ["CMN", "UJI", "VIJ", "IJT"],
        "correctIndex": 2,
        "explanation": "First letter increases: S, T, U, V, W. Second and third letters are consecutive pairs: CD, EF, GH, IJ, KL. So next term is VIJ.",
        "tags": ["letter-series"],
        "roles": ["all"]
    },
    {
        "id": 209,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "If 'P + Q' means P is the daughter of Q, 'P - Q' means P is the husband of Q, 'P * Q' means P is the brother of Q. Which of the following shows that T is the daughter-in-law of M?",
        "options": ["T + M * B", "T - K + M", "T + K - M", "M - K + T"],
        "correctIndex": 1,
        "explanation": "T - K + M means T is husband of K (inverted relation) or K is son of M (K + M) and married to T, making T daughter-in-law.",
        "tags": ["blood-relations"],
        "roles": ["all"]
    },
    {
        "id": 210,
        "category": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Look at this series: 2, 6, 12, 20, 30, 42, ... What number should come next?",
        "options": ["52", "54", "56", "60"],
        "correctIndex": 2,
        "explanation": "Differences are +4, +6, +8, +10, +12, so next is +14. 42 + 14 = 56. (Also n * (n+1): 1*2, 2*3, 3*4, 4*5, 5*6, 6*7, 7*8 = 56).",
        "tags": ["number-series"],
        "roles": ["all"]
    },
    {
        "id": 211,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "In a row of students, Rahul is 11th from the left and 23rd from the right. How many total students are there in the row?",
        "options": ["32", "33", "34", "35"],
        "correctIndex": 1,
        "explanation": "Total students = (Left position + Right position) - 1 = (11 + 23) - 1 = 33.",
        "tags": ["ranking"],
        "roles": ["all"]
    },
    {
        "id": 212,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Statements: Some actors are singers. All singers are dancers.\nConclusions:\nI. Some actors are dancers.\nII. No singer is an actor.",
        "options": ["Only I follows", "Only II follows", "Either I or II follows", "Neither I nor II follows"],
        "correctIndex": 0,
        "explanation": "Since some actors are singers and all singers are dancers, the actors who are singers are definitely dancers (I follows). Since some actors are singers, 'No singer is an actor' is false.",
        "tags": ["syllogisms"],
        "roles": ["all"]
    },
    {
        "id": 213,
        "category": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Light is to Darkness as Knowledge is to:",
        "options": ["Ignorance", "Intelligence", "Power", "Education"],
        "correctIndex": 0,
        "explanation": "Light is the antonym of Darkness, and Knowledge is the antonym of Ignorance.",
        "tags": ["analogy"],
        "roles": ["all"]
    },
    {
        "id": 214,
        "category": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Six people A, B, C, D, E, and F are sitting in a circle facing the center. A is second to the left of C. B is to the immediate right of A. D is between C and F. Who is sitting opposite to B?",
        "options": ["C", "D", "E", "F"],
        "correctIndex": 1,
        "explanation": "Arrangement in clockwise order: A, B, E, C, D, F. The person opposite to B is D.",
        "tags": ["seating-arrangement"],
        "roles": ["all"]
    },
    {
        "id": 215,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "If in a certain code, 'ROAD' is written as 'URDG', how is 'SWAN' written in that code?",
        "options": ["VXDO", "VZDQ", "UXDQ", "VYDQ"],
        "correctIndex": 1,
        "explanation": "Each letter is shifted forward by +3: S+3=V, W+3=Z, A+3=D, N+3=Q => VZDQ.",
        "tags": ["coding-decoding"],
        "roles": ["all"]
    },
    {
        "id": 216,
        "category": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Which word does NOT belong with the others?",
        "options": ["Inch", "Ounce", "Centimeter", "Yard"],
        "correctIndex": 1,
        "explanation": "Inch, Centimeter, and Yard are units of length, whereas Ounce is a unit of mass/weight.",
        "tags": ["classification"],
        "roles": ["all"]
    },
    {
        "id": 217,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Introducing a woman, a man said, 'Her mother is the only daughter of my mother-in-law.' How is the man related to the woman?",
        "options": ["Father", "Uncle", "Brother", "Husband"],
        "correctIndex": 0,
        "explanation": "The only daughter of the man's mother-in-law is the man's wife. The woman's mother is the man's wife, so the man is her Father.",
        "tags": ["blood-relations"],
        "roles": ["all"]
    },
    {
        "id": 218,
        "category": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Statement: Should higher education in all fields be made completely free for all students?\nArguments:\nI. Yes, it will improve the literacy rate and economic standard of the nation.\nII. No, the government does not have enough financial resources to sustain free higher education without compromising quality.",
        "options": ["Only argument I is strong", "Only argument II is strong", "Either I or II is strong", "Both arguments I and II are strong"],
        "correctIndex": 3,
        "explanation": "Both arguments present valid socioeconomic concerns regarding human capital advancement vs fiscal viability.",
        "tags": ["statement-argument"],
        "roles": ["all"]
    },
    {
        "id": 219,
        "category": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Look at this series: 36, 34, 30, 28, 24, ... What number should come next?",
        "options": ["20", "22", "23", "26"],
        "correctIndex": 1,
        "explanation": "Alternating pattern of subtraction: -2, -4, -2, -4. 24 - 2 = 22.",
        "tags": ["number-series"],
        "roles": ["all"]
    },
    {
        "id": 220,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "A clock seen through a mirror shows 3:15. What is the actual time?",
        "options": ["8:45", "9:15", "8:15", "9:45"],
        "correctIndex": 0,
        "explanation": "Actual time = 11:60 - Mirror time = 11:60 - 3:15 = 8:45.",
        "tags": ["clocks-mirror"],
        "roles": ["all"]
    },
    {
        "id": 221,
        "category": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "If SOUTH-EAST becomes NORTH, NORTH-EAST becomes WEST and so on. What will WEST become?",
        "options": ["NORTH-EAST", "SOUTH-EAST", "NORTH-WEST", "SOUTH-WEST"],
        "correctIndex": 1,
        "explanation": "The entire direction compass rotates 135° anti-clockwise. West rotated 135° anti-clockwise becomes South-East.",
        "tags": ["direction-sense"],
        "roles": ["all"]
    },
    {
        "id": 222,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "Statements: All books are papers. Some papers are journals.\nConclusions:\nI. Some books are journals.\nII. Some journals are papers.",
        "options": ["Only I follows", "Only II follows", "Both I and II follow", "Neither follows"],
        "correctIndex": 1,
        "explanation": "Since some papers are journals, some journals are papers (II follows). There is no direct connection establishing books as journals (I does not necessarily follow).",
        "tags": ["syllogisms"],
        "roles": ["all"]
    },
    {
        "id": 223,
        "category": "Logical Reasoning",
        "difficulty": "Easy",
        "question": "Find the missing number in the sequence: 4, 9, 25, 49, 121, ____",
        "options": ["144", "169", "196", "225"],
        "correctIndex": 1,
        "explanation": "The sequence is the squares of consecutive prime numbers: 2^2, 3^2, 5^2, 7^2, 11^2, 13^2 = 169.",
        "tags": ["number-series", "primes"],
        "roles": ["all"]
    },
    {
        "id": 224,
        "category": "Logical Reasoning",
        "difficulty": "Medium",
        "question": "In a code language, 123 means 'hot filtered coffee', 356 means 'very hot day', and 589 means 'day and night'. Which numerical digit stands for 'very'?",
        "options": ["3", "5", "6", "8"],
        "correctIndex": 2,
        "explanation": "'hot' is common in 123 and 356 => hot = 3. 'day' is common in 356 and 589 => day = 5. In 356 ('very hot day'), the remaining digit is 6 for 'very'.",
        "tags": ["coding-decoding"],
        "roles": ["all"]
    },
    {
        "id": 225,
        "category": "Logical Reasoning",
        "difficulty": "Hard",
        "question": "Statements: The principal announced a ban on mobile phones inside the campus.\nAssumptions:\nI. Students will abide by the principal's regulation.\nII. Mobile phones cause distraction in academic activities.",
        "options": ["Only assumption I is implicit", "Only assumption II is implicit", "Both I and II are implicit", "Neither is implicit"],
        "correctIndex": 2,
        "explanation": "Any institutional authority assumes adherence (I is implicit) and acts upon the premise that the banned object causes disturbance (II is implicit).",
        "tags": ["critical-reasoning"],
        "roles": ["all"]
    },

    # =========================================================================
    # 3. VERBAL ABILITY (25 Questions)
    # =========================================================================
    {
        "id": 301,
        "category": "Verbal Ability",
        "difficulty": "Easy",
        "question": "Choose the word most nearly OPPOSITE in meaning to: 'METICULOUS'.",
        "options": ["Careless", "Painstaking", "Accurate", "Diligent"],
        "correctIndex": 0,
        "explanation": "'Meticulous' means showing great attention to detail. The direct antonym is 'Careless'.",
        "tags": ["antonyms"],
        "roles": ["all"]
    },
    {
        "id": 302,
        "category": "Verbal Ability",
        "difficulty": "Easy",
        "question": "Choose the word most nearly SIMILAR in meaning to: 'CANDID'.",
        "options": ["Secretive", "Frank", "Deceitful", "Cautious"],
        "correctIndex": 1,
        "explanation": "'Candid' means truthful, straightforward, and frank.",
        "tags": ["synonyms"],
        "roles": ["all"]
    },
    {
        "id": 303,
        "category": "Verbal Ability",
        "difficulty": "Medium",
        "question": "Identify the grammatically correct sentence:",
        "options": [
            "Neither of the candidates have submitted their profile.",
            "Neither of the candidates has submitted his profile.",
            "Neither of the candidates have submitted his profile.",
            "Neither of the candidate has submitted their profile."
        ],
        "correctIndex": 1,
        "explanation": "'Neither' is a singular indefinite pronoun requiring a singular verb ('has') and singular possessive pronoun ('his').",
        "tags": ["sentence-correction"],
        "roles": ["all"]
    },
    {
        "id": 304,
        "category": "Verbal Ability",
        "difficulty": "Easy",
        "question": "Fill in the blank: She was surprised ______ his sudden decision to resign.",
        "options": ["with", "at", "by", "for"],
        "correctIndex": 1,
        "explanation": "'Surprised at' is the standard idiomatic preposition used when reacting to an event, action, or decision.",
        "tags": ["prepositions"],
        "roles": ["all"]
    },
    {
        "id": 305,
        "category": "Verbal Ability",
        "difficulty": "Medium",
        "question": "What is the meaning of the idiom: 'To bite the bullet'?",
        "options": [
            "To act recklessly without planning",
            "To face an inevitable grim situation with courage",
            "To speak harshly to someone",
            "To suffer an unexpected defeat"
        ],
        "correctIndex": 1,
        "explanation": "'To bite the bullet' means to bravely endure a painful or unavoidable situation.",
        "tags": ["idioms"],
        "roles": ["all"]
    },
    {
        "id": 306,
        "category": "Verbal Ability",
        "difficulty": "Medium",
        "question": "Find the correctly spelled word:",
        "options": ["Accomodation", "Accommodation", "Acommodation", "Accomadation"],
        "correctIndex": 1,
        "explanation": "The correct spelling is 'Accommodation' with double 'c' and double 'm'.",
        "tags": ["spelling"],
        "roles": ["all"]
    },
    {
        "id": 307,
        "category": "Verbal Ability",
        "difficulty": "Hard",
        "question": "Choose the one-word substitute for: 'A person who is indifferent to pleasure or pain.'",
        "options": ["Stoic", "Ascetic", "Epicurean", "Cynic"],
        "correctIndex": 0,
        "explanation": "A 'Stoic' is an individual who endures hardship without showing feelings or complaining.",
        "tags": ["one-word-substitution"],
        "roles": ["all"]
    },
    {
        "id": 308,
        "category": "Verbal Ability",
        "difficulty": "Easy",
        "question": "Choose the word most nearly OPPOSITE in meaning to: 'AUGMENT'.",
        "options": ["Increase", "Diminish", "Enhance", "Amplify"],
        "correctIndex": 1,
        "explanation": "'Augment' means to make something greater by adding to it. The opposite is 'Diminish'.",
        "tags": ["antonyms"],
        "roles": ["all"]
    },
    {
        "id": 309,
        "category": "Verbal Ability",
        "difficulty": "Medium",
        "question": "Fill in the blank: The project was delayed ______ unforeseen technical complications.",
        "options": ["due to", "because", "owing", "in spite of"],
        "correctIndex": 0,
        "explanation": "'Due to' functions as a predicate adjective prepositional phrase modifying the noun delay/predicative clause.",
        "tags": ["fill-in-blanks"],
        "roles": ["all"]
    },
    {
        "id": 310,
        "category": "Verbal Ability",
        "difficulty": "Hard",
        "question": "Identify the part containing an error: 'If I was you (A) / I would not accept (B) / that offer without negotiation (C) / No error (D)'",
        "options": ["A", "B", "C", "D"],
        "correctIndex": 0,
        "explanation": "In hypothetical/subjunctive conditional clauses, 'were' is used instead of 'was': 'If I were you'.",
        "tags": ["error-spotting"],
        "roles": ["all"]
    },
    {
        "id": 311,
        "category": "Verbal Ability",
        "difficulty": "Easy",
        "question": "Choose the synonym for: 'EPHEMERAL'.",
        "options": ["Transient", "Permanent", "Eternal", "Enduring"],
        "correctIndex": 0,
        "explanation": "'Ephemeral' means lasting for a very short time; 'Transient' is the exact synonym.",
        "tags": ["synonyms"],
        "roles": ["all"]
    },
    {
        "id": 312,
        "category": "Verbal Ability",
        "difficulty": "Medium",
        "question": "Choose the correct passive voice for: 'The architect has designed a groundbreaking blueprint.'",
        "options": [
            "A groundbreaking blueprint is designed by the architect.",
            "A groundbreaking blueprint had been designed by the architect.",
            "A groundbreaking blueprint has been designed by the architect.",
            "A groundbreaking blueprint was designed by the architect."
        ],
        "correctIndex": 2,
        "explanation": "Present perfect active 'has designed' converts to present perfect passive 'has been designed'.",
        "tags": ["active-passive"],
        "roles": ["all"]
    },
    {
        "id": 313,
        "category": "Verbal Ability",
        "difficulty": "Medium",
        "question": "What is the meaning of the idiom: 'Burn the midnight oil'?",
        "options": [
            "To waste valuable electricity",
            "To work or study late into the night",
            "To cause accidental damage",
            "To complete a task early in the morning"
        ],
        "correctIndex": 1,
        "explanation": "'To burn the midnight oil' means to work or study late into the night.",
        "tags": ["idioms"],
        "roles": ["all"]
    },
    {
        "id": 314,
        "category": "Verbal Ability",
        "difficulty": "Easy",
        "question": "Choose the antonym for: 'LUCID'.",
        "options": ["Clear", "Obscure", "Transparent", "Articulate"],
        "correctIndex": 1,
        "explanation": "'Lucid' means expressed clearly; 'Obscure' means unclear or difficult to understand.",
        "tags": ["antonyms"],
        "roles": ["all"]
    },
    {
        "id": 315,
        "category": "Verbal Ability",
        "difficulty": "Hard",
        "question": "Select the correct one-word substitute for: 'The practice of putting a painless end to the lives of persons suffering from incurable diseases.'",
        "options": ["Euthanasia", "Genocide", "Homicide", "Asphyxiation"],
        "correctIndex": 0,
        "explanation": "'Euthanasia' is mercy killing or assisted painless death for patients with irreversible pain/conditions.",
        "tags": ["one-word-substitution"],
        "roles": ["all"]
    },
    {
        "id": 316,
        "category": "Verbal Ability",
        "difficulty": "Easy",
        "question": "Fill in the blank: He has lived in this city ______ 2018.",
        "options": ["for", "since", "from", "during"],
        "correctIndex": 1,
        "explanation": "'Since' is used to specify a particular starting point in time with present perfect continuous/perfect tenses.",
        "tags": ["prepositions"],
        "roles": ["all"]
    },
    {
        "id": 317,
        "category": "Verbal Ability",
        "difficulty": "Medium",
        "question": "Find the correctly spelled word:",
        "options": ["Bureaucracy", "Beurocracy", "Bureaucrasy", "Burocracy"],
        "correctIndex": 0,
        "explanation": "The correct spelling is 'Bureaucracy' (B-U-R-E-A-U-C-R-A-C-Y).",
        "tags": ["spelling"],
        "roles": ["all"]
    },
    {
        "id": 318,
        "category": "Verbal Ability",
        "difficulty": "Hard",
        "question": "Identify the error: 'The manager along with his team members (A) / are attending (B) / the annual global conference (C) / No error (D)'",
        "options": ["A", "B", "C", "D"],
        "correctIndex": 1,
        "explanation": "When a subject is joined with phrases like 'along with', the verb agrees with the first subject ('The manager', singular). It should be 'is attending'.",
        "tags": ["error-spotting"],
        "roles": ["all"]
    },
    {
        "id": 319,
        "category": "Verbal Ability",
        "difficulty": "Medium",
        "question": "Choose the synonym for: 'PRAGMATIC'.",
        "options": ["Idealistic", "Practical", "Theoretical", "Speculative"],
        "correctIndex": 1,
        "explanation": "'Pragmatic' means dealing with things sensibly and realistically based on practical considerations.",
        "tags": ["synonyms"],
        "roles": ["all"]
    },
    {
        "id": 320,
        "category": "Verbal Ability",
        "difficulty": "Easy",
        "question": "Choose the antonym for: 'HARMONY'.",
        "options": ["Symphony", "Discord", "Accord", "Consensus"],
        "correctIndex": 1,
        "explanation": "'Harmony' means agreement or peaceful concord; 'Discord' means disagreement or conflict.",
        "tags": ["antonyms"],
        "roles": ["all"]
    },
    {
        "id": 321,
        "category": "Verbal Ability",
        "difficulty": "Medium",
        "question": "What is the meaning of the idiom: 'Spill the beans'?",
        "options": [
            "To drop kitchen groceries",
            "To reveal a secret unintentionally or prematurely",
            "To create a big mess",
            "To apologize humbly"
        ],
        "correctIndex": 1,
        "explanation": "'Spill the beans' means to disclose confidential information or a secret.",
        "tags": ["idioms"],
        "roles": ["all"]
    },
    {
        "id": 322,
        "category": "Verbal Ability",
        "difficulty": "Hard",
        "question": "Rearrange the sentence parts into a coherent sequence:\nP: throughout the software lifecycle\nQ: continuous integration ensures\nR: automated code testing and rapid deployment\nS: high system reliability",
        "options": ["Q-R-S-P", "Q-P-R-S", "S-P-Q-R", "R-S-Q-P"],
        "correctIndex": 0,
        "explanation": "Correct order: Q (continuous integration ensures) -> R (automated code testing and rapid deployment) -> S (high system reliability) -> P (throughout the software lifecycle).",
        "tags": ["para-jumbles"],
        "roles": ["all"]
    },
    {
        "id": 323,
        "category": "Verbal Ability",
        "difficulty": "Easy",
        "question": "Fill in the blank: Despite the heavy traffic, we arrived ______ time for the interview.",
        "options": ["at", "on", "in", "by"],
        "correctIndex": 1,
        "explanation": "'On time' means punctual/at the scheduled time.",
        "tags": ["idioms-prepositions"],
        "roles": ["all"]
    },
    {
        "id": 324,
        "category": "Verbal Ability",
        "difficulty": "Medium",
        "question": "Choose the one-word substitute for: 'A speech delivered without any prior preparation.'",
        "options": ["Extempore", "Monologue", "Eulogy", "Soliloquy"],
        "correctIndex": 0,
        "explanation": "An impromptu speech given on the spot is called 'Extempore'.",
        "tags": ["one-word-substitution"],
        "roles": ["all"]
    },
    {
        "id": 325,
        "category": "Verbal Ability",
        "difficulty": "Easy",
        "question": "Choose the word most nearly SIMILAR to: 'ZEALOUS'.",
        "options": ["Apathetic", "Enthusiastic", "Reluctant", "Indifferent"],
        "correctIndex": 1,
        "explanation": "'Zealous' means having or showing passionate fervor; 'Enthusiastic' is the synonym.",
        "tags": ["synonyms"],
        "roles": ["all"]
    },

    # =========================================================================
    # 4. DATA INTERPRETATION (15 Questions)
    # =========================================================================
    {
        "id": 401,
        "category": "Data Interpretation",
        "difficulty": "Medium",
        "question": "A tech company's revenue grew from $400,000 in 2021 to $520,000 in 2022, and $650,000 in 2023. What was the percentage growth in revenue from 2022 to 2023?",
        "options": ["20%", "25%", "30%", "32.5%"],
        "correctIndex": 1,
        "explanation": "Growth = (650,000 - 520,000) / 520,000 = 130,000 / 520,000 = 1/4 = 25%.",
        "tags": ["percentage-growth"],
        "roles": ["all"]
    },
    {
        "id": 402,
        "category": "Data Interpretation",
        "difficulty": "Easy",
        "question": "In an engineering cohort of 120 students: 65 study Python, 55 study Java, and 20 study both. How many students study neither Python nor Java?",
        "options": ["15", "20", "25", "30"],
        "correctIndex": 1,
        "explanation": "Total studying at least one = (65 + 55) - 20 = 100. Neither = 120 - 100 = 20.",
        "tags": ["venn-diagram"],
        "roles": ["all"]
    },
    {
        "id": 403,
        "category": "Data Interpretation",
        "difficulty": "Medium",
        "question": "In a pie chart representing a startup's $1,200,000 annual budget, Engineering takes up 108° of the circle. What is the dollar allocation for Engineering?",
        "options": ["$300,000", "$360,000", "$400,000", "$450,000"],
        "correctIndex": 1,
        "explanation": "Engineering share = 108° / 360° = 3/10 = 30%. 30% of $1,200,000 = $360,000.",
        "tags": ["pie-chart"],
        "roles": ["all"]
    },
    {
        "id": 404,
        "category": "Data Interpretation",
        "difficulty": "Medium",
        "question": "A table shows monthly website visits (in thousands): Jan: 80, Feb: 95, Mar: 110, Apr: 115. What is the average monthly traffic for Q1 (Jan-Mar)?",
        "options": ["90k", "95k", "100k", "105k"],
        "correctIndex": 1,
        "explanation": "Q1 total = 80 + 95 + 110 = 285. Average = 285 / 3 = 95k.",
        "tags": ["tables-averages"],
        "roles": ["all"]
    },
    {
        "id": 405,
        "category": "Data Interpretation",
        "difficulty": "Hard",
        "question": "Product sales across 4 quarters: Q1: 450 units @ $20, Q2: 500 units @ $22, Q3: 600 units @ $25, Q4: 550 units @ $24. In which quarter was the total revenue highest?",
        "options": ["Q1", "Q2", "Q3", "Q4"],
        "correctIndex": 2,
        "explanation": "Q1 = 450 * 20 = $9,000; Q2 = 500 * 22 = $11,000; Q3 = 600 * 25 = $15,000; Q4 = 550 * 24 = $13,200. Highest is Q3.",
        "tags": ["revenue-analysis"],
        "roles": ["all"]
    },
    {
        "id": 406,
        "category": "Data Interpretation",
        "difficulty": "Easy",
        "question": "In a department of 200 employees, 60% are Developers and 40% are Testers. If 25% of Developers and 10% of Testers work remotely, what is the total number of remote workers?",
        "options": ["32", "38", "42", "48"],
        "correctIndex": 1,
        "explanation": "Developers = 120 => Remote = 0.25 * 120 = 30. Testers = 80 => Remote = 0.10 * 80 = 8. Total remote = 30 + 8 = 38.",
        "tags": ["percentages-breakdown"],
        "roles": ["all"]
    },
    {
        "id": 407,
        "category": "Data Interpretation",
        "difficulty": "Medium",
        "question": "A server logs latency: 50% of requests take 20ms, 30% take 40ms, and 20% take 70ms. What is the weighted average request latency?",
        "options": ["32 ms", "36 ms", "40 ms", "44 ms"],
        "correctIndex": 1,
        "explanation": "Weighted avg = (0.50 * 20) + (0.30 * 40) + (0.20 * 70) = 10 + 12 + 14 = 36 ms.",
        "tags": ["weighted-average"],
        "roles": ["all"]
    },
    {
        "id": 408,
        "category": "Data Interpretation",
        "difficulty": "Medium",
        "question": "A bar chart shows defect count per sprint: Sprint 1: 18, Sprint 2: 12, Sprint 3: 8, Sprint 4: 6. What is the percentage reduction in defects from Sprint 1 to Sprint 4?",
        "options": ["50%", "60%", "66.67%", "75%"],
        "correctIndex": 2,
        "explanation": "Reduction = (18 - 6) / 18 = 12 / 18 = 2/3 = 66.67%.",
        "tags": ["bar-chart"],
        "roles": ["all"]
    },
    {
        "id": 409,
        "category": "Data Interpretation",
        "difficulty": "Hard",
        "question": "Company A and B produce laptops. In 2023, A produced 50,000 with a 4% defect rate, while B produced 30,000 with a 2% defect rate. What is the overall combined defect percentage?",
        "options": ["2.75%", "3.00%", "3.25%", "3.50%"],
        "correctIndex": 2,
        "explanation": "Defects in A = 50000 * 0.04 = 2000. Defects in B = 30000 * 0.02 = 600. Total defects = 2600. Total units = 80000. Overall% = (2600 / 80000) * 100 = 3.25%.",
        "tags": ["weighted-ratio"],
        "roles": ["all"]
    },
    {
        "id": 410,
        "category": "Data Interpretation",
        "difficulty": "Easy",
        "question": "A line graph shows cloud infrastructure cost ($k): Q1: 40, Q2: 48, Q3: 60, Q4: 72. What was the ratio of Q1 cost to Q4 cost?",
        "options": ["5 : 9", "4 : 7", "2 : 3", "5 : 8"],
        "correctIndex": 0,
        "explanation": "Ratio Q1 : Q4 = 40 : 72 = 5 : 9.",
        "tags": ["line-graph"],
        "roles": ["all"]
    },
    {
        "id": 411,
        "category": "Data Interpretation",
        "difficulty": "Medium",
        "question": "Out of 500 software patches tested, 85% were successful on the first pass, 10% required one fix, and the rest were rejected. How many patches were completely rejected?",
        "options": ["15", "20", "25", "30"],
        "correctIndex": 2,
        "explanation": "Rejected% = 100% - (85% + 10%) = 5%. Rejected count = 0.05 * 500 = 25.",
        "tags": ["pie-percentages"],
        "roles": ["all"]
    },
    {
        "id": 412,
        "category": "Data Interpretation",
        "difficulty": "Medium",
        "question": "In a survey of 150 developers: 90 use Git, 75 use Docker, and 45 use both. How many developers use Docker but NOT Git?",
        "options": ["25", "30", "35", "40"],
        "correctIndex": 1,
        "explanation": "Docker only = Total Docker - Both = 75 - 45 = 30.",
        "tags": ["venn-diagram"],
        "roles": ["all"]
    },
    {
        "id": 413,
        "category": "Data Interpretation",
        "difficulty": "Hard",
        "question": "A server rack consumes 4.5 kWh at peak (8 hrs/day) and 1.5 kWh at idle (16 hrs/day). If electricity costs $0.10 per kWh, what is the daily operational cost of the server rack?",
        "options": ["$4.80", "$5.40", "$6.00", "$6.60"],
        "correctIndex": 2,
        "explanation": "Peak consumption = 4.5 * 8 = 36 kWh. Idle = 1.5 * 16 = 24 kWh. Total = 60 kWh. Cost = 60 * $0.10 = $6.00.",
        "tags": ["cost-analysis"],
        "roles": ["all"]
    },
    {
        "id": 414,
        "category": "Data Interpretation",
        "difficulty": "Easy",
        "question": "The speed of 4 algorithms solving a benchmark: Algo A: 120ms, Algo B: 80ms, Algo C: 60ms, Algo D: 40ms. By what factor is Algo D faster than Algo A?",
        "options": ["2x", "2.5x", "3x", "4x"],
        "correctIndex": 2,
        "explanation": "Speed factor = Time A / Time D = 120 / 40 = 3x faster.",
        "tags": ["speed-ratio"],
        "roles": ["all"]
    },
    {
        "id": 415,
        "category": "Data Interpretation",
        "difficulty": "Medium",
        "question": "A recruitment drive evaluated 400 candidates: 200 cleared Aptitude, 120 cleared Coding, and 80 cleared Interview. What percentage of the initial pool cleared the Interview round?",
        "options": ["15%", "20%", "25%", "30%"],
        "correctIndex": 1,
        "explanation": "Percentage = (80 / 400) * 100 = 20%.",
        "tags": ["percentages-funnel"],
        "roles": ["all"]
    },

    # =========================================================================
    # 5. BASIC TECHNICAL APTITUDE (30 Questions - Tagged for Roles)
    # =========================================================================
    # --- JAVA & OOP ---
    {
        "id": 501,
        "category": "Basic Technical Aptitude",
        "difficulty": "Easy",
        "question": "Which of the following is NOT an Object-Oriented Programming (OOP) pillar in Java/C++?",
        "options": ["Encapsulation", "Inheritance", "Compilation", "Polymorphism"],
        "correctIndex": 2,
        "explanation": "The four core pillars of OOP are Abstraction, Encapsulation, Inheritance, and Polymorphism. Compilation is a build process.",
        "tags": ["oop", "java", "cpp"],
        "roles": ["java", "software engineer", "full stack", "all"]
    },
    {
        "id": 502,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "In Java, what is the default value of an uninitialized instance variable of type boolean?",
        "options": ["true", "false", "null", "0"],
        "correctIndex": 1,
        "explanation": "In Java, boolean instance variables default to false.",
        "tags": ["java", "basics"],
        "roles": ["java", "software engineer", "full stack"]
    },
    {
        "id": 503,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "What is the key difference between HashMap and Hashtable in Java?",
        "options": [
            "HashMap is synchronized whereas Hashtable is not.",
            "HashMap permits one null key and multiple null values, whereas Hashtable does not permit null keys or values.",
            "Hashtable is faster than HashMap in single-threaded environments.",
            "HashMap is legacy while Hashtable was introduced in Java 8."
        ],
        "correctIndex": 1,
        "explanation": "HashMap is unsynchronized and allows null keys/values; Hashtable is thread-safe/synchronized and rejects null keys/values.",
        "tags": ["java", "collections"],
        "roles": ["java", "software engineer", "backend"]
    },
    {
        "id": 504,
        "category": "Basic Technical Aptitude",
        "difficulty": "Hard",
        "question": "In Java, which memory area stores method bytecode, static variables, and class metadata?",
        "options": ["Heap Memory", "Stack Memory", "Metaspace / Method Area", "Program Counter Register"],
        "correctIndex": 2,
        "explanation": "Since Java 8, class metadata and static variables reside in Metaspace (formerly PermGen / Method Area in native memory).",
        "tags": ["java", "jvm"],
        "roles": ["java", "backend", "software engineer"]
    },
    {
        "id": 505,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "What happens when you invoke thread.start() versus thread.run() in Java?",
        "options": [
            "start() creates a new execution thread; run() executes the method synchronously on the current thread.",
            "run() creates a new execution thread; start() runs synchronously.",
            "There is no functional difference between start() and run().",
            "start() is deprecated in modern Java."
        ],
        "correctIndex": 0,
        "explanation": "start() allocates OS-level resources and invokes the run() method asynchronously on a new call stack.",
        "tags": ["java", "multithreading"],
        "roles": ["java", "backend"]
    },
    {
        "id": 506,
        "category": "Basic Technical Aptitude",
        "difficulty": "Easy",
        "question": "In Spring Boot, which annotation is used to designate a class as a RESTful web controller?",
        "options": ["@Controller", "@RestController", "@Service", "@Component"],
        "correctIndex": 1,
        "explanation": "@RestController combines @Controller and @ResponseBody, automatically serializing return values to JSON.",
        "tags": ["spring-boot", "java"],
        "roles": ["java", "backend", "full stack"]
    },

    # --- PYTHON & DATA ---
    {
        "id": 507,
        "category": "Basic Technical Aptitude",
        "difficulty": "Easy",
        "question": "Which of the following data types is IMMUTABLE in Python?",
        "options": ["List", "Dictionary", "Tuple", "Set"],
        "correctIndex": 2,
        "explanation": "Tuples (along with strings, ints, and frozensets) are immutable in Python; their elements cannot be modified in place.",
        "tags": ["python", "data-types"],
        "roles": ["python", "data", "ai", "software engineer"]
    },
    {
        "id": 508,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "What keyword is used in a Python function to create a Generator that produces a sequence lazily?",
        "options": ["return", "produce", "yield", "emit"],
        "correctIndex": 2,
        "explanation": "The 'yield' keyword pauses execution and emits a value to the caller, resuming state on subsequent next() iterations.",
        "tags": ["python", "generators"],
        "roles": ["python", "data", "software engineer"]
    },
    {
        "id": 509,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "What is the purpose of Python's Global Interpreter Lock (GIL)?",
        "options": [
            "To optimize mathematical calculations on GPU.",
            "To ensure thread-safe memory management in CPython by allowing only one native thread to execute Python bytecode at a time.",
            "To enforce strict type annotations across modules.",
            "To prevent unauthorized system file access."
        ],
        "correctIndex": 1,
        "explanation": "The GIL is a mutex that protects access to Python objects, preventing multiple threads from concurrently executing Python bytecodes in CPython.",
        "tags": ["python", "concurrency"],
        "roles": ["python", "backend", "software engineer"]
    },
    {
        "id": 510,
        "category": "Basic Technical Aptitude",
        "difficulty": "Easy",
        "question": "In Python, what is the output of `bool([])`, `bool([0])`?",
        "options": ["(False, False)", "(False, True)", "(True, False)", "(True, True)"],
        "correctIndex": 1,
        "explanation": "An empty container `[]` evaluates to False, whereas a non-empty container `[0]` has length 1 and evaluates to True.",
        "tags": ["python", "basics"],
        "roles": ["python", "data", "software engineer"]
    },
    {
        "id": 511,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "In Python, which built-in function returns both the index and the item when iterating over an iterable?",
        "options": ["map()", "enumerate()", "zip()", "filter()"],
        "correctIndex": 1,
        "explanation": "`enumerate(iterable)` yields tuples of (index, item).",
        "tags": ["python", "builtins"],
        "roles": ["python", "data", "software engineer"]
    },
    {
        "id": 512,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "In Pandas / NumPy, which method is used to remove missing or NaN values from a DataFrame?",
        "options": ["df.clean()", "df.dropna()", "df.fillnull()", "df.remove_nan()"],
        "correctIndex": 1,
        "explanation": "`df.dropna()` filters out rows or columns containing null/NaN values.",
        "tags": ["python", "pandas", "data"],
        "roles": ["python", "data", "ai"]
    },

    # --- WEB / FRONTEND & JAVASCRIPT ---
    {
        "id": 513,
        "category": "Basic Technical Aptitude",
        "difficulty": "Easy",
        "question": "In JavaScript, what is the difference between `==` and `===`?",
        "options": [
            "`==` checks equality with type coercion; `===` checks strict equality without type coercion.",
            "`===` is used for assigning variables; `==` is used for comparisons.",
            "`==` is strictly faster than `===`.",
            "There is no difference between them in modern ECMAScript."
        ],
        "correctIndex": 0,
        "explanation": "`==` performs automatic type conversion before comparing values; `===` requires both value and type to be identical.",
        "tags": ["javascript", "web"],
        "roles": ["frontend", "web", "full stack", "software engineer"]
    },
    {
        "id": 514,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "What is a Closure in JavaScript?",
        "options": [
            "A function combined with references to its lexical surrounding state.",
            "A method to terminate an event listener loop.",
            "A syntax error caused by unclosed curly braces.",
            "A built-in method to encrypt local storage data."
        ],
        "correctIndex": 0,
        "explanation": "A closure gives an inner function access to its outer enclosing function's scope even after the outer function has finished executing.",
        "tags": ["javascript", "closures"],
        "roles": ["frontend", "web", "full stack"]
    },
    {
        "id": 515,
        "category": "Basic Technical Aptitude",
        "difficulty": "Easy",
        "question": "In CSS layout, which property value creates a flexible grid container along a single dimension?",
        "options": ["display: block;", "display: flex;", "display: inline;", "display: table;"],
        "correctIndex": 1,
        "explanation": "`display: flex;` initializes the CSS Flexbox model for flexible directional layouts.",
        "tags": ["css", "frontend"],
        "roles": ["frontend", "web", "full stack"]
    },
    {
        "id": 516,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "In the browser JavaScript runtime, where are resolved Promise callbacks (e.g. .then) placed?",
        "options": ["Call Stack", "Microtask Queue", "Macrotask (Callback) Queue", "Render Pipeline"],
        "correctIndex": 1,
        "explanation": "Promise reactions and `queueMicrotask` callbacks enter the Microtask Queue, which executes before the next Macrotask (setTimeout/setInterval).",
        "tags": ["javascript", "event-loop"],
        "roles": ["frontend", "web", "full stack"]
    },
    {
        "id": 517,
        "category": "Basic Technical Aptitude",
        "difficulty": "Easy",
        "question": "Which HTTP status code signifies that a resource was successfully created on the server?",
        "options": ["200 OK", "201 Created", "204 No Content", "304 Not Modified"],
        "correctIndex": 1,
        "explanation": "HTTP 201 Created indicates successful request processing resulting in the creation of a new resource.",
        "tags": ["http", "api"],
        "roles": ["all", "frontend", "backend", "full stack"]
    },
    {
        "id": 518,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "In React, what hook is used to perform side effects such as data fetching or DOM subscriptions?",
        "options": ["useState", "useEffect", "useReducer", "useRef"],
        "correctIndex": 1,
        "explanation": "`useEffect` lets developers execute side effects in function components following DOM renders.",
        "tags": ["react", "frontend"],
        "roles": ["frontend", "web", "full stack"]
    },

    # --- DATA STRUCTURES & ALGORITHMS ---
    {
        "id": 519,
        "category": "Basic Technical Aptitude",
        "difficulty": "Easy",
        "question": "What is the average time complexity of searching an element in a balanced Binary Search Tree (BST)?",
        "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"],
        "correctIndex": 1,
        "explanation": "Searching in a balanced BST divides the search space in half at each step, taking O(log n) time.",
        "tags": ["dsa", "trees"],
        "roles": ["all", "software engineer", "java", "python"]
    },
    {
        "id": 520,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "Which data structure operates strictly on a First-In, First-Out (FIFO) principle?",
        "options": ["Stack", "Queue", "Binary Tree", "Heap"],
        "correctIndex": 1,
        "explanation": "A Queue operates on FIFO (First-In, First-Out), while a Stack is LIFO (Last-In, First-Out).",
        "tags": ["dsa", "queue"],
        "roles": ["all", "software engineer", "java", "python"]
    },
    {
        "id": 521,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "What is the worst-case time complexity of QuickSort when a poorly chosen pivot is selected?",
        "options": ["O(n log n)", "O(n)", "O(n^2)", "O(log n)"],
        "correctIndex": 2,
        "explanation": "When the smallest or largest element is consistently chosen as pivot in an already sorted array, QuickSort degrades to O(n^2).",
        "tags": ["dsa", "algorithms", "sorting"],
        "roles": ["all", "software engineer"]
    },
    {
        "id": 522,
        "category": "Basic Technical Aptitude",
        "difficulty": "Hard",
        "question": "Which algorithm is used to find the shortest path in a weighted graph with non-negative edge weights?",
        "options": ["Dijkstra's Algorithm", "Kruskal's Algorithm", "Floyd-Warshall Algorithm", "Prim's Algorithm"],
        "correctIndex": 0,
        "explanation": "Dijkstra's algorithm finds single-source shortest paths in weighted graphs with non-negative edge weights.",
        "tags": ["dsa", "graphs"],
        "roles": ["software engineer", "java", "python"]
    },
    {
        "id": 523,
        "category": "Basic Technical Aptitude",
        "difficulty": "Easy",
        "question": "Which data structure is typically used to implement Breadth-First Search (BFS) on a graph?",
        "options": ["Stack", "Queue", "Priority Queue", "Hash Map"],
        "correctIndex": 1,
        "explanation": "BFS uses a Queue to explore neighbor nodes level by level.",
        "tags": ["dsa", "graphs"],
        "roles": ["all", "software engineer"]
    },

    # --- SQL & DATABASE SYSTEMS ---
    {
        "id": 524,
        "category": "Basic Technical Aptitude",
        "difficulty": "Easy",
        "question": "In SQL, which clause is used to filter records resulting from a GROUP BY aggregation?",
        "options": ["WHERE", "HAVING", "FILTER", "ORDER BY"],
        "correctIndex": 1,
        "explanation": "`HAVING` filters aggregated group records, whereas `WHERE` filters individual rows before grouping.",
        "tags": ["sql", "database"],
        "roles": ["all", "backend", "full stack", "data"]
    },
    {
        "id": 525,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "What is the primary function of a Database Index (e.g. B-Tree)?",
        "options": [
            "To encrypt table rows against unauthorized access.",
            "To accelerate data retrieval (SELECT queries) at the cost of slight overhead on INSERT/UPDATE operations.",
            "To automatically enforce foreign key cascade deletes.",
            "To compress table storage size on disk."
        ],
        "correctIndex": 1,
        "explanation": "Indexes provide quick lookup access trees (B-Trees/Hash) to speed up queries at the expense of storage and write performance.",
        "tags": ["sql", "indexing"],
        "roles": ["all", "backend", "data", "software engineer"]
    },
    {
        "id": 526,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "What does the ACID acronym stand for in relational database transactions?",
        "options": [
            "Atomicity, Consistency, Isolation, Durability",
            "Accuracy, Concurrency, Integrity, Dependability",
            "Access, Control, Isolation, Distribution",
            "Availability, Consistency, Invariance, Durability"
        ],
        "correctIndex": 0,
        "explanation": "ACID stands for Atomicity (all-or-nothing), Consistency (rules preserved), Isolation (independent transactions), and Durability (committed data persists).",
        "tags": ["database", "acid"],
        "roles": ["all", "backend", "software engineer"]
    },
    {
        "id": 527,
        "category": "Basic Technical Aptitude",
        "difficulty": "Easy",
        "question": "Which SQL JOIN returns all rows from the left table, and matching rows from the right table (with NULLs for unmatched rows)?",
        "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"],
        "correctIndex": 1,
        "explanation": "A `LEFT JOIN` (or LEFT OUTER JOIN) guarantees all rows from the left table are returned regardless of matches.",
        "tags": ["sql", "joins"],
        "roles": ["all", "backend", "data", "full stack"]
    },

    # --- SYSTEM DESIGN, OS & NETWORKING ---
    {
        "id": 528,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "In computer networking, which protocol provides reliable, connection-oriented byte stream transmission with error checking?",
        "options": ["UDP", "TCP", "ICMP", "IP"],
        "correctIndex": 1,
        "explanation": "TCP (Transmission Control Protocol) is connection-oriented, reliable, and handles retransmission, ordering, and flow control.",
        "tags": ["networking", "tcp-ip"],
        "roles": ["all", "software engineer", "backend"]
    },
    {
        "id": 529,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "What is the key difference between a Process and a Thread in modern Operating Systems?",
        "options": [
            "Processes share memory by default; Threads have completely isolated address spaces.",
            "A Process has its own independent address space; Threads within the same process share code, data, and resources.",
            "Threads are managed exclusively by hardware; Processes are managed by software.",
            "A system cannot have multiple threads inside one process."
        ],
        "correctIndex": 1,
        "explanation": "A process represents an isolated executing program with its own memory space; threads are lightweight execution paths sharing the process's memory.",
        "tags": ["os", "processes-threads"],
        "roles": ["all", "software engineer", "backend"]
    },
    {
        "id": 530,
        "category": "Basic Technical Aptitude",
        "difficulty": "Medium",
        "question": "In modern software architecture, what is the primary benefit of deploying stateless microservices behind a Load Balancer?",
        "options": [
            "Elimination of all network latency.",
            "Seamless horizontal scalability since any request can be handled by any service replica without session affinity.",
            "Automatic conversion of SQL queries to NoSQL format.",
            "Guaranteed zero memory consumption on worker nodes."
        ],
        "correctIndex": 1,
        "explanation": "Stateless services store state in external databases or caches, enabling easy horizontal scaling by spinning up/down identical replicas.",
        "tags": ["system-design", "microservices"],
        "roles": ["all", "software engineer", "backend", "full stack"]
    }
]
