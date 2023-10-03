import pandas as pd
import re
DEBATE_FILE = "debateRaw.txt"
df = pd.DataFrame(columns=['Candidate', 'Response'])
#pd.set_option('display.max_rows', None)
bidenText = ''
buttText = ''
bernieText = ''
warrenText = ''
amyText = ''
bloombergText = ''

with open(DEBATE_FILE) as debate:
    for eachLine in debate:
        eachLine = eachLine.lower()
        candidate = ''
        response = ''

        # Process Eachline where Biden is speaking
        if "joe biden" in eachLine[:10]:
            candidate = 'Joe Biden'
            response = eachLine[10:]
            response = re.sub("[^a-zA-Z ]", ' ', response)
            new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
            df = pd.concat([df, new_row], ignore_index=True)
            bidenText = bidenText + response

        elif "pete buttigieg" in eachLine[:17]:
            candidate = 'Pete Buttigieg'
            response = eachLine[17:]
            response = re.sub("[^a-zA-Z ]", ' ', response)
            new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
            df = pd.concat([df, new_row], ignore_index=True)
            buttText = buttText + response

        elif "bernie sanders" in eachLine[:15]:
            candidate = 'Bernie Sanders'
            response = eachLine[15:]
            response = re.sub("[^a-zA-Z ]", ' ', response)
            new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
            df = pd.concat([df, new_row], ignore_index=True)
            bernieText = bernieText + response

        elif "michael bloomberg" in eachLine[:18]:
            candidate = 'Michael Bloomberg'
            response = eachLine[18:]
            response = re.sub("[^a-zA-Z ]", ' ', response)
            new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
            df = pd.concat([df, new_row], ignore_index=True)
            bloombergText = bloombergText + response

        elif "amy klobuchar" in eachLine[:14]:
            candidate = 'Amy Klobuchar'
            response = eachLine[14:]
            response = re.sub("[^a-zA-Z ]", ' ', response)
            new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
            df = pd.concat([df, new_row], ignore_index=True)
            amyText = amyText + response

        elif "elizabeth warren" in eachLine[:16]:
            candidate = 'Elizabeth Warren'
            response = eachLine[16:]
            response = re.sub("[^a-zA-Z ]", ' ', response)
            new_row = pd.DataFrame({'Candidate': [candidate], 'Response': [response]})
            df = pd.concat([df, new_row], ignore_index=True)
            warrenText = warrenText + response

print(df)
